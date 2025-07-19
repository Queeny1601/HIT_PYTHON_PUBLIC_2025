n= int(input("Số tiền (VND): "))
so_bia= n // 28000
vo_bia= so_bia
tong_bia= so_bia
while vo_bia >= 3:
    tang_bia = vo_bia // 3
    tong_bia += tang_bia
    vo_bia = vo_bia % 3 + tang_bia
print(f"Số bia mua được là:{tong_bia}")
