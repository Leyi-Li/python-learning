
friends = ["Leyla", "Ian", "John", "Colin", "Jack", "Dan"]

print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[0:3])

friends[4] = "Mike"
print(friends)

# lists functions
lucky_numbers = [23, 32, 6, 13, 8, 49, 52]

friends.extend(lucky_numbers)
print(friends)
# add to the end of the list
friends.append("Anna")
print(friends)
# insert to a certain position
friends.insert(1, "BB")
print(friends)
# remove element
friends.remove("BB")
print(friends)

# remove all the elements
friends.clear()
print(friends)
friends = ["Leyla", "Ian", "John", "Colin", "Jack", "Dan"]


# remove the last element
friends.pop()
print(friends)

# check if something is in the list
print(friends.index("Leyla"))
# print(friends.index("Tom"))