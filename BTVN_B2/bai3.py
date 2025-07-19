def dem_tong():
    n = int(input("Nhập vào số nguyên n: "))
    count = 0
    sum = 0 
    original_n = n
    
    while n > 0:
        chu_so = n % 10
        sum += chu_so
        count += 1
        n = n // 10
    print(f"Số các chữ số là:{count}. Tổng các chữ số là:{sum}")

dem_tong()


 



