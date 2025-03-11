from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
app = Flask(__name__)

#CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()
vigenere_ceipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayfairCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt(plain_text, key)
    return jsonify({"encrypted_message": encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt(cipher_text, key)
    return jsonify({"decrypted_message": decrypted_text})

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']                   
    encrypted_text = vigenere_ceipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text' : encrypted_text} )

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_ceipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

@app.route('/api/railfence/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypt_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypt_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypt_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypt_text})

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'matrix': playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    key = data['key']
    plain_text = data['plain_text']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)