print("HASHMAP")

data = {}
data["Charles"] = "Ferrai"
data["Max"] = "RedBull"
data["Lando"] = "Mclaren"

print("we can also add the values like pairs")

team = {"Ferrai": "Fred", "Mercedes": "Toto"}

print(data)
print(team)

print()

print("DICTIONARY COMPREHEnsion")
sample = {i: i**2 for i in range(1,5,1)}
print(sample)

print()

print("Iterating through a Hashmap")
print()

for key in data:
    print(key, data[key])
    
print()

for val in data.values():
    print(val)
    
print()

for key, value in data.items():
    print("Key: ", key, "Values: ", value)
    
print()

print(data.get("Seb"))
print(data.get("Seb", "Default Team"))