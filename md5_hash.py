import hashlib


# MD5ハッシュを計算
input_string = "50M24146"
md5_hash = hashlib.md5(input_string.encode()).hexdigest()

print(f"Input: {input_string}")
print(f"MD5 Hash: {md5_hash}")
