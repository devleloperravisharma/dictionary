fruits = ["oranges", "bananas", "blueberries"]
#creating a dictionary
sampledict = {
    "name1" : "rashi", 
    "color" : "wine red",
    "programme" : "IB"
}
print(sampledict)

print(fruits[1])

print(sampledict["name1"], sampledict["color"])
#####get the list of keys
print(sampledict.keys())
##### get the list of values
print(sampledict.values())

for meow in sampledict:
    print(meow, sampledict[meow])

##### checking if there is a key in a dictionary
if "city" in sampledict:
    print("True")
else:
    print("False")

##### adding a key and value pair to the dictionary
sampledict["hobby"] = "drawing"
print(sampledict)

##### how to delete a key
del(sampledict["programme"])
print(sampledict)

sampledict["fruits"] = ["appples", "strawberries", "oranges", "kiwis", "pomagrate seeds", "mango", "lychee", "rassberries", "blackberries"]
print(sampledict)

##### creating nested dictionary