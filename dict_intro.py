vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

my_car = vehicles['fiesta']
print(my_car)

commuter = vehicles['virago']
print(commuter)
#commuter = vehicles['Virago'] # it could crash the code but fast
#print(commuter)

learner = vehicles.get("er5")
print(learner)
learner = vehicles.get("ER5") #it will not crash the code but slow
print(learner)
print("-"*40)

#Adding values to dictionaries
vehicles["toy "] = "Glider"

#Deleting values
del vehicles["starfighter"]
# del vehicles["f1"]
result = vehicles.pop("f1", "You wish! Sell the Learjet and you might afford a racing car.")
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()


#Iterating over dictionaries
for key in (vehicles):
    print("{} \t:{}".format(key,vehicles[key]))

print("-"*40)

#Alternative of enumerate for dictionaries
for key,value in vehicles.items():
    print(key,value, sep="\t:")
