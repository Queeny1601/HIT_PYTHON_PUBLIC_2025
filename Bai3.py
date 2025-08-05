n = int(input(" Nhập số lượng phần tử trong mảng: "))
arr = []
for i in range(n):
    num = int(input(f" Phần tử thứ {i+1} trong mảng là: "))
    arr.append(num)

n1 = int(input(" Nhập số lượng phần tử trong set A (bạn thích): "))
A = set()
for i in range(n1):
    num_A = int(input(f" Phần tử thứ {i+1} trong set A là: "))
    A.add(num_A)

n2 = int(input(" Nhập số lượng phần tử trong set B (khongg thích): "))
B = set()
for i in range(n2):
    num_B = int(input(f" Phần tử thứ {i+1} trong set B là: "))
    B.add(num_B) 
print(arr)
print(A)
print(B)

happiness = 0
for item in arr:
    if item in A:
        happiness += 1
    elif item in B:
        happiness -= 1
print("Mức độ hạnh phúc cuối cùng:", happiness)
