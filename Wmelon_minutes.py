def waterMmelon(h, k):
    
    total_minutes = 2 * h + k # Calculate minutes
    
    # check if their lives will last equal
    if total_minutes % 2 == 0:
        print("Yes")
    else:
        print("No")

# inputs
h = int(input("Enter number of watermelons: "))
k = int(input("Enter number of melons: "))

waterMmelon(h, k) # call funtion
