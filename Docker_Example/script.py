#!/usr/bin/env python

def generate_multiplication_table(start, end):
    print(f"Multiplication Table for numbers {start} to {end}:\n")

    for i in range(start, end + 1):
        print(f"\nMultiplication table for {i}:\n")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")

if __name__ == "__main__":
    # Prompt the user for the range of numbers
    start_number = int(input("Enter the start number: "))
    end_number = int(input("Enter the end number: "))

    # Validate the input
    if start_number > end_number:
        print("Invalid range. The start number should be less than or equal to the end number.")
    else:
        # Generate and print the multiplication table
        generate_multiplication_table(start_number, end_number)