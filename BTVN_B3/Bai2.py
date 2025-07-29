# Nhập list a có k phần tử (từ bàn phím)
k = int(input("Nhập số phần tử của list a(k): "))
a = []

for i in range(k):
      nums = int(input(f"Nhập phần tử thứ {i+1}: "))
      a.append(nums)

# Nhập 2 số nguyên n và m (số dòng và cột của ma trận)
n = int(input("Nhập số dòng của ma trận: "))
m = int(input("Nhập số cột của ma trận: "))

# Kiểm tra xem có tạo được ma trận không
if k!= n*m:
        print("No")
else:
    MT = []
    for i in range(n):
          row = a[i*m:(i+1)*m]
          MT.append(row)

print("Ma trận thu được là:")
for row in MT:
      print(row)