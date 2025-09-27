# Using 'with' automatically closes the file

# Append mode
with open("example.txt", "a") as file:
    file.write("Added with context manager.\n")

# Read mode
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
