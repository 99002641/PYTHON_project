from donor import *
A = blooddb("aau", "aau", "aau", "aau", "aau")
A.read_data(thelist)
A.write_data(thelist)
print("-----------------------------------------------------------------------------------")
B = input("Enter phone num to search:")
A.search_donor(B)
