def tinh_thue(luong):
    if luong >= 15000000:
        return luong * 0.3
    elif luong >= 7000000:
        return luong * 0.2
    else:
        return luong * 0.1
    
def main():
    luong = float(input("Nhập lương nhân viên: "))
    thue = float(tinh_thue(luong))
    thu_nhap = float(luong - thue)
    print (f"Thuế thu nhập: {thue}")
    print (f"Thu nhập: {thu_nhap}")
main()