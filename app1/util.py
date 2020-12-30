from Crypto.Cipher import DES3

def Encrypt(g_key, img_file):
    given_key = bytes(g_key, 'utf-8')
    while True:
        try:
            key = DES3.adjust_key_parity(given_key)
            break
        except ValueError:
            pass
    input_file = open(img_file, "rb")
    input_data = input_file.read()
    input_file.close()

    iv = b"abcdefgh"

    cipher = DES3.new(key, DES3.MODE_CFB, iv)
    enc_data = cipher.encrypt(input_data)
    return enc_data

def Decrypt(g_key, img_file):
    given_key = bytes(g_key, 'utf-8')
    while True:
        try:
            key = DES3.adjust_key_parity(given_key)
            break
        except ValueError:
            pass
    enc_file = open(img_file, "rb")
    enc_data = enc_file.read()
    enc_file.close()

    iv = b"abcdefgh"

    decipher = DES3.new(key, DES3.MODE_CFB, iv)
    plain_text = decipher.decrypt(enc_data)
    return plain_text
