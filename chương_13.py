#CHƯƠNG 13

#Bài 13.1
from xu_ly_tap_tin import *
bai_13_1()

#Bài 13.2
from xu_ly_tap_tin import *
ten = 'HumptyDumpty.txt'
bai_13_2(ten)

#Bài 13.3
from xu_ly_tap_tin import *
ten = input("Nhập tên tập tin txt là:")
noi_dung = input("Nhập nội dung:")
print("Đã ghi nội dung vào tập tin",ten)
bai_13_3(ten)
ghi(ten,noi_dung)

#Bài 13.4
from xu_ly_tap_tin import *
mo_file_csv()

#Bài 13.5
from xu_ly_tap_tin import *
ten_tap_tin = input("Nhập tên tập tin csv:")
noi_dung = input("Nhập nội dung:")
ghi_noi_dung_vao_tap_tin(ten_tap_tin,noi_dung)
doc_csv_file(ten_tap_tin)