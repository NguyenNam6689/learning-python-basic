# Hàm tính tổng a và b
def tinh_tong(a, b):
    tong = a + b
    return tong

# Sử dụng hàm
x=5
y=10
result = tinh_tong(x, y)
print("Tổng của ", x, " và ", y, " là ", result)

# Xử lý chuỗi
# Trích xuất ký tự của chuỗi
str="""dòng 1
dòng 2
dòng 3"""
print(str)
print("In ra ký tự đầu tiên của chuổi: " + str[0])

# Nối chuỗi
str1="Hello"
str2="World"
str=str1+" "+str2
print(str)

# Trích xuất chuỗi con
chuoi="Hello world"
print(chuoi[0:5]) #Output: Hello
print(chuoi[6:]) #Output: world

# Lấy độ dài chuỗi
print(len(chuoi)) #Output: 11

# Tìm và thay thế nội dung
chuoi_moi=chuoi.replace("Hello", "TTP")
print(chuoi_moi) #Output: TTP world

# Tìm và xử lý chuổi con
chuoi_cha="Hello world"
chuoi_con="world"
vi_tri=chuoi_cha.find(chuoi_con) # Tìm vị trí chuỗi con trong chuỗi cha. Hàm trả về kết quả là vị trí chuỗi con, nếu không tìm thấy trả về giá trị -1
if vi_tri !=-1:
    print(f"Chuỗi con '{chuoi_con}' được tìm thấy tại vị trí '{vi_tri}'")
else:
    print("Không tìm thấy chuỗi con trong chuỗi cha")
    
# Tách chuỗi
chuoi="apple,banana,orange"
danh_sach=chuoi.split(",") # Tách chuỗi thành danh sách các phần tử dựa trên ký tự phân tách ","
print(danh_sach)

# Trim kí tự khoảng trắng
chuoi="            Hello, world!         "
chuoi_da_trim=chuoi.strip() # Xóa khoảng trắng ở đầu và cuối chuỗi
print(chuoi_da_trim)
chuoi_da_trim=chuoi.lstrip() # Xóa khoảng trắng ở đầu chuỗi
print(chuoi_da_trim)
chuoi_da_trim=chuoi.rstrip() # Xóa khoảng trắng ở cuối chuỗi
print(chuoi_da_trim)

# Kiểm tra chuỗi có phải là chuỗi số không
chuoi1="12345"
chuoi2="3.14"
chuoi3="1/2"
chuoi4="Hello123"

print(chuoi1.isnumeric()) # Output: true (Chỉ chứa kí tự số)
print(chuoi2.isnumeric()) # Output: false (Chứa dấu chấm không phải số)
print(chuoi3.isnumeric()) # Output: false (Chứa kí tự đặt biệt, cũng coi là số)
print(chuoi4.isnumeric()) # Output: false (Chứa kí tự không phải số)

# Chuyển đổi thành chữ thường
chuoi="HELLO WORLD"
chuoi_thuong=chuoi.lower() # Chuyển đổi tất cả các ký tự trong chuỗi thành chữ thường
print(chuoi_thuong)

# Chuyển chuỗi thành chữ hoa
chuoi="hello world"
chuoi_hoa=chuoi.upper() # Chuyển đổi tất cả các ký tự trong chuỗi thành chữ hoa
print(chuoi_hoa)