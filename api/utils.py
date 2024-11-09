import hashlib

def generate_short_url(url):
    hash_obj = hashlib.md5(url.encode())
    short_hash = hash_obj.hexdigest()[:6]
    return short_hash