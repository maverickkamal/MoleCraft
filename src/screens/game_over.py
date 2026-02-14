from textual.screen import ModalScreen
from textual.widgets import Static, Button
from textual.containers import Horizontal, Vertical
from textual.binding import Binding
from textual.app import ComposeResult


class GameOverModal(ModalScreen):
    CSS = """
    GameOverModal {
        align: center middle;
    }
    #modal-container {
        width: 40;
        height: auto;
        background: $surface;
        border: thick $error;
        padding: 2;
    }
    #title {
        text-align: center;
        margin-bottom: 1;
    }
    #score {
        text-align: center;
        margin-bottom: 2;
    }
    #button-row {
        align: center middle;
        height: auto;
    }
    .modal-btn {
        margin: 0 1;
    }
    """

    BINDINGS = [
        Binding("r", "restart", "Restart"),
        Binding("m", "menu", "Menu"),
        Binding("escape", "menu", "Menu", show=False),
    ]

    def __init__(self, score: int, high_score: int = 0, reason: str = "Time's up!") -> None:
        super().__init__()
        self.final_score = score
        self.high_score = high_score
        self.reason = reason
        self.is_new_record = score > 0 and score >= high_score

    def compose(self) -> ComposeResult:
        with Vertical(id="modal-container"):
            yield Static(f"[bold red]{self.reason}[/]", id="title")
            if self.is_new_record:
                yield Static(f"[bold bright_yellow]NEW HIGH SCORE![/]", id="record")
            yield Static(f"Final Score: [bold]{self.final_score}[/]  |  Best: [bold]{self.high_score}[/]", id="score")
            with Horizontal(id="button-row"):
                yield Button("Restart (R)", id="restart-btn", classes="modal-btn", variant="primary")
                yield Button("Menu (M)", id="menu-btn", classes="modal-btn", variant="default")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "restart-btn":
            self.action_restart()
        elif event.button.id == "menu-btn":
            self.action_menu()

    def action_restart(self) -> None:
        self.app.restart_game()

    def action_menu(self) -> None:
        self.app.return_to_menu()
