import json

# Đối tượng Python (đối tượng dict)
data = {
    "Ho_va_ten": "Dương Văn Quỳnh",
    "Nam_sinh": 2006,
    "Gioi_tinh": "Nam",
    "so_dt": "0976095422",
    "email": "dvquynh.24174600058@sv.uneti.edu.vn"
}

# Sử dụng 'with open' để mở tệp 'thongtin.json' với chế độ ghi ('w') và mã hóa utf-8
# Hàm json.dump() sẽ ghi đối tượng Python trực tiếp vào tệp đã mở
with open('Chương 2. json/Ví dụ chương 2/thongtin.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)  # Ghi đối tượng Python vào file thongtin.json

print("Dữ liệu đã được ghi thành công vào tệp 'thongtin.json'.")
