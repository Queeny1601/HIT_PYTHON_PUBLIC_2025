# Tạo mảng a
n = int(input(" Nhập số lượng phần tử của mảng: "))
a = []
for i in range(n):
    num = (input(f" Nhập phần tử thứ {i+1} của mảng: "))
    a.append(num)
# In tuple b
b = tuple(a)
print(b)
# Đếm số phần tử trong b là số
count = 0
count = 0
for item in b:
    if item.isdigit():  # Kiểm tra xem chuỗi toàn số
        count += 1
print("Số phần tử trong b là dạng số:", count)
