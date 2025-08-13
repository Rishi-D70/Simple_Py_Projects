numbers = [5, 12, 7, 18, 3, 6, 20]
even_numbers = []


for num in numbers:
    if num % 2 ==0:
        even_numbers.append(num)


print("Sum of even numbers = ", sum(even_numbers))
