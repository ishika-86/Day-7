ab = set ([1, 2, 3, 4, 5])
print(ab)

# remove single elements
ab.pop()
print(ab)

# remove a element if it exists
ab.discard(2)
print(ab)

# remove a element if it exists
ab.discard(12)
print(ab)

# to remove all elements
while ab:
    ab.pop()
print(ab)

