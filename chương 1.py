import time
# Không cần dấu ";" 
name = "Nam"
age = 25
print("Xin chào ",name)
print("Bạn năm nay ",age," tuổi")
# vòng lặp
for i in range(10):
    print("Số thứ ",i)
# sử dụng thư viện
for i in range(5, 0, -1):
    print(i)
print("Chúc mừng")
# khai báo biến
x = 10
y = "hello"
# đặt tên phân biệt chữ hoa, chữ thường
variable = 20
Variable = 20
print(variable) 
print(Variable)
# kiểu dữ liệu của biên
# int
age = 23
number_of_student = 10

# str
name = "Phong"
message = "Hello Word!"

# float
pi = 3.1415
height = 1.5

# bool
is_male = True
is_female = False

# list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fruits = ["apple","orange","banana"]

# dictionary
student = {
    "name": "Phong",
    "age": 23,
    "number_of_student": 10,
    "message": "Hello Word!"
}

# set
primes = {2,3,5,7,11}

# tuple
point = (10,20)

# None
result = None

# gán giá trị mới
a = 3
print(a) # 3
a = 1
print(a) # 1

# gán nhiều biến cùng 1 giá trị
a, b, c = 5
print(a) # 5
print(b) # 5
print(c) # 5

# gán nhiều biến với nhiều giá trị
a, b, c, d = 5, 6, 7, 8
print(a) # 5
print(b) # 6
print(c) # 7
print(d) # 8

# biến toàn cục (Biến được khai báo bên ngoài một hàm được coi là biến toàn cục và có thể sử dụng trong toàn bộ chương trình.)
global_var = 10

# biến cục bộ (Biến được khai báo trong một hàm chỉ có thể sử dụng bên trong hàm đó và được coi là biến cục bộ)
def my_function():
    local_var = 20
    print(local_var) # chỉ có thể truy cập trong hàm
    print(global_var) # có thể truy cập biến toàn cục
my_function()

# huỷ biến 
x = 10
print(x) 
del x
print(x) # NameError: name 'x' is defined
