import pytest
from kpcli.entries import Entries, Entry

def test_entries():
    entries = Entries(
        [Entry('name1','group1'),
        Entry('name1','group1'),
        Entry('name2','group1')]
    )
    assert entries.group_max_size() == 6
