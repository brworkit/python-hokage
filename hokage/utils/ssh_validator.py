import base64
import struct
def validate_ssh(key, accepted_type="ssh-rsa"):
    try:
        prefix, key_string = key.split()
        data = base64.b64decode(key_string.encode('ASCII'))
        int_len = 4
        str_len = struct.unpack('>I', data[:int_len])[0]  # this should return 7
        return (data[int_len:int_len + str_len].decode('ASCII') == accepted_type)
    except Exception as e:
        return False