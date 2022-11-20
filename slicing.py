
name = "Chris Gauthier"
number = "1,2,3,4,5,6,7,7,9,10"
letters = 'abcdefghijklemnopqrstrz'
print(name[0:6])

print(name[3:4])

print(name[:9])

print(name[9:])

print(name[-4:-2])

#starts at 0, goes up to but not including 6 steps up by 2s
print(name[0:6:2])

print(number[1::4])

print(letters[0:25:2])
#printing letters backwards
#doesn't cover a because 0 is up to and including 1
print(letters[25:0:-1])
#getting the end of the string
print(letters[25::-1])
