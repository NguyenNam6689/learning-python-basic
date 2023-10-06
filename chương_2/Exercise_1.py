# Viết một chương trình yêu cầu người dùng nhập chiều dài và chiều rộng của hình chữ nhật và sau đó vẽ nó bằng các dấu sao (*).
# Nhập chiều dài và chiều rộng từ người dùng
length = int(input("Nhập chiều dài của hình chữ nhật: "))
width = int(input("Nhập chiều rộng của hình chữ nhật: "))

# Vẽ hình chữ nhật
for i in range(length):
    for j in range(width):
        print("*", end="")
    print()