



# Python also has support for Frozen sets.
# Those sets are just like the normal sets but they are immutable: So doesn't provide support adding or removing items.

set_that_cannot_changed = frozenset({1, 2, 3})

set_that_cannot_changed.add(4) # Will cause AttributeError: 'frozenset' object has no attribute 'add'