#booleans
a = 200
b = 33

if b>a:
    print ("b is greater than a")
else:
    print ("b is not greater than a")

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

def myfun():
    return True
if myfun ():
    print ("YES")
else:
    print ("NO")

#operators
print (10+5)
print (10-2)
print(3*2)
print(6/2)
print (7%2)  #остаток
print(2**5)
print(7//2)  #целое число при делении

#list
thislist = ["appele", "banana", "cherry"]
print(thislist)

list1 = ["abc", 34, True, 40, "male"]
print(list1)

thislist = ["appele", "banana", "cherry"]
print(len(thislist)) #количество пунктов в листе

thislist = ["appele", "banana", "cherry"]
print(type(thislist))

thislist = list(("apple", "banana", "cherry")) #другой вид записи 
print(thislist)

#access items
thislist = ["appele", "banana", "cherry"]
print(thislist[1])         #first index is 0       

thislist = ["appele", "banana", "cherry"]
print (thislist[-1])        

mylist = ["appele", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print (mylist[2:5])          #5 is not include and 2 is include

mylist = ["appele", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[2:])

thislist = ["appele", "banana", "cherry"]
if "appele" in thislist:
    print ("Yes, 'appele' is in list ")

#change item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
mylist[1:3] = ["blackcurrant", "watermelon"]
print(mylist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print (thislist)

#add list items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")     #.append() add item to the end of list
print (thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")      #.insert() add item to the specified index
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)   #extend() add additional list to the list 
print(thislist)

#remove list items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)        #pop(index) is same with remove()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]  #same with remove
print (thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()      #delate all elements
print(thislist)

#loop list
thislist = ["apple", "banana", "cherry"]
for x in thislist:          #print items one by one
    print(x)

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

thislist = ["apple", "banana", "cherry"]
[print (x) for x in thislist]

#list comperehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print (newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


newlist = [x for x in range(10)]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


#sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print (thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#TUPLES
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")  #нет запятой
print(type(thistuple))

'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

#access tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#update tuples
x = ("apple", "banana", "cherry")
y= list(x)
y[1] = "kiwi"
x = tuple[y]
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#loop 
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#join 
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

#SET
#Set items are unchangeable, but you can remove items and add new items.
#The values True and 1 are considered the same value in sets, and are treated as duplicates:
#The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

myset = {"apple", "banana", "cherry"}
print(type(myset))

#access
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print (x)

thisset = {"appele", "banana", "cherry"}
print ("banana" in thisset)

thisset = {"appele", "banana", "cherry"}
print ("banana" not in thisset)

#add
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papay"}
thisset.update(tropical)
print (thisset)

#remove
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")  # If the item to remove does not exist, discard() will NOT raise an error.
print(thisset)

#loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#join 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

#dictionaries
'''
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable
Do not allow duplicates.
'''

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(thisdict)

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(len(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#access
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x=thisdict["model"]
print(x)


thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x = thisdict.get("model")
print(x)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)


#change 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)


#add
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


#remove
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


#loop
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.items():
  print(x)


#copy
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


#nested
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)


#IF ELSE
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#WHILE LOOP
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#FOR LOOP
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


