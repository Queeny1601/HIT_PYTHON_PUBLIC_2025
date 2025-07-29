# 1: Nhập 2 chuỗi s1, s2
s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")


# 2: Đảo ngược chuỗi
print("Đảo chuỗi của s1: ", s1[::-1])
#3: Nhập vào 2 số nguyên `a`, `b` (1 <= a < b <= len(s2)). In ra chuỗi `s2` sau khi đảo ngược chuỗi từ vị trí `a` đến `b`.
a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
if 1 <= a < b <= len(s2):
    S2 = s2[:a] + s2[a:b+1][::-1] + s2[b+1:]
    print("Chuỗi s2 sau khi đảo ngược đoạn từ a - b:", S2)
else:
    print("Nhâp lại a, b thỏa mãn điều kiện 1 <= a < b <= len(s2)")
# 4. In ra chuỗi `s3` là chuỗi `s1` sau khi xóa các kí tự vị trí chẵn.
s3 = ""
for i in range(len(s1)):
    if i % 2 !=0:
        s3 +=s1[i]
print("Chuỗi s3:",s3)
#5. Trả về chuỗi `s4` là đan xen các kí tự của `s1` và `s2`. - VD: `s1 = “abc”`, `s2 = “123”` -> `s4 = “a1b2c3”`.

s4=""
min_len = min(len(s1), len(s2))
for i in range(min_len):
    s4+= s1[i] + s2[i]
for i in range(min_len, len(s1)):
    s4+= s1[1]
for i in range(min_len, len(s2)):
    s4+= s2[i]
print("Chuỗi s4:", s4)



