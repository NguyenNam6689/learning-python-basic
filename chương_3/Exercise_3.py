# Cho trước hai xâu kí tự s1, s2. 
# Viết đoạn chương trình in ra xâu kí tự bao gồm lần lượt các kí tự được lấy ra từ s1, s2. 
# Nếu một trong hai xâu s1, s2 hết trước thì lấy tiếp từ xâu còn lại.
s1 = input("Nhập xâu kí tự s1: ")
s2 = input("Nhập xâu kí tự s2: ")
result = ""
i = 0
j = 0
while i < len(s1) and j < len(s2):
    result += s1[i]
    result += s2[j]
    i += 1
    j += 1
if i < len(s1):
    result += s1[i:] 
if j < len(s2):
    result += s2[j:]
print("Xâu kết quả là:", result)