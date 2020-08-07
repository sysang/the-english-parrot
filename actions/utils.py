from zlib import crc32

def _bytes_to_float(b):
    return float(crc32(b) & 0xffffffff) / 2**32

def text_to_float(s, encoding="utf-8"):
    return _bytes_to_float(s.encode(encoding))
