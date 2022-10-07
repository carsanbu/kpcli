from pyfzf.pyfzf import FzfPrompt

class Search:
    def __init__(self, entries):
        self.entries = entries
    def select(self):
        fzf = FzfPrompt()
        return fzf.prompt(self.entries)
