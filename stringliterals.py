string1 = "hello "
string2 = "world "
string3 = "how are you "
string4 = "today? "

print(string1 + string2 + string3 + string4)
print ("hello " "world " "how are you " "today")

#you can also do this
print("hello " * 5)
print("hello " * (5 + 4))
print("hello" * 5 + "4")

print("day" in string4 )
print("now" in string4)
print("now" in "test")

age = 24

print("My age is {0} years".format(age))


print("My age is {0} days in {1}".format(age,"12"))