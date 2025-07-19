def la_nam_nhuan(nam):
    return( nam % 4 == 0 and nam % 100 != 0)
def so_ngay_trong_thang(thang, nam):
    if thang in[1,3,5,7,8,10,12]:
        return (31)
    elif thang in [4,6,9,11]:
        return(30) 
    elif thang == 2:
        return(29 if la_nam_nhuan(nam) else 28)
    else:
        return("Tháng không hợp lệ")
def main():
    thang = int(input("Tháng: "))
    nam = int(input("Năm: "))
    so_ngay = so_ngay_trong_thang(thang, nam)

    if so_ngay == "Tháng không hợp lệ":
        print(so_ngay)
    else:
        print(f"Tháng {thang} năm {nam} có {so_ngay} ngày.")

main()