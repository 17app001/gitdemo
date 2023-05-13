import random

# 1.號碼不能重複
# 2.要排序

numbers = []
for i in range(6):
    x = random.randint(1, 49)
    if x not in numbers:
        numbers.append(x)
        print(numbers, end=" ")
    else:
        print(x)

y = random.randint(1, 49)
print(f"特別號:{y}")
