#Project 3
#Create	a multiplicative for a specific number.	
#(Create a multiplication table	for one	number at a time)
#Go up to 12 (1x1; 1x2;	1x3; 1x4; etc...)
#Using for loop to iterate multiplication 10 times
#Will need user	input to populate the variables


print("------------------------------------------------------------")

num = int(input("Show the multiplication table for which number?: "))
print("\n")
for a in range(1,11):
    print(num,"x", a, "=",num*a)
    
