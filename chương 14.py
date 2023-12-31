#CHƯƠNG 14

#Bài 1
try:
    a, b, c = map(float, input("Nhap 3 canh cua tam giac: ").split())
    if a <= 0  or b <= 0 or c <= 0:
        raise ValueError
    if a <= 0 or b <= 0 or c <=0 or a + b <= c or b + c <= a or a + c <= b:
        raise ValueError
except  ValueError as e:
    print("Lỗi thử lại !!!")
else:
    print("Ba cạnh đúng là cạnh của tam giác !!!")

#Bài 2
so_truoc = [None, None, None]
while True:
        try:
            x = int(input("Nhập một số nguyên dương (0:kết thúc): "))
            so = int(x)
            if so < 0:
                raise ValueError
            elif so == 0:
                break
            elif so == so_truoc[0] == so_truoc[1] == so_truoc[2]:
                raise ValueError
            else:
                so_truoc = [so, so_truoc[0], so_truoc[1]]
        except ValueError as e:
            print("lỗi ,vui lòng nhập lại")
