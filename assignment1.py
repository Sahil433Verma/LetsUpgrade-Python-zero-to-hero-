x = input("Enter few numbers: ")
str1 = x.split()
List1 = [int(i) for i in str1]
List1.sort()
List1.reverse()
print(List1)