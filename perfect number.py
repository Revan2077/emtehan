def perfectNumber(num) :
    x = 0
    
    for i in range(1, num):
        if num % i == 0:
            x += i
    
    if x == num:
        return "YES"
    else:
        return "NO"

num = int(input("Enter your number: ")) # Input

# call and print
PN = perfectNumber(num)
print(PN)
