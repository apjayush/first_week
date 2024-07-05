# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)



# name = input("Enter your name\n")
# lst = name.split(" ")
# print(lst)

# when split is applied on string it becomes an arrayn = int(input("Enter the size of list :"))

lst = list

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

texts = ["apple,banana", "cherry,orange", "grape,lemon"]



# n = int(input("Enter the size of list :"))

# lst = list(map(int, input("Enter the numbers\n").strip().split()))[:n]
# print(lst)


# Insert method
lst = [1,2,3,4]
lst.insert(1,"yaha par")


"""
in insert youh have to first write the index 
as the first argument and at the second argument 
it is the element which you want to insert before the index
"""

# there is one more method called extend() it is also used to add
# element just like append but it can add more than one element at the same time

# Syntax: list.extend(iterable)

lst.extend(["hey", "there", "I", "am", "writing", 2, "you"])

print(lst)



"""Using reversed function"""
my_list = [1,2,3,4,5]
reversed_list = reversed(my_list)
print(reversed_list)




"""remove function removes the first element
error is raise if the element does not exist"""

my_list = [1,2,3,4,5]

my_list.remove(2)
print(my_list)



List = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]
# Removing elements from List
# using iterator method
for i in range(1, 5):
    List.remove(i)
print("\nList after Removing a range of elements: ")


"""pop function is used to remove the last elment from the list
but if you want to remove a specific element the the index of that
element is passed as argument"""

lst = [1,2,3,4]
lst.pop()
lst.pop(2)
print(lst)

lst2 = lst.copy()
print(lst2)



lst = [2,4,6,8,0,1]


# slicing in list

lst = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(lst[2::3])


str = "string slicing"

print(str[-7:])
print(str[-1:-1:-1])
print(str[-11:-4:2])


lst.insert(1,100)
print(lst)


items = [(1, 3), (3, 2), (2, 1)]
items.sort(key= lambda x: x[1])


lst_data = [3,1,5,9,11]
print(sorted(lst_data))


"""sorted does not modify the original list
it just creates a new list but list.sort modifies 
the original list that is the difference"""



# List comprehension

squares = []

for i in range(1,10):
    squares.append(i**2)

print(squares)    


cubes = list(x**3 for x in range(1,10))
print(cubes)

# or

cubes = list(map(lambda x:x**2, range(0,5)))
print(cubes)

print(list(range(0,100)))


# enumerate function

numbers = [11,12,13,14,15]

for index,value in enumerate(numbers):
    print(f"The index is {index} and value is {value}")