#To declare a set
numbers = set()

print(numbers,type(numbers))
numbers.add(1)
print(numbers)


'''while len(numbers)< 5:
    next_number= int(input("Please enter next number :"))
    numbers.add(next_number)

print(numbers)
'''
#To remove duplicaate from the list make it  a set.

data = ["blue","Green","Red","Green","Red","blue"]
new_data = set(data)
print(data)
print(new_data)

#To remove duplicates from list but to keep order same use dict.fromkeys()
data_new = list(dict.fromkeys(data))
print(data_new)
print()
print(dict.fromkeys(data))
