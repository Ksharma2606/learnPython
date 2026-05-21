# string data type
#This is a test

# literal assignment
first = "Karan"
last = "Sharma"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))


# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)


statement = "The decade of the 80's was the " + decade
print(statement)


# multiple lines
multiline = """This is a string that spans
multiple lines."""

print(multiline)

# Escaping special characters
sentence = 'I\'m learning Python!\tHey!\n'
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
