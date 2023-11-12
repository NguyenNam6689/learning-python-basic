"""
* Tuple, Dictionary, Set
* Mục tiêu: 
* Tuple là gì? Cách sử dụng
* Dictionary là gì? Cách sử dụng
* Set là gì? Cách sử dụng
"""
# Tuple là gì? Cách sử dụng
## Khai báo
### Cách 1
my_tuple = (1,2,3, 'hello', True)
### Cách 2
my_tuple = tuple([1,2,3, 'hello', True])
## Truy cập phân tử
### Khởi tạo một tuple chưa thông tin về một sinh viên
hoc_sinh=('Trần Thanh Phong', 25, 'Nha Trang', 'Khánh Hòa')
### Truy cập và hiển thị thông tin 
ho_ten=hoc_sinh[0]
tuoi=hoc_sinh[1]
thanh_pho=hoc_sinh[2]
tinh=hoc_sinh[3]

print("Họ và tên: " + ho_ten)
print("Tuổi: " + str(tuoi))
print("Thanh Phố: " + thanh_pho)
print("Tỉnh: " + tinh)

### Sử dụng slicing để trích xuất một phân của tuple
ten_tuoi=hoc_sinh[0:2]
que_quan=hoc_sinh[2:4]

print(ten_tuoi[0] + " " + str(ten_tuoi[1]) + " tuổi")
print("Vị trí hiện tại: Thành phố " + que_quan[0] + ", tỉnh " + que_quan[1])

## Đếm số lần xuât hiện của phần tử
diem_thi=(8,10,9,7,8.5,5,10)
### Đếm điểm số điểm thi là 8
so_diem_thi_8 = diem_thi.count(8)

print('Học sinh: ' + hoc_sinh[0] + ' có ' + str(so_diem_thi_8) + ' điểm thi là 8 điểm')

## Kết hợp 2 tuple lại với nhau
mon_hoc=('Lập trình Python', 'Lập trình ReactJS')

### Kết hợp 2 thông tin học sinh và môn học lại
thong_tin=hoc_sinh+mon_hoc
print(thong_tin)

##Sử dụng unpacking(giải nén) để gán giá trị từ tuple vào biến:
ten, tuoi, thanh_pho, tinh, mon_hoc_1, mon_hoc_2 = thong_tin
print(ten, tuoi, thanh_pho, tinh, mon_hoc_1, mon_hoc_2)