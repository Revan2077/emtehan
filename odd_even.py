def separator(ls): # create function
    evens = []
    odds = []
    for num in ls:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
# sort them and make them tuple            
    evens.sort()  
    odds.sort()
    return tuple(evens), tuple(odds)

# input 
numbers = list(map(int, input("Enter your numbers with space between : ").split()))

# calling function
evens, odds = separator(numbers)

#results
print("Evens:", evens)
print("Odds:", odds)