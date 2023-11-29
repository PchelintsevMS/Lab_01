def euclid(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = 5
num2 = 3

result = euclid(num1, num2)
print(f"НОД чисел {num1} и {num2}: {result}")
