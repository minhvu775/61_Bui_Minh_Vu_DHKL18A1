import json

# Viết một hàm để kiểm tra xem một đối tượng có phải là số phức hay không
def complex_encode(obj):
    # Kiểm tra sử dụng isinstance()
    if isinstance(obj, complex):
        return [obj.real, obj.imag]
    # Kích hoạt lỗi nếu obj không phải là số phức
    raise TypeError(repr(obj) + " is not JSON serializable")

# Dữ liệu không phải là đối tượng số phức
data = {1, 2, 3}

# Sử dụng hàm json.dumps() để mã hóa dữ liệu
# Khi gặp kiểu dữ liệu không hỗ trợ, hàm sẽ kích hoạt lỗi TypeError
complex_obj = json.dumps(data, default=complex_encode)

print(complex_obj)
