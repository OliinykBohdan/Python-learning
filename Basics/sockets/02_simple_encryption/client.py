data = b'hello'
key = 5


def tcp_send_all(data: bytes):
    print(data.decode())


def send_key():
    print(key)


def secure_send_all(data):
    s_data = bytes()

    for byte in data:
        s_data += bytes([(byte + key) % 256])

    tcp_send_all(s_data)


send_key()
secure_send_all(data)
