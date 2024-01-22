def generate_bracelet(num1, num2):
    bracelet = [num1, num2]

    while True:
        next_num = (bracelet[-1] + bracelet[-2]) % 10
        bracelet.append(next_num)
        
        # Check for repetition
        if bracelet[-2:] == [num1, num2]:
            break

    return bracelet

# Get user input for num1
num1 = int(input("Enter the first number (less than 10): "))
while num1 >= 10:
    num1 = int(input("The number must be an integer less than 10, enter a valid number: "))

# Get user input for num2
num2 = int(input("Enter the second number (less than 10): "))
while num2 >= 10:
    num2 = int(input("The number must be an integer less than 10, enter a valid number: "))

result_bracelet = generate_bracelet(num1, num2)
length=  len(result_bracelet)-2
# Print the bracelet and its length
print("Number Bracelet:", result_bracelet)
print("Length of Bracelet:", length)
