def format_phone_number(phone: str) -> str:
    """

    Hàm chuẩn hóa số điện thoại Việt Nam về dạng quốc tế (+84)
    
    Thực hiện các bước:
    1. Loại bỏ kí tự không phải số
    2. Kiểm tra tính hợp lệ: bắt đầu bằng 0 và có đúng 10 chữ số
    3. Chuyển 0 thành đầu '+84'
    
    Tham số: 
        phone(str): Chuỗi số điện thoại (có thể chứ kí tự thừa).
        
    Trả về: 
        Str: Số điện thoại chuẩn hóa hoặc "Invalid phone number."
   
    
    """
    digits = "".join(ch for ch in phone if ch.isdigit())

    if len(digits) !=10:
        return "Invalid phone number"
    if not digits.startswith("0"): 
        return "Invalid phone number"
    return "+84" + digits[1:]
 

print(format_phone_number("036-401-7336")) 

