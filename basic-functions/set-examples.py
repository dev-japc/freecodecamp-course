# Set operations
set_a = {1, 2, 3, 4}
set_b = {2, 3, 4, 5, 6}

# Union, intersection, difference, symmetric difference
print(set_a.union(set_b))                    # or set_a | set_b
print(set_a.intersection(set_b))             # or set_a & set_b
print(set_a.difference(set_b))               # or set_a - set_b
print(set_a.symmetric_difference(set_b))     # or set_a ^ set_b

# Subset and superset checks
print(set_a.issubset(set_b))
print(set_a.issuperset(set_b))
print(set_a.isdisjoint(set_b))