#  Remove all occurences from a list of an element
str1 = input("enter some numbers seperated by spaces: ")
demo = str1.split()
List1 = [int(i) for i in demo]
key = int(input("Enter the repeatetive element: "))
List2 = [i for i in List1 if i != key]
print("original List: ", List1)
print("Processed List: ", List2)