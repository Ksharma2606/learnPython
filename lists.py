users = ['Karan', 'John', 'Sara']

data = ['Karan', '42', 'True']

emptylist = []

# print("Karan" in emptylist)

# print(users[0])
# print(users[-1])
# print(users[-2])

# print(users.index('Sara'))

# print(users[0:2])
# print(users[1:])
# print(users[-3:-1])

# print(len(data))
# users.append('[Karan, Sara]')
# print(users)
# users.append('Karan')
# print(users)

# users.extend(['Robert','Jimmy'])
# print(users)

# users.extend(data)
# print(users)

# users.insert(0,'Bob')
# print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ['Robert', 'JPJ']
print(users)

users[1:2] = ['Karan']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)



# users.remove('Bob')
# print(users)

# print(users.pop())
# print(users)

# del users[0]
# print(users)

# data.clear()
# print(data)

# users.sort()
# print(users)