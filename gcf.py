# 1. Get first number
# 2. Get second number

# gcf = 1
# loop thru 1 thru first/second number
# and see if they are divisible by the number in the loop(index)
# if they are divisbile assign gcf to it
# exit loop
# print gcf


num_one = int(input("Enter your first number:"))
num_two = int(input("Enter your second number"))

#34, 17
#num_one = 34
#num_two = 17

gcf = 1
for x in range(1,num_one+1,1):
    if(num_one % x == 0 and num_two % x == 0):
        gcf = x

print("All done!!")
print("GCF is:", gcf)




