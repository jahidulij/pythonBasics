lucky_numbers = [4, 8, 15, 16, 23, 42, 3, 10]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby", "Toby"]

print(friends)
friends.extend(lucky_numbers)
print(friends)

friends.append("Mike")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

print(friends.index("Toby"))

print(friends.count("Toby"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)
friends.reverse()
print(friends)

friends2 = friends.copy()
print(friends2)

friends.clear()
print(friends)
