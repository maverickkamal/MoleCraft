from textual.screen import ModalScreen
from textual.widgets import Static, Button
from textual.containers import Vertical, Horizontal
from textual.binding import Binding
from textual.app import ComposeResult


class PauseModal(ModalScreen):
    CSS = """
    PauseModal {
        align: center middle;
    }
    #pause-container {
        width: 44;
        height: auto;
        background: $surface;
        border: thick $primary;
        padding: 2 4;
    }
    #pause-title {
        text-align: center;
        width: 100%;
        margin-bottom: 1;
    }
    #pause-hint {
        text-align: center;
        width: 100%;
        margin-bottom: 2;
        color: $text-muted;
    }
    #pause-buttons {
        align: center middle;
        height: auto;
    }
    .pause-btn {
        margin: 0 1;
        min-width: 16;
    }
    """

    BINDINGS = [
        Binding("p", "resume", "Resume", show=True),
        Binding("escape", "resume", "Resume", show=False),
    ]

    def compose(self) -> ComposeResult:
        with Vertical(id="pause-container"):
            yield Static("[bold yellow]⏸  PAUSED[/]", id="pause-title")
            yield Static(f"[dim]Score: {self.app.score}[/]", id="pause-hint")
            with Horizontal(id="pause-buttons"):
                yield Button("Resume (P)", id="resume-btn", classes="pause-btn", variant="primary")
                yield Button("Quit to Menu", id="menu-btn", classes="pause-btn", variant="default")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "resume-btn":
            self.action_resume()
        elif event.button.id == "menu-btn":
            self.dismiss()
            self.app.return_to_menu()

    def action_resume(self) -> None:
        self.dismiss()
