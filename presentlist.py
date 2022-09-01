my_list = ["apple", "banana", "cherry"]
if "apple" in my_list:
  print("Yes, 'apple' is in the fruits list")

  #3b question change name
my_list = ["apple", "banana", "cherry"]
my_list[1] = "mango"

print(my_list)

  #3c
myList = ['apple', 'banana', 'cherry', 'orange']
myList.insert(2, 'mango')
print(myList)

#4 create a tuple with only one item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#tuple allow  duplicate values explain with examples

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#5) a)create dictionary and get value of first key?
my_new_dict ={'George':192,'Micheal':269,'James':159,'Potter':432}

new_k = list(my_new_dict.keys())[0]
print("Get first key from dictionary:",new_k)

#5b)ANS=Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#6a) Create set and delete the last element from set
# create a set and last remove
mySet = {"Ram", "Shyam","Bilal",  "Feroz"}

# Remove single element from a Set using remove()
mySet.remove("Feroz")

# Print result
print(mySet)


#common elements from in both the sets?

def common_member(a, b):
  a_set = set(a)
  b_set = set(b)

  if (a_set & b_set):
    print(a_set & b_set)
  else:
    print("No common elements")


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
common_member(A, B)