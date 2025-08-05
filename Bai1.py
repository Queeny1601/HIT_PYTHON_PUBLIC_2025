# Tuple ban đầu chứa các chuỗi ký tự số
n= int(input(" Nhập số kí tự của tuple: "))
a= []
for i in range(n):
    num=input(f" Nhập kí tự thứ {i+1} của tuple: ")
    a.append(num)
original_tuple = tuple(a)
# Chuyển đổi tuple chứa chuỗi -> tuple chứa số nguyên
converted_tuple = tuple(int(x) for x in original_tuple)

# Tính trung bình cộng
average = sum(converted_tuple) / len(converted_tuple)

# In kết quả
print("Tuple ban đầu:", original_tuple)
print("Tuple sau chuyển đổi:", converted_tuple)
print("Trung bình cộng:", average)