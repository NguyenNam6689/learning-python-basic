# Các phần tử Tuple có thể có các kiểu dữ liệu khác nhau
my_tuple = ("freetuts", [8, 4, 6], (1, 2, 3))
print(my_tuple)
# Kết quả: ("freetuts", [8, 4, 6], (1, 2, 3))
 
# tuple có thể được tạo bằng cách bỏ đi cặp ngoặc đơn
my_tuple = 3, 4.6, "blog"
print(my_tuple)
# Kết quả: 3, 4.6, "blog"
 
# Bạn có thể tách các phần tử tuple thành nhiều biến nhỏ
a, b, c = my_tuple
print(a)
print(b)
print(c)
# Kết quả:
# 3
# 4.6
# blog