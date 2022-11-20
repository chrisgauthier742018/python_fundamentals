
for i in range(1,13):
    print("No: {0} squared: {1} and cubed: {2}".format(i,i**2,i**3))

#you can do some column formatting
for i in range(1,20):
    print("No: {0:4}, squared: {1} and cubed: {2}".format(i,i**2,i**3))
#formatting for left align and right align
for i in range(1,20):
    print("No: {0:2} squared: {1:<3} and cubed: {1:^4}".format(i,i**2,i**3))

#printing floating point numbers
print("pi is: {0:12f}".format(22/7))
print("pi is: {0:3.50f}".format(22/7))

print("pi is: {0:<72.54f}".format(22/7))