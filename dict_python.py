# Python Dictionary Syntax
# dict_var = {key1 : value1, key2 : value2, …..}

# Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable. 

marks = {"Ayush": 50, "Shankar":45, "Sharma":65}

marks["kapp"] = 100   #here i have added a new element

for key,value in marks.items():
    print(f"{key} : {value}")

marks.update({"Ayush": 90})

# Nested dictionary

print(marks)


# in dictionary elements can be accessed by using get and by manually using list[item]

marks = {"Ayush": 50, "Shankar":45, "Sharma":65}

# marks.clear()   #removes all the elements 
# marks.copy()    #returns the copy of a dictionary


print(marks.keys())

marks.pop("Ayush")   #Remove the element with specified key

marks.popitem()  #removes the last inserted key value pair


status = "Shankar" in marks

print(status)

print(marks)