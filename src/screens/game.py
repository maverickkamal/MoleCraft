from textual.screen import Screen
from textual.widgets import Static, Button, Footer
from textual.containers import Container, Horizontal, Vertical
from textual.binding import Binding
from textual.app import ComposeResult
from textual.timer import Timer

from src.widgets.puzzle_grid import PuzzleGrid
from src.puzzles import Puzzle


class GameScreen(Screen):
    CSS = """
    GameScreen {
        layout: vertical;
    }
    #header-bar {
        height: 3;
        background: $primary-darken-2;
        padding: 0 2;
    }
    #puzzle-name {
        width: 1fr;
        text-align: left;
    }
    #timer {
        width: auto;
        text-align: right;
        color: $warning;
    }
    #grid-container {
        height: 1fr;
        padding: 1;
    }
    PuzzleGrid {
        width: 100%;
        height: 100%;
    }
    #toolbar {
        height: 5;
        background: $surface;
        padding: 1;
    }
    #element-row {
        height: auto;
        align: center middle;
    }
    .element-btn {
        min-width: 8;
        margin: 0 1;
    }
    #h-btn { background: $warning; color: black; }
    #o-btn { background: red; }
    #n-btn { background: blue; }
    #cl-btn { background: green; }
    #bond-info {
        text-align: center;
        margin-top: 1;
    }
    #action-row {
        height: auto;
        align: center middle;
        margin-top: 1;
    }
    .action-btn {
        margin: 0 2;
    }
    """

    BINDINGS = [
        Binding("up", "move_up", "Up", show=False),
        Binding("down", "move_down", "Down", show=False),
        Binding("left", "move_left", "Left", show=False),
        Binding("right", "move_right", "Right", show=False),
        Binding("h", "add_h", "H"),
        Binding("o", "add_o", "O"),
        Binding("n", "add_n", "N"),
        Binding("l", "add_cl", "Cl"),
        Binding("space", "toggle_select", "Bond"),
        Binding("delete", "delete", "Del"),
        Binding("backspace", "delete", "Del", show=False),
        Binding("enter", "submit", "Submit"),
        Binding("r", "reset", "Reset"),
        Binding("escape", "back", "Back"),
    ]

    def __init__(self, puzzle: Puzzle) -> None:
        super().__init__()
        self.puzzle = puzzle
        self.time_left = puzzle.time_limit
        self.timer: Timer | None = None

    def compose(self) -> ComposeResult:
        with Horizontal(id="header-bar"):
            yield Static(f"[bold]{self.puzzle.name}[/] ({self.puzzle.formula})", id="puzzle-name")
            yield Static(f"⏱ {self.time_left:02d}s", id="timer")
        with Container(id="grid-container"):
            yield PuzzleGrid(self.puzzle)
        with Vertical(id="toolbar"):
            with Horizontal(id="element-row"):
                yield Button("H", id="h-btn", classes="element-btn")
                yield Button("O", id="o-btn", classes="element-btn")
                yield Button("N", id="n-btn", classes="element-btn")
                yield Button("Cl", id="cl-btn", classes="element-btn")
                yield Static("  │  ", id="sep")
                yield Button("Submit", id="submit-btn", classes="action-btn", variant="success")
                yield Button("Reset", id="reset-btn", classes="action-btn", variant="warning")
            yield Static("[dim]Arrow keys: move | H/O/N/L: place atom | Space: bond | Enter: submit[/]", id="bond-info")
        yield Footer()

    def on_mount(self) -> None:
        self.grid = self.query_one(PuzzleGrid)
        self.grid.focus()
        self.timer = self.set_interval(1, self.tick)
        self.update_status()

    def tick(self) -> None:
        self.time_left -= 1
        self.query_one("#timer", Static).update(f"⏱ {self.time_left:02d}s")
        if self.time_left <= 0:
            self.timer.stop()
            self.notify("Time's up!", severity="error")

    def update_status(self) -> None:
        atom = self.grid.get_atom_at(self.grid.cursor_x, self.grid.cursor_y)
        if atom:
            rem = self.grid.remaining_bonds(atom)
            info = f"{atom.element}: {rem} bonds left"
        else:
            info = "Empty cell"
        self.sub_title = info

    def on_puzzle_grid_cursor_moved(self, event: PuzzleGrid.CursorMoved) -> None:
        self.update_status()

    def on_puzzle_grid_atom_placed(self, event: PuzzleGrid.AtomPlaced) -> None:
        self.update_status()

    def on_puzzle_grid_bond_created(self, event: PuzzleGrid.BondCreated) -> None:
        self.update_status()

    def action_move_up(self) -> None:
        self.grid.move_cursor(0, -1)

    def action_move_down(self) -> None:
        self.grid.move_cursor(0, 1)

    def action_move_left(self) -> None:
        self.grid.move_cursor(-1, 0)

    def action_move_right(self) -> None:
        self.grid.move_cursor(1, 0)

    def action_add_h(self) -> None:
        self.grid.add_atom("H")

    def action_add_o(self) -> None:
        self.grid.add_atom("O")

    def action_add_n(self) -> None:
        self.grid.add_atom("N")

    def action_add_cl(self) -> None:
        self.grid.add_atom("Cl")

    def action_toggle_select(self) -> None:
        self.grid.toggle_select()

    def action_delete(self) -> None:
        self.grid.delete_atom()

    def action_submit(self) -> None:
        self.app.check_solution(self.grid)

    def action_reset(self) -> None:
        self.grid.atoms.clear()
        self.grid.bonds.clear()
        self.grid.locked_positions.clear()
        self.grid.selected_atom_id = None
        self.grid._setup_puzzle()
        self.grid.refresh()
        self.time_left = self.puzzle.time_limit
        self.query_one("#timer", Static).update(f"⏱ {self.time_left:02d}s")
        self.notify("Puzzle reset")

    def action_back(self) -> None:
        if self.timer:
            self.timer.stop()
        self.app.pop_screen()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn_id = event.button.id
        if btn_id == "h-btn":
            self.action_add_h()
        elif btn_id == "o-btn":
            self.action_add_o()
        elif btn_id == "n-btn":
            self.action_add_n()
        elif btn_id == "cl-btn":
            self.action_add_cl()
        elif btn_id == "submit-btn":
            self.action_submit()
        elif btn_id == "reset-btn":
            self.action_reset()
