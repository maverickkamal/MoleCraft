from typing import Dict, Optional
from copy import deepcopy

from textual.widgets import Static
from textual.reactive import reactive
from textual.message import Message
from rich.text import Text

from models import Atom, Bond
from puzzles import Puzzle


class PuzzleGrid(Static):
    GRID_WIDTH = 60
    GRID_HEIGHT = 16

    cursor_x: reactive[int] = reactive(30)
    cursor_y: reactive[int] = reactive(8)

    ELEMENT_COLORS = {
        "C": "bright_white",
        "H": "bright_yellow",
        "O": "bright_red",
        "N": "bright_blue",
        "Cl": "bright_green",
    }

    MAX_VALENCY = {
        "C": 4,
        "N": 3,
        "O": 2,
        "H": 1,
        "Cl": 1,
    }

    class CursorMoved(Message):
        def __init__(self, x: int, y: int) -> None:
            super().__init__()
            self.x = x
            self.y = y

    class AtomPlaced(Message):
        pass

    class BondCreated(Message):
        pass

    MAX_UNDO = 50

    def __init__(self, puzzle: Puzzle) -> None:
        super().__init__()
        self.can_focus = True
        self.puzzle = puzzle
        self.atoms: Dict[str, Atom] = {}
        self.bonds: Dict[str, Bond] = {}
        self.selected_atom_id: Optional[str] = None
        self.current_element = "H"
        self.locked_positions: set = set()
        self.hint_positions: Dict[tuple, str] = {}
        self.show_hints = True
        self._undo_stack: list = []
        self._setup_puzzle()

    def _setup_puzzle(self) -> None:
        self.hint_positions.clear()
        for x, y in self.puzzle.carbons:
            atom = Atom(element="C", x=x, y=y)
            self.atoms[atom.id] = atom
            self.locked_positions.add((x, y))
        for elem, x, y in self.puzzle.target_atoms:
            if elem == "C":
                continue
            self.hint_positions[(x, y)] = elem

    def _push_undo(self) -> None:
        snapshot = (deepcopy(self.atoms), deepcopy(self.bonds), self.selected_atom_id)
        self._undo_stack.append(snapshot)
        if len(self._undo_stack) > self.MAX_UNDO:
            self._undo_stack.pop(0)

    def undo(self) -> bool:
        if not self._undo_stack:
            return False
        self.atoms, self.bonds, self.selected_atom_id = self._undo_stack.pop()
        self.refresh()
        return True

    def on_mount(self) -> None:
        if self.puzzle.carbons:
            self.cursor_x = self.puzzle.carbons[0][0]
            self.cursor_y = self.puzzle.carbons[0][1]
        self.refresh()

    def get_atom_at(self, x: int, y: int) -> Optional[Atom]:
        for atom in self.atoms.values():
            if atom.x == x and atom.y == y:
                return atom
        return None

    def get_bond_count(self, atom: Atom) -> int:
        total = 0
        for bond_id in atom.bonds:
            if bond_id in self.bonds:
                total += self.bonds[bond_id].order
        return total

    def remaining_bonds(self, atom: Atom) -> int:
        max_val = self.MAX_VALENCY.get(atom.element, 4)
        return max_val - self.get_bond_count(atom)

    def add_atom(self, element: str) -> None:
        if (self.cursor_x, self.cursor_y) in self.locked_positions:
            return
        self._push_undo()
        existing = self.get_atom_at(self.cursor_x, self.cursor_y)
        if existing:
            if (existing.x, existing.y) in self.locked_positions:
                return
            for bond_id in list(existing.bonds):
                self.remove_bond(bond_id)
            self.atoms.pop(existing.id)
        atom = Atom(element=element, x=self.cursor_x, y=self.cursor_y)
        self.atoms[atom.id] = atom
        self.post_message(self.AtomPlaced())
        self.refresh()

    def delete_atom(self) -> None:
        if (self.cursor_x, self.cursor_y) in self.locked_positions:
            return
        existing = self.get_atom_at(self.cursor_x, self.cursor_y)
        if not existing:
            return
        self._push_undo()
        for bond_id in list(existing.bonds):
            self.remove_bond(bond_id)
        self.atoms.pop(existing.id)
        self.refresh()

    def remove_bond(self, bond_id: str) -> None:
        if bond_id in self.bonds:
            bond = self.bonds[bond_id]
            if bond.atom_a_id in self.atoms:
                a = self.atoms[bond.atom_a_id]
                if bond_id in a.bonds:
                    a.bonds.remove(bond_id)
            if bond.atom_b_id in self.atoms:
                b = self.atoms[bond.atom_b_id]
                if bond_id in b.bonds:
                    b.bonds.remove(bond_id)
            del self.bonds[bond_id]

    def toggle_select(self) -> None:
        atom = self.get_atom_at(self.cursor_x, self.cursor_y)
        if not atom:
            self.selected_atom_id = None
            self.refresh()
            return
        if self.selected_atom_id is None:
            self.selected_atom_id = atom.id
            self.refresh()
            return
        if self.selected_atom_id == atom.id:
            self.selected_atom_id = None
            self.refresh()
            return
        selected = self.atoms.get(self.selected_atom_id)
        if selected:
            self._push_undo()
            self.create_bond(selected, atom)
        self.selected_atom_id = None
        self.refresh()

    def get_existing_bond(self, a: Atom, b: Atom) -> Optional[Bond]:
        for bond in self.bonds.values():
            if (bond.atom_a_id == a.id and bond.atom_b_id == b.id) or \
               (bond.atom_a_id == b.id and bond.atom_b_id == a.id):
                return bond
        return None

    def can_add_bond(self, atom: Atom, order: int = 1) -> bool:
        return self.remaining_bonds(atom) >= order

    def create_bond(self, source: Atom, target: Atom) -> None:
        existing = self.get_existing_bond(source, target)
        if existing:
            if self.can_add_bond(source, 1) and self.can_add_bond(target, 1):
                existing.order += 1
                if existing.order > 3:
                    self.remove_bond(existing.id)
                self.post_message(self.BondCreated())
            return
        if source.x != target.x and source.y != target.y:
            return
        if not self.can_add_bond(source, 1) or not self.can_add_bond(target, 1):
            return
        orientation = "V" if source.x == target.x else "H"
        bond = Bond(atom_a_id=source.id, atom_b_id=target.id, orientation=orientation)
        self.bonds[bond.id] = bond
        source.bonds.append(bond.id)
        target.bonds.append(bond.id)
        self.post_message(self.BondCreated())

    def get_bond_cells(self) -> Dict[tuple, str]:
        cells: Dict[tuple, str] = {}
        for bond in self.bonds.values():
            a = self.atoms.get(bond.atom_a_id)
            b = self.atoms.get(bond.atom_b_id)
            if not a or not b:
                continue
            chars = {1: ("─", "│"), 2: ("═", "║"), 3: ("≡", "┃")}
            h_char, v_char = chars.get(bond.order, ("─", "│"))
            if bond.orientation == "H":
                x1, x2 = min(a.x, b.x), max(a.x, b.x)
                for x in range(x1 + 1, x2):
                    cells[(x, a.y)] = h_char
            else:
                y1, y2 = min(a.y, b.y), max(a.y, b.y)
                for y in range(y1 + 1, y2):
                    cells[(a.x, y)] = v_char
        return cells

    def render(self) -> Text:
        bond_cells = self.get_bond_cells()
        text = Text()
        for y in range(self.GRID_HEIGHT):
            for x in range(self.GRID_WIDTH):
                atom = self.get_atom_at(x, y)
                is_cursor = x == self.cursor_x and y == self.cursor_y
                is_selected = self.selected_atom_id and atom and atom.id == self.selected_atom_id
                is_locked = (x, y) in self.locked_positions
                hint_elem = self.hint_positions.get((x, y))
                if atom:
                    ch = atom.element[0]
                    color = self.ELEMENT_COLORS.get(atom.element, "white")
                    if is_selected:
                        text.append(ch, style=f"bold {color} on dark_green")
                    elif is_cursor:
                        text.append(ch, style=f"bold {color} reverse")
                    elif is_locked:
                        text.append(ch, style=f"bold {color}")
                    else:
                        text.append(ch, style=color)
                elif (x, y) in bond_cells:
                    text.append(bond_cells[(x, y)], style="cyan")
                elif self.show_hints and hint_elem:
                    ch = hint_elem[0].lower()
                    if is_cursor:
                        text.append(ch, style="dim bright_magenta reverse")
                    else:
                        text.append(ch, style="dim bright_black")
                elif is_cursor:
                    text.append("◊", style="bold bright_magenta")
                else:
                    text.append("·", style="bright_black")
            text.append("\n")
        return text

    def watch_cursor_x(self) -> None:
        self.refresh()
        self.post_message(self.CursorMoved(self.cursor_x, self.cursor_y))

    def watch_cursor_y(self) -> None:
        self.refresh()
        self.post_message(self.CursorMoved(self.cursor_x, self.cursor_y))

    def move_cursor(self, dx: int, dy: int) -> None:
        new_x = self.cursor_x + dx
        new_y = self.cursor_y + dy
        if 0 <= new_x < self.GRID_WIDTH:
            self.cursor_x = new_x
        if 0 <= new_y < self.GRID_HEIGHT:
            self.cursor_y = new_y
