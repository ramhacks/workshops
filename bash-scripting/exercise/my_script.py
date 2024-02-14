#!/usr/bin/env python3

def sort_numbers(numbers):
  return sorted(numbers)

if __name__ == "__main__":
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_numbers = sort_numbers(numbers)
    print(sorted_numbers)