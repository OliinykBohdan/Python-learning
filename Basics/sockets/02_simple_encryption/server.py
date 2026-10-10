import sys


def tcp_recv():
    data = sys.stdin.buffer.readline().strip()

    return data


def get_key():
    return int(sys.stdin.buffer.readline().strip())


def secure_recv(key):
    s_data = tcp_recv()
    data = bytes()

    for s_byte in s_data:
        data += bytes([(s_byte - key) % 256])

    return data

key = get_key()
data = secure_recv(key)

print(data)
