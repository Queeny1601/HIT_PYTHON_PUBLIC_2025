n = int(input("Nhập số dòng của ma trận: "))
m = int(input("Nhập số cột của ma trận: "))
def matrix(m,n):
    """
    Hàm matrix(n,m) để nhập một ma trận có n dòng và m cột từ người dùng.

    Bước thực hiện:
    1. Tạo một danh sách rỗng a để lưu ma trận.
    2. Dùng vòng lặp for chạy từ 0 đến n-1 để nhập từng dòng
    - Với mỗi dòng tạo một danh sách row rỗng.
    - Dùng vòng lặp for để chạy từ 0 đến m-a để nhập phần tử từng dòng
    - Sử dụng imput() để nhập số nguyên, append vào rơ
    3. Sau khi nhập xong một dòng, append row vào a
    4. Trả về ma trận a dạng danh sách 2 chiều.
    """
    a= []
    print(" Nhập các phần tử của ma trận: ")
    for i in range(n):
        row = []
        for j in range(m):
            num = int(input(f"Nhập phần tử a[{i+1}, {j+1}]: "))
            row.append(num)
        a.append(row)
    return a


def trans_matrix(matrix):
    """
    Hàm trans_matrix(matrix) dùng để tính ma trận chuyển vị của một ma trận 'matrix'
    
    Bước thực hiện:
    1. Dùng zip(*) để ghép các phần tử cùng cột của ma trận gốc thành các hàng mới.
    2. Mỗi phần tử zip trả về là tuple, dùng list() để chuyển thành danh sách.
    3. Trả về ma trận chuyển vị dưới dạng danh sách 2 chiểu.
    """
    return[list(row) for row in zip(*matrix)]

# Nhập ma trận bạn đầu
mat = matrix (n,m)
print("Ma trận vừa nhập: ")
for row in mat:
    print(*row)

# Ma trận chuyển vị
trans = trans_matrix(mat)
print(" Ma trận chuyển vị: ")
for row in trans:
    print(*row)

print("Ma trận ban đầu vẫn là: ")
for row in mat:
    print(*row)

