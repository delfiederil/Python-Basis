# Writing to a file
file = open("example.txt", "w")  # "w" = write mode
file.write("Hello, Python!\n")
file.close()

# Reading from a file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Appending to a file
file = open("example.txt", "a")
file.write("This line is appended.\n")
file.close()
