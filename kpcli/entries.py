class Entry:
    def __init__(self, name, group):
        self.name = name
        self.group = group
    def __str__(self):
        return self.name

class Entries:
    def __init__(self, entry_list):
        self.entry_list = entry_list
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= len(self.entry_list):
            raise StopIteration
        item = self.entry_list[self.i]
        self.i += 1
        return item
    def group_max_size(self):
        group_set = set([entry.group for entry in self.entry_list])
        return max([len(group) for group in group_set])
