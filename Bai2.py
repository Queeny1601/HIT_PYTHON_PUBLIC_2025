n1 = int(input("Nhập số sinh viên đăng kí tại bàn 1: "))
A = set()
for i in range (n1):
    Ma_SV = input(f" Nhập mã sinh viên thứ {i+1}: ")
    A.add(Ma_SV)

n2 = int(input("Nhập số sinh viên đăng kí tại bàn 1: "))
B = set()
for i in range (n2):
    Ma_SV = input(f" Nhập mã sinh viên thứ {i+1}: ")
    B.add(Ma_SV)

print(" Danh sách sinh viên bàn tiếp nhận số 1:", A)
print(" Danh sách sinh viên bàn tiếp nhận số 2",B)

# Sinh viên đăng kí cả hai bàn
both = A.intersection(B)
if both:
    print(" Sinh viên đăng kí ở cả hai bàn:", both)
else: 
    print(" Không có sinh viên nào đăng kí ở hai bàn.")

# Danh sách tổng hợp
 
all = A.union(B)
print(" Danh sách tổng hợp của các sinh viên đã đăng ký của cả hai bàn.", all)

# Danh sách các sinh viên đã đăng ký tại bàn 1 mà không đăng ký tại bàn 2
Only_1 = A - B
print(" Danh sách sinh viên chỉ đăng kí bàn 1", Only_1)