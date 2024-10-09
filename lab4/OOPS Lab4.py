#1
number = int(input("Enter a number: "))
num_str = str(number)
total = 0
for i in range(len(num_str)):
    total += int(num_str[i]) ** (i + 1)
print(f"{number} is a Disarium Number: {total == number}")

#2
number = int(input("Enter a number: "))
digit_sum = 0
for digit in str(number):
    digit_sum += int(digit)
print(f"{number} is a Harshad Number: {number % digit_sum == 0}")

#3
print("Armstrong Numbers from 1 to 1000:")
for n in range(1, 1001):
    power = len(str(n))
    total = 0
    for digit in str(n):
        total += int(digit) ** power
    if total == n:
        print(n)


#4
x = float(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))
result = 1
for _ in range(n):
    result *= x
print(f"{x}^{n} = {result}")


#5
n = int(input("Enter n: "))
r = int(input("Enter r: "))

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

nCr = factorial(n) // (factorial(r) * factorial(n - r))
print(f"{n}C{r} = {nCr}")


#6
terms = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for _ in range(terms):
    print(a, end=' ')
    a, b = b, a + b
print()


#7
number = int(input("Enter a number: "))
digit_sum = 0
for digit in str(number):
    digit_sum += int(digit)
print("Sum of digits:", digit_sum)


#8
number = int(input("Enter a number: "))
reversed_num = 0
while number > 0:
    reversed_num = reversed_num * 10 + number % 10
    number //= 10
print("Reversed number:", reversed_num)


#9
number = int(input("Enter a number: "))
total = 0
for i in range(1, number):
    if number % i == 0:
        total += i
print(f"{number} is a Perfect Number: {total == number}")


#10
number = int(input("Enter a number: "))
num_str = str(number)
is_palindrome = True
for i in range(len(num_str) // 2):
    if num_str[i] != num_str[-(i + 1)]:
        is_palindrome = False
        break
print(f"{number} is a Palindrome: {is_palindrome}")


#11
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


#12
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=' ')
    print()


#13
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(chr(64 + i), end=' ')
    print()


#14
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()


#15
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


#16
n = 5
for i in range(1, 2 * n, 2):
    for j in range(i):
        print('*', end=' ')
    print()


#17
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i + j, end=' ')
    for j in range(i - 1, 0, -1):
        print(i + j - 1, end=' ')
    print()


#18
n = 5
for i in range(n, 0, -1):
    for j in range(2 * i - 1):
        print('*', end=' ')
    print()


#19
n = 5
for i in range(n):
    row = [1]
    for j in range(1, i):
        row.append(row[j - 1] * (i - j) // j)
    row.append(1)
    print(' '.join(map(str, row)))


#20
n = 4
count = 1
for i in range(1, n + 1):
    for j in range(count, count + i):
        print(j, end=' ')
    count += i
    print()


#21
n = 4
for i in range(n):
    row = []
    for j in range(i + 1):
        if j % 2 == 0:
            row.append('A')
        else:
            row.append('B')
    print(' '.join(row))


#22
n = 4
for i in range(n):
    row = []
    for j in range(i + 1):
        row.append(str((i + j) % 2))
    print(' '.join(row))
