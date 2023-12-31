def ham_tinh_diem_TB(hk1,hk2):
    dtb = float(hk1+hk2*2)/3
    print("Điểm trung bình năm là: %0.2f" % dtb)
    return
hk1 = float(input("Nhập điểm trung bình học kì 1: "))
hk2 = float(input("Nhập điểm trung bình học kì 2: "))
ham_tinh_diem_TB(hk1,hk2)

import math 
def tinh_bmi(can_nang,chieu_cao):
    BMI = can_nang/math.pow(chieu_cao,2)
    return BMI

w = float(input("Nhập cân nặng: "))
h = float(input("Nhập chiều cao: "))
tinh_bmi(w,h)
print("Chỉ số BMI của bạn là: %0.2f" % (tinh_bmi(w,h)))