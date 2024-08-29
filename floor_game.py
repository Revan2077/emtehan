def calculate_floor(string):
    if len(string) > 4:  # check input range
        print("up tp 4 floors are allowed")
        exit()
        
    
    floor = 0  # calculate final floor
    for i in string:
        if i == 'U':
            floor += 1
        elif i == 'D':
            floor -= 1
        else :
            print("invalid input") 
            exit()
    return floor
    

# Example usage
floorInput = input("Enter the commands : ")
call_result = calculate_floor(floorInput)
print(call_result)