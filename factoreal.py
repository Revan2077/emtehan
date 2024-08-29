def factoreal(x):  # function and if statment to make factoreal of number
    if x == 0 or x == 1:
        return 1
    else:
        return x * factoreal(x - 1)

# input
num_input = int(input("Enter your number: "))

# get the factoeal of the number
fact_res = factoreal(num_input)

print(fact_res) # Print result
