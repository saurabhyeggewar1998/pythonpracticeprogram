
list1 =  [10, 20, 30]

list2 = ["One","Three",5]


# to convert lists to dictionary
res = {list1[i]: list2[i] for i in range(len(list1))}

# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))


#Que2 Merge two Python dictionaries into one
dict_1 = {1: 'a', 3: 'b'}
dict_2 = {2: 'c', 4: 'd'}
print(dict_1 | dict_2)

#Que3
a_dict = {'John': 32, 'Mel': 31, 'Nik': 33, 'Katie': 32, 'James': 29, 'Matt': 35}
a_dict.pop('John')
print(a_dict)

#que4
def checkKey(dict, key):
    if key in dict.keys():
        print("Present, ", end=" ")
        print("value =", dict[key])
    else:
        print("Not present")

# Driver Code
dict = {'name': "mike", 'salary':"10000" }

key = 'salary'
checkKey(dict, key)

#que5
ini_dict = {
  "name": "Mike",
  "age":25,
  "salary": 8000,
  "place": "New york"
}

# printing initial json
print("initial 1st dictionary", ini_dict)

# changing keys of dictionary
ini_dict['city'] = ini_dict.pop('place')

# printing final result
print("final dictionary", str(ini_dict))
#Que6
list1 = [5,10,-30,25,45]

# printing the maximum element
print("Largest element is:", max(list1))

#que7
lis1 = []
if lis1!=[]:
    print("The list is not empty")
else:
    print("Empty List")



#Que8

list1=[1, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6,6, 7,7, 8, 9, 0, 4]
print(list(set(list1)))

#Assignment Dict
dict1 = {}
n = int(input("enter a number"))
for i in range(n):
    key = input("enter key")
    value = input("Enter value")
    dict1.update(key=key, value=value)



print(dict1)



