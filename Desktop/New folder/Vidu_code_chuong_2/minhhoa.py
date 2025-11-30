import json

# data là đối tượng Python kiểu từ điển (dict)
data = {
    "name": "Ng Văn A",
    "age": 23,
    "skills": ["AI", "Python"]
}

# Chuyển dict Python sang chuỗi JSON
json_str = json.dumps(data, ensure_ascii=False)

print(json_str)
