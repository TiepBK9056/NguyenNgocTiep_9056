# Hàm kiểm tra số nhị phân có chia hết cho 5 không
def chia_het_cho_5(so_nhi_phan):
    # Chuyển số nhị phân sang hệ 10
    so_he_10 = int(so_nhi_phan, 2)
    # Kiểm tra xem số hệ 10 có chia hết cho 5 không
    if so_he_10 % 5 == 0:
        return True
    return False
# Nhập số nhị phân từ người dùng
chuoi_so_nhi_phan = input("Nhập số nhị phân (phân tách bởi dấu phẩy): ")
# Tach chuoi so nhị phân thành các số nhị phân và kiểm tra số chia hết cho 5
so_nhi_phan_list = chuoi_so_nhi_phan.split(",")
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]
# In ra các số nhị phân chia hết cho 5
if len(so_chia_het_cho_5) > 0:
    ket_qua = ", ".join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5 là:", ket_qua)
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập.")