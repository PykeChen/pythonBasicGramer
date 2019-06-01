import zlib

s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s, 4)
print(len(t))

ct = zlib.decompress(t)
print(ct)

print(zlib.crc32(s))
