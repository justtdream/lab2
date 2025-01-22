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