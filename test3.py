'''name = input("enter the string: ")
sub = input("enter the string that you want to count: ")
n = name.count(sub)
print(n)'''
string = input("enter the string: ")
substring = input("enter the string you want search: ")
count = 0
for i in range(len(string)):
    if string[i:i+len(substring)] == substring:
        count += 1
print(count) 