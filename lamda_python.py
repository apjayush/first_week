strl = "GeeksforGeeks"

# def upper(string):
#     return string.upper()


upper = lambda string: string.upper()

print(upper(strl))

is_even_list = [lambda arg=x: arg*10 for x in range(1,5)]

for item in is_even_list:
      print(item())