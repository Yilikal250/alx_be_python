number = int(input("Enter the size of the pattern: "))
start = 0
while start < number:
    start2 = 0
    while start2 < number:
        print("*", end=" ")
        start2 += 1  # Increment start2 to prevent infinite loop
    print()  # Move to the next line after finishing the row
    start += 1  # Correctly increment start