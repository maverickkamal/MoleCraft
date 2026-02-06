from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.binding import Binding

class MoleCraftApp(App):
    CSS = """
    Screen {
        background: $surface;
    }
    """

def main() -> None:
    app = MoleCraftApp()
    app.run()


if __name__ == "__main__":
    main()