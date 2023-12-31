#CHƯƠNG 12

#BÀI 12.1
#bài 1
from ham_chuong_8 import *
lon_nho = [1,0,9,58,10,98,7,56,6]
print("max là:",max(lon_nho))
print("min là:",min(lon_nho))

#Bài 2
from ham_chuong_8 import abss
x = int(input("nhập giá trị của x:"))
abss(x)

#Bài 3
from ham_chuong_8 import giai_pt_bac_nhat
a=eval(input("Nhap he so a :"))
b=eval(input("Nhap he so b :"))
giai_pt_bac_nhat(a,b)

#bài 4
from ham_chuong_8 import dien_tich_tam_giac
a=eval(input("nhap do dai canh a: "))
b=eval(input("nhap do dai canh b: "))
c=eval(input("nhap do dai canh c: "))
dien_tich_tam_giac(a,b,c)

#bài 5
from ham_chuong_8 import kt_nam_nhuan
nam = eval(input("Nhap year: "))
kt_nam_nhuan(nam)

#bài 6
from ham_chuong_8 import tinh_phi_taxi
loai_xe=int(input("Loai xe 4 or 7 ? "))
so_km=eval(input("Nhap so km = "))
time_cho=eval(input("Nhap time phai cho = "))
tinh_phi_taxi(time_cho,loai_xe,so_km)

#bài 7
from ham_chuong_8 import tinh_tien_dien
so_dien=eval(input("Nhap so kwh tieu thu:"))
tinh_tien_dien(so_dien)

#bài 8
from ham_chuong_8 import tinh_gia_phong
print("Cac loai ma phong:")
print("1-Standard")
print("2-Superior Garden View")
print("3-Superior Ocean View")
print("4-Garden View Bungalow")
print("5-Pool View Bungalow")
print("6-Family Room")
print("7-Beach Front Bungalow")
print("8-VIP sea View")
a=eval(input("Nhap loai ma phong:"))
b=eval(input("Nhap so dem:"))
tinh_gia_phong(a,b)

#bài 9
from ham_chuong_8 import dem_nguoc
n=eval(input("Input number:"))
dem_nguoc(n)

#bài 10
from ham_chuong_8 import tinh_S
n=eval(input("Nhap n: "))
x=eval(input("Nhap x: "))
tinh_S(x,n)

#bài 11
from ham_chuong_8 import tinh_S
n=eval(input("Nhap n: "))
x=eval(input("Nhap x: "))
tinh_S(x,n)

#bài 12
from ham_chuong_8 import kiem_tra_so_nguyen_to
n=eval(input("Nhap n: "))
kiem_tra_so_nguyen_to(n)

#bài 13
# A = tổng các số lẻ nhỏ hơn hoặc bằng n
# B = tổng các số chẵn nhỏ hơn hay bằng n
# C = tích các số từ 1 đến n
# D = tích các số chia hết cho 3
# E = tổng các số nguyên tố nhỏ hơn hay bằng n
# F = tổng chuỗi đan dấu
from ham_chuong_8 import *
n = int(input("Nhập vào số nguyên dương n: "))
A(n)
B(n)
C(n)
D(n)
E(n)
F(n)

#bài 14
from ham_chuong_8 import tinh_tong
n=int(input("Nhap so nguyen n : "))
tinh_tong(n)

#bài 15
from ham_chuong_8 import tinh_tong_so_nguyen
tinh_tong_so_nguyen()

#bài 16
from ham_chuong_8 import tim_ucln
a=int(input("Nhap so nguyen a:"))
b=int(input("Nhap so nguyen b:"))
tim_ucln(a,b)

#bài 17
from ham_chuong_8 import tim_bcnn
a=int(input("Nhap so nguyen a:"))
b=int(input("Nhap so nguyen b:"))
tim_bcnn(a,b)

#bài 18
from ham_chuong_8 import so_hoan_hao
x=eval(input("Nhap gia tri x :"))
so_hoan_hao(x)

#bài 19
from ham_chuong_8 import tao_day_so_moi
n=eval(input("Nhap vao mot day so la :"))
tao_day_so_moi(n)

#bài 20
from ham_chuong_8 import tinh_e_mu_x
n=eval(input("Nhap n la:"))
x=eval(input("Nhap x la:"))
tinh_e_mu_x(n,x)

