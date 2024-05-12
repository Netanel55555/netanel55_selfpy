NUM_OF_PIGS = 3
num_of_bricks = input("Enter three digits (each digit for one pig):")

digits_sum = sum(map(int, num_of_bricks))

# print the sum
print(digits_sum)

# print the number of brick per pig
print(digits_sum/NUM_OF_PIGS)

reminder = digits_sum % NUM_OF_PIGS
# Print the remaining amount of bricks
print(reminder)

print(reminder == 0)