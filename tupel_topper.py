toppers = (
    ("arav", "Bsc", 92.00),
    ("chaitanya", "BCA", 99.00),
    ("dhruvika", "B tech", 97)
)

# Print original toppers
for t in toppers:
    print(t)

choice = input("Do you want to edit the details (y/n): ")

if choice.lower() == "y":
    name = input("Enter the name of the student whose details are to be edited: ")
    new_name = input("Enter the correct name: ")
    new_course = input("Enter the correct course: ")
    new_aggr = float(input("Enter the correct aggregate: "))

    i = 0
    new_topper = ()
    while i < len(toppers):
        if toppers[i][0] == name:
            new_topper += ((new_name, new_course, new_aggr),)  # tuple inside tuple
        else:
            new_topper += (toppers[i],)  # keep original
        i += 1

    # Print updated list
    for t in new_topper:
        print(t)
else:
    print("No changes made.")
                   