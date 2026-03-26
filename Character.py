string=input("Enter a string: ")

chr=input("Enter a letter to search: ")

i=0
count=0

while(i<len(string)):
    if string[i]==chr:
        count += 1
    i += 1

print("Total number of times ",chr," has occured= ",count)