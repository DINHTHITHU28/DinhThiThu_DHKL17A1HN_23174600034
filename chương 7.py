#CHƯƠNG 7

#bài 1
x = int(input("Nhập giá trị của x: "))

S = 1 + x + (x ** 3) / 3 + (x ** 5) / 5

print("Giá trị của biểu thức S =", S)

#bài 2
result = 1 + 2
print('result =', result)
original_result = result

result = result - 1
print('result =', result)
original_result = result

result = result * 2
print('result =', result)
original_result = result

result = result ** 3
print('result =', result)
original_result = result

result = result + 8
print('result =', result)
original_result = result

result = result % 7
print('result =', result)
original_result = result

result = result // 2
print('result =', result)
original_result = result

#bài 3
result = 5
print('result = ', result)
result -= 1
print('result = ', result)
result += 3
print('result = ', result)
result = -result
print('result = ', result)
result = True
print('not result = ', not result)

#bài 4
x = 16
y = 4

print((x, y))

equivelence = x == y
print("x = -y is", equivelence)

equivelence = x != y
print("x != y is", equivelence)

equivelence = x > y
print("x > y is", equivelence)

x = 8
y = 9

print((x, y))

equivelence = x >= y
print("x >= y is", equivelence)

equivelence = x < y
print("x < y is", equivelence)

equivelence = x <= y
print("x <= y is", equivelence)

#bài 5
x=15
y=12

print('Binary of x= ', bin(x), ', Binary of y=', bin(y))
print('x&y=', bin(x&y))
print('x/y=', bin(x|y))
print('x^y=', bin(x^y))
print('~x=', bin(~x))
print('x<<2=', bin(x<<2))
print('y>>2=', bin(y>>2))

#bài 6
x = True
y = False

print(x and y)
print(x or y)
print(not x)
print(x is y)
print(x is not y)

#bài 7
def doi_tien(so_tien):
    menh_gia = [500000, 200000, 100000, 50000]
    so_to = []
    
    for menh_gia_i in menh_gia:
        so_to_i = so_tien // menh_gia_i
        so_to.append(so_to_i)
        so_tien %= menh_gia_i
    
    return so_to, so_tien

so_tien_muon_doi = int(input("Số tiền muốn đổi: "))
so_to, so_tien_con_lai = doi_tien(so_tien_muon_doi)

print("Số tờ 500,000:", so_to[0])
print("Số tờ 200,000:", so_to[1])
print("Số tờ 100,000:", so_to[2])
print("Số tờ 50,000:", so_to[3])
print("Tiền còn lại:", so_tien_con_lai)