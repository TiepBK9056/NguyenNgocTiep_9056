import os
import ecdsa

# Tạo thư mục lưu trữ khóa nếu chưa tồn tại
if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        """Tạo khóa riêng tư và khóa công khai"""
        sk = ecdsa.SigningKey.generate()  # Tạo khóa riêng tư
        vk = sk.get_verifying_key()  # Lấy khóa công khai từ khóa riêng tư

        # Lưu khóa vào file
        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())

        with open('cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        """Tải khóa từ file"""
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())

        with open('cipher/ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())

        return sk, vk

    def sign(self, message, key):
        """Ký dữ liệu bằng khóa riêng tư"""
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key):
        """Xác minh chữ ký với khóa công khai"""
        _, vk = self.load_keys()
        try:
            return vk.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False
