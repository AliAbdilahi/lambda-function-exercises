nameheight = [('Ali', 5), ('Mo', 6), ('Alex', 7), ('Pop', 4)]
print("list of tuples:")
print(nameheight)
nameheight.sort(key = lambda i: i[1])
print("Sorted list of tuples:")
print(nameheight)
