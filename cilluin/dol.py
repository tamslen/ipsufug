from rich import print as cprint
from rich.console import Console
from rich.style import Style

console = Console()

network = "my_network"

style = Style(color="black")

cprint(f"  {network:<12} failed", style=style)

