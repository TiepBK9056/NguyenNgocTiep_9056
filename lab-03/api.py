from flask import Flask, request, jsonify
from cipher.rsa.rsa_cipher import RSACipher
from cipher.ecc import ECCCipher

app = Flask(__name__)

# RSA Cipher Instance
rsa_cipher = RSACipher()

@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route('/api/rsa/encrypt', methods=['POST'])
def rsa_encrypt():
    data = request.json
    message = data.get('message')  # Changed from 'Message' to 'message' to match client code
    key_type = data.get('key_type')
    
    # Validate message is not None
    if message is None:
        return jsonify({'error': 'Message is required'}), 400
        
    private_key, public_key = rsa_cipher.load_keys()
    if key_type == 'public':
        key = public_key
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({'error': 'Invalid key type'}), 400
    
    encrypted_message = rsa_cipher.encrypt(message, key)
    encrypted_hex = encrypted_message.hex()
    return jsonify({'encrypted_message': encrypted_hex})




@app.route('/api/rsa/decrypt', methods=['POST'])
def rsa_decrypt():
    data = request.json
    ciphertext_hex = data.get('ciphertext')
    key_type = data.get('key_type')
    
    private_key, public_key = rsa_cipher.load_keys()
    key = public_key if key_type == 'public' else private_key if key_type == 'private' else None
    
    if not key:
        return jsonify({'error': 'Invalid key type'})
    
    ciphertext = bytes.fromhex(ciphertext_hex)
    decrypted_message = rsa_cipher.decrypt(ciphertext, key)
    return jsonify({'decrypted_message': decrypted_message})

@app.route('/api/rsa/sign', methods=['POST'])
def rsa_sign_message():
    data = request.json
    message = data.get('message')
    private_key, _ = rsa_cipher.load_keys()
    
    signature = rsa_cipher.sign(message, private_key)
    return jsonify({'signature': signature.hex()})

@app.route('/api/rsa/verify', methods=['POST'])
def rsa_verify_signature():
    data = request.json
    message = data.get('message')
    signature_hex = data.get('signature')
    
    public_key, _ = rsa_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = rsa_cipher.verify(message, signature, public_key)
    
    return jsonify({'is_verified': is_verified})


##ECC CIPHER ALGORTHIM
ecc_cipher = ECCCipher()

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'ECC keys generated successfully'})

@app.route('/api/ecc/sign' , methods =['POST'])
def ecc_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    data = request.json
    message = data.get('message')
    signature_hex = data.get('signature')
    
    # Validate inputs
    if not message:
        return jsonify({'error': 'Message is required'}), 400
    if not signature_hex:
        return jsonify({'error': 'Signature is required'}), 400
    
    public_key, _ = ecc_cipher.load_keys()
    
    try:
        signature = bytes.fromhex(signature_hex)
        is_verified = ecc_cipher.verify(message, signature, public_key)
        return jsonify({'is_verified': is_verified})
    except ValueError as e:
        return jsonify({'error': f'Invalid signature format: {str(e)}'}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
