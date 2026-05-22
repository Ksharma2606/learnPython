users = ['Karan', 'John', 'Sara']

data = ['Karan', '42', 'True']

emptylist = []

print("Karan" in emptylist)

print(users[0])
print(users[-1])
print(users[-2])

print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))
users.append('[Karan, Sara]')
print(users)
users.append('Karan')
print(users)

users.extend(['Robert','Jimmy'])
print(users)

users.extend(data)
print(users)