import random

from textual.app import App

from screens.menu import MenuScreen
from screens.game import GameScreen
from screens.game_over import GameOverModal
from puzzles import Difficulty, get_puzzles, Puzzle
from widgets.puzzle_grid import PuzzleGrid
from save_manager import load_save, write_save


class MoleCraftApp(App):
    CSS = """
    Screen {
        background: $surface;
    }
    """

    SCREENS = {
        "menu": MenuScreen,
    }

    def __init__(self) -> None:
        super().__init__()
        self.save_data = load_save()
        self.score = 0
        self.current_puzzle: Puzzle | None = None
        self.current_difficulty: Difficulty | None = None

    def on_mount(self) -> None:
        self.push_screen("menu")

    def start_puzzle(self, difficulty: Difficulty) -> None:
        self.current_difficulty = difficulty
        puzzles = get_puzzles(difficulty)
        self.current_puzzle = random.choice(puzzles)
        self.push_screen(GameScreen(self.current_puzzle))

    def show_game_over(self, reason: str) -> None:
        self._save_high_score()
        self.push_screen(GameOverModal(self.score, self.save_data["high_score"], reason))

    def restart_game(self) -> None:
        self.score = 0
        while len(self.screen_stack) > 1:
            self.pop_screen()
        self.start_puzzle(self.current_difficulty)

    def return_to_menu(self) -> None:
        self.score = 0
        while len(self.screen_stack) > 1:
            self.pop_screen()

    def _record_solve(self, puzzle: Puzzle, time_remaining: int) -> None:
        diff_key = self.current_difficulty.value
        completed = self.save_data["completed_puzzles"]
        if puzzle.name not in completed[diff_key]:
            completed[diff_key].append(puzzle.name)
        self.save_data["total_solved"] = self.save_data.get("total_solved", 0) + 1
        solve_time = puzzle.time_limit - time_remaining
        fastest = self.save_data.get("fastest_solve")
        if fastest is None or solve_time < fastest:
            self.save_data["fastest_solve"] = solve_time
        self._save_high_score()

    def _save_high_score(self) -> None:
        if self.score > self.save_data["high_score"]:
            self.save_data["high_score"] = self.score
        self.save_data["last_difficulty"] = self.current_difficulty.value if self.current_difficulty else "easy"
        write_save(self.save_data)

    def check_solution(self, grid: PuzzleGrid) -> None:
        player_atoms = set()
        for atom in grid.atoms.values():
            if (atom.x, atom.y) not in grid.locked_positions:
                player_atoms.add((atom.element, atom.x, atom.y))

        target_atoms = set()
        for elem, x, y in self.current_puzzle.target_atoms:
            if elem != "C":
                target_atoms.add((elem, x, y))

        player_bonds = set()
        for bond in grid.bonds.values():
            a = grid.atoms.get(bond.atom_a_id)
            b = grid.atoms.get(bond.atom_b_id)
            if a and b:
                key = tuple(sorted([(a.x, a.y), (b.x, b.y)]))
                player_bonds.add((key, bond.order))

        target_bonds = set()
        for (x1, y1), (x2, y2), order in self.current_puzzle.target_bonds:
            key = tuple(sorted([(x1, y1), (x2, y2)]))
            target_bonds.add((key, order))

        atoms_correct = player_atoms == target_atoms
        bonds_correct = player_bonds == target_bonds

        if atoms_correct and bonds_correct:
            time_bonus = self.screen.time_left * 10
            self.score += 100 + time_bonus
            self.notify(f"Correct! +{100 + time_bonus} points", severity="information")
            self._record_solve(self.current_puzzle, self.screen.time_left)
            self.pop_screen()
            self.start_puzzle(self.current_difficulty)
        else:
            missing_atoms = target_atoms - player_atoms
            extra_atoms = player_atoms - target_atoms
            if missing_atoms:
                self.notify("Missing atoms!", severity="error")
            elif extra_atoms:
                self.notify("Extra atoms!", severity="error")
            elif not bonds_correct:
                self.notify("Bonds incorrect!", severity="error")


def main() -> None:
    app = MoleCraftApp()
    app.run()


if __name__ == "__main__":
    main()
