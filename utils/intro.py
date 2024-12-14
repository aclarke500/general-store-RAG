import pyfiglet
from rich.console import Console
from rich.text import Text


def display_ascii_art():
    console = Console()
    ascii_art = pyfiglet.figlet_format("JSI General Store")
    console.print(Text(ascii_art, style="bold cyan"))
    console.print(Text("Welcome to the JSI General RAG Time Store!", style="bold green"))
    console.print(Text("We are a store that sells all sorts of items. Feel free to talk to our AI assistant, Beedle. I'm sure he will be able to help you find what you need!", style="bold green"))

