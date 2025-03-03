# tạo một danh sách rỗng để lưu kết quả
j = [ ]
# Duyệt qua tất cả các số trong đoạn từ 2000 đến 3000, kiểm tra xem số i có chia hết cho 7 và không phải là bội số của 5 khong
for i in range(2000, 3001):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))