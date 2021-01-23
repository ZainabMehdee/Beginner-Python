# Get a number
num = int(input("Enter a number: "))

# Check if positive
if num > 0:
    print("Positive")
# Check if negative
elif num < 0:
    print("Negative")

# If not positive or negative, it has to be zero.
else:
    print("Zero")

# Check if even
if num % 2 == 0:
    print("Even")
# If not even its has to be odd
else:
    print("Odd")