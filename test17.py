import hashlib

sha256_hash = hashlib.sha256()
sha256_hash.update(b'Hello,')
sha256_hash.update(b'RUNOOB!')
print(sha256_hash.hexdigest())