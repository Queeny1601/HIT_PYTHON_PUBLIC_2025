#1. Nhập vào một list có N phần tử là số nguyên (N nhập từ bàn phím).
n = int(input("Nhập vào số lượng phần tử N:  "))
list = []
for i in range(n):
    num = int(input(f"Nhập vào phần tử thứ {i+1}: "))
    list.append(num)
print(list)

#2. Nhập một số X từ bàn phím, kiểm tra số lần X xuất hiện trong list.
X = int(input("Nhập X: "))
count_X = list.count(X)
print(f"Số {X} xuất hiện {count_X} lần")

#3. Thay thế phần tử từ vị trí 2 -> 7 trong list thành `[8, 5, 4, 0, 1, 3]`.
list[2:8] = [8,5,4,0,1,3]
print("List sau khi thay thế từ 2-7:", list)

#4. Tìm số lớn nhất và nhỏ nhất trong list.
Max_value = max(list)
Min_value = min(list)
print(f"Số lớn nhất:", Max_value)
print(f"Số nhỏ nhất:", Min_value)

#5. Nhập một số Y tùy chọn từ bàn phím. Chèn số Y vào đầu list.
Y = int(input("Nhập vào số Y: "))
list.insert(0,Y)
print("List sau khi chèn Y vào đầu:", list)

#6. Sau khi chèn số Y, kiểm tra các số trong list có sắp xếp theo thứ tự tăng dần hay giảm dần không. Nếu sắp xếp theo tăng dần thì in ra màn hình “TĂNG”, còn nếu sắp xếp theo thứ tự giảm dần thì in ra màn hình “GIẢM”, nếu không tăng không giảm thì in “NO”.
if list == sorted(list):
    print("Tăng")
elif list == sorted(list, reverse= True):
    print("Giảm")
else:
    print("NO")
