# Chỉ có một phần tử nên Python hiểu nhầm qua kiểu string
my_tuple = ("hello")
print(type(my_tuple))
# Kết quả: <class 'str'>
 
# Bạn thêm dấu phẩy để Python biết đây là 1 tuple
my_tuple = ("hello",)
print(type(my_tuple))
# Kết quả: <class 'tuple'>
 
# Bạn cũng có thể bỏ cặp dấu ngoặc đơn nhưng phải có dấu phẩy
my_tuple = "hello",
print(type(my_tuple))
# Output: <class 'tuple'>