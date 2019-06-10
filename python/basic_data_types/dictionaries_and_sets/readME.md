


Python sets and dictionaries can both be constructed using curly braces:

my_dict = {'a': 1, 'b': 2}

my_set = {1, 2, 3}

The interpreter (and human readers) can distinguish between them based on their contents. 
However it isn't possible to distinguish between an empty set and an empty dict, 
so this case you need to use set() for empty sets to disambiguate.