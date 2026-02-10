# Create sets of squares and cubes
squares = set([x**2 for x in range(1, 10)])
cubes = set([x**3 for x in range(1, 10)])

print("squares:", squares)
print("cubes:", cubes)

# Add cubes to squares (union in place)
squares.update(cubes)
print("updated:", squares)

# Add 1331 (11^3) to the set
squares.add(11*11*11)
print("add:", squares)

# Remove 1331 from the set
squares.remove(1331)
print("remove:", squares)

# Pop an arbitrary element from the set
popped_value = squares.pop()
print("popped value:", popped_value)
print("after pop:", squares)

# Clear the set
squares.clear()
print("clear:", squares)
