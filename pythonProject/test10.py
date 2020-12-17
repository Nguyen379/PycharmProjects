"""
Viết chương trình xuất ra màn hình hình vuông đặc kí tự "*" có cạnh bằng a (với a nhập từ bàn phím). 
Viết chương trình nhập vào ba cạnh của một tam giác, tính và xuất ra diện tích của tam giác đó. 
Viết chương trình tính n!! với n!! = 1.3.5...n nếu n lẻ, n!! = 2.4.6...n nếu n chẵn. 
Viết chương trình giải phương trình bậc 2 với các hệ số nhập từ bàn phím (xét đầy đủ các trường hợp). 
Viết chương trình tính số Fibonashi thứ n. 
Cho mảng một chiều các số thực hãy tìm đoạn [a,b] sao cho đoạn này chứa tất cả các giá trị trong mảng (a,b: số nguyên). (Sử dụng numpy)
"""
# Cau 1:
from math import sqrt

while True:
    try:
        a = int(input("Nhap so nguyen duong:"))
    except:
        print("Integer only")
    else:
        break
for n in range(a):
    print('*' * a)

# Cau 2:
while True:
    try:
        a = float(input("Canh tam giac: "))
        b = float(input("Canh tam giac: "))
        c = float(input("Canh tam giac: "))
        if a + b > c and b + c > a and a + c > b:
            pass
        else:
            print(f'{a}, {b}, {c} khong phai 3 canh tam giac')
            continue
    except:
        print("Numbers only")
    else:
        break
p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print(f'Dien tich tam giac {a}, {b}, {c} = {s}')

# Cau 3:
while True:
    try:
        n = int(input("Nhap so nguyen duong:"))
    except:
        print("Integer only")
    else:
        break
result = 1
if n % 2 == 0:
    for m in range(2, n + 1, 2):
        result *= m
else:
    for m in range(1, n + 1, 2):
        result *= m
print(result)

# Cau 4:
while True:
    try:
        num1 = float(input("a = "))
        num2 = float(input("b = "))
        num3 = float(input("c = "))
    except:
        print("Numbers only")
    else:
        break


def calculate_result(a, b, c):
    if a != 0 and b != 0:
        # pt bac 2
        try:
            delta = (b ** 2) - (4 * a * c)
            if delta > 0:
                x1 = (-b + sqrt(delta)) / (2 * a)
                x2 = (-b - sqrt(delta)) / (2 * a)
                return f'2 nghiem cua phuong trinh la {x1}, {x2}'
            else:
                # delta = 0
                x = (-b) / (2 * a)
                return f'Phuong trinh co nghiem duy nhat la {x}'
        except:
            return "Phuong trinh vo nghiem"
    elif a == 0 and b != 0:
        # pt bac 1
        x = (-c) / b
        return f'Phuong trinh co nghiem duy nhat la {x}'
    else:
        # a va b deu = 0
        if c == 0:
            return "Phuong trinh vo so nghiem"
        else:
            return "Phuong trinh vo nghiem"


result_1 = calculate_result(num1, num2, num3)
print(result_1)


# Cau 5:
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n >= 3:
        return fibonacci(n - 1) + fibonacci(n - 2)


while True:
    try:
        fn = int(input("Nhap so fibonacci thu n: "))
        if fn < 1:
            print("n phai nguyen duong va >=1")
            continue
    except:
        print("Integer only")
    else:
        break
print(fibonacci(fn))

# Cau 6:
import numpy as np

m = np.array([1, 2, 3, 9, 6, -1])
a = np.max(m)
b = np.min(m)
print(f'Ma tran {m} nam trong khoang ({b}, {a}).')

