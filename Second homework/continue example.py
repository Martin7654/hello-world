for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")

    else: #else does the same thing as continue here?
        print(f"Found an odd number {num}") 

for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue #continue to the next iteration if the number is even
    print(f"Found an odd number {num}")