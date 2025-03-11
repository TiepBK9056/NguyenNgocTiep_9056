class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text
    
    # def decrypt(self, text, key):
    #     decrypted_text = [''] * key
    #     row, col = 0, 0
    #     for symbol in text:
    #         decrypted_text[col] += symbol
    #         col += 1
    #         if col == key or (col == key -1 and row >= len(text) % key):
    #             col = 0
    #             row += 1
    #     return ''.join(decrypted_text)

    def decrypt(self, text, key):
        num_rows = (len(text) + key - 1) // key  # Tính số hàng cần thiết
        decrypted_text = [''] * num_rows  # Danh sách hàng thay vì cột
        index = 0

        for col in range(key):
            for row in range(num_rows):
                if index < len(text):
                    decrypted_text[row] += text[index]
                    index += 1

        return ''.join(decrypted_text)

    

    
