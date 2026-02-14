from textual.screen import Screen
from textual.widgets import Static, Button
from textual.containers import Container, Horizontal
from textual.binding import Binding
from textual.app import ComposeResult

from puzzles import Difficulty


TITLE_ART = """
[bold cyan]
███╗   ███╗ ██████╗ ██╗     ███████╗ ██████╗██████╗  █████╗ ███████╗████████╗
████╗ ████║██╔═══██╗██║     ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
██╔████╔██║██║   ██║██║     █████╗  ██║     ██████╔╝███████║█████╗     ██║   
██║╚██╔╝██║██║   ██║██║     ██╔══╝  ██║     ██╔══██╗██╔══██║██╔══╝     ██║   
██║ ╚═╝ ██║╚██████╔╝███████╗███████╗╚██████╗██║  ██║██║  ██║██║        ██║   
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝   
[/]
[dim]Build molecules. Beat the clock. Master chemistry.[/]
"""


class MenuScreen(Screen):
    CSS = """
    MenuScreen {
        align: center middle;
    }
    #menu-container {
        width: 80;
        height: auto;
        align: center middle;
    }
    #title {
        text-align: center;
        width: 100%;
        margin-bottom: 2;
    }
    #button-row {
        align: center middle;
        width: 100%;
        height: auto;
        margin: 1;
    }
    .difficulty-btn {
        margin: 0 2;
        min-width: 16;
    }
    #easy-btn {
        background: green;
    }
    #medium-btn {
        background: orange;
    }
    #hard-btn {
        background: red;
    }
    #info {
        text-align: center;
        margin-top: 2;
        color: $text-muted;
    }
    """

    BINDINGS = [
        Binding("1", "start_easy", "Easy"),
        Binding("2", "start_medium", "Medium"),
        Binding("3", "start_hard", "Hard"),
        Binding("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        with Container(id="menu-container"):
            yield Static(TITLE_ART, id="title")
            with Horizontal(id="button-row"):
                yield Button("1. Easy", id="easy-btn", classes="difficulty-btn")
                yield Button("2. Medium", id="medium-btn", classes="difficulty-btn")
                yield Button("3. Hard", id="hard-btn", classes="difficulty-btn")
            yield Static("[dim]Press 1, 2, 3 to select difficulty | Q to quit[/]", id="info")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "easy-btn":
            self.start_game(Difficulty.EASY)
        elif event.button.id == "medium-btn":
            self.start_game(Difficulty.MEDIUM)
        elif event.button.id == "hard-btn":
            self.start_game(Difficulty.HARD)

    def action_start_easy(self) -> None:
        self.start_game(Difficulty.EASY)

    def action_start_medium(self) -> None:
        self.start_game(Difficulty.MEDIUM)

    def action_start_hard(self) -> None:
        self.start_game(Difficulty.HARD)

    def start_game(self, difficulty: Difficulty) -> None:
        self.app.start_puzzle(difficulty)

    def action_quit(self) -> None:
        self.app.exit()
