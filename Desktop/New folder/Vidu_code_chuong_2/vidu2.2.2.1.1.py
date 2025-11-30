import json

# TẠO ĐỐI TƯỢNG PYTHON (DICTIONARY)
data = {
    "Ho_va_ten": "Ng Văn A",
    "Nam_sinh": 2025,
    "Gioi_tinh": "Nam",
    "so_dt": "0123456789",
    "email": "nguyenvana@uneti.edu.vn"
}

# CHUYỂN ĐỐI TƯỢNG PYTHON THÀNH CHUỖI JSON
json_string = json.dumps(data, ensure_ascii=False)

# IN KẾT QUẢ RA MÀN HÌNH
print(json_string)
print(type(json_string))
