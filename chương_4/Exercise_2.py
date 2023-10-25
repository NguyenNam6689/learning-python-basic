# Nhập dữ liệu là danh sách 5 số float input vào từ người dùng
#khai báo 1 mảng rỗng
numbers = []

#chạy vòng lặp 5 lần
for i in range(0, 5):
  	#xuất nhập giá trị tại index i
    print("nhập số", i, ":")
    # Chuyển sang kiểu float
    item = float(input())
    # thêm số này vào mảng
    numbers.append(item)

print("danh sách số:", numbers)