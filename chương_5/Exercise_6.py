my_tuple = (4, 2, 3, [6, 5])
 
# Thay đổi giá trị cho phần tử thứ nhất của phần tử thứ 4 trong my_tuple.
my_tuple[3][0] = 9
print(my_tuple)
 
# Chương trình này sẽ bị lỗi
my_tuple = ('p','r','o','g','r','a','m','i','z')
 
# Bỏ dòng này sẽ không có lỗi như hình
# Bạn hãy thử mở lại dòng này sẽ thấy bị lỗi do ta cố tình thay đổi ..
# giá trị cho phần tử tuple
# my_tuple[1] = 'a'
 
print(my_tuple)