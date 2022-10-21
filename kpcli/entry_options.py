import sys
from kpcli.getch import getch

class EntryOptions:
    def __init__(self, typer):
        self.typer = typer
        self.options = [
                ["y", "y", "copy password to clipboard"],
                ["y", "u", "copy user to clipboard"],
                ["d", "d", "delete entry"],
            ]
    def wait_key(self):
        return getch()
    def show(self):
        self.typer.echo("-------------------------------------------------------------")
        self.typer.echo("yy\t copy password to clipboard")
        self.typer.echo("yu\t copy user to clipboard")
        self.typer.echo("dd\t delete entry")
        self.typer.echo("ESC\t return to search")
        key = None
        ESC = 27
        while key == None or ord(key) != ESC: 
            key = self.wait_key()
            filtered = list(filter(
                    lambda option: option[0] == key,
                    self.options))
            self.typer.echo(filtered)
            if len(filtered) > 0:
                while ord(key) != ESC:
                    key = self.wait_key()
                    filtered2 = list(filter(
                            lambda option: option[1] == key,
                            filtered))
                    if(len(filtered2) == 0):
                        break
                    self.typer.echo(filtered2)





