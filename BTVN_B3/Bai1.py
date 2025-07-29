##1
n = int(input("Nhập vào số lượng phần tử N:  "))
list = []
for i in range(n):
    num = int(input(f"Nhập vào phần tử thứ {i+1}: "))
    list.append(num)
print(list)

##2
X = int(input("Nhập X: "))
count_X = list.count(X)
print(f"Số {X} xuất hiện {count_X} lần")

##3

list[2:8] = [8,5,4,0,1,3]
print("List sau khi thay thế từ 2-7:", list)

##4

Max_value = max(list)
Min_value = min(list)
print(f"Số lớn nhất:", Max_value)
print(f"Số nhỏ nhất:", Min_value)

##5

Y = int(input("Nhập vào số Y: "))
list.insert(0,Y)
print("List sau khi chèn Y vào đầu:", list)

##6


if list == sorted(list):
    print("Tăng")
elif list == sorted(list, reverse= True):
    print("Giảm")
else:
    print("NO")
