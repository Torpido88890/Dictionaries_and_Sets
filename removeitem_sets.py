small_ints = set(range(20))
print(small_ints)

small_ints.clear()
print(small_ints)

small_ints = set(range(20))
print(small_ints)
small_ints.discard(1) #when you are not sure that something is in the set and remove if it is in the set
small_ints.remove(2)  #when you are sure that the thing is in the set and you want to remove it
print(small_ints)
