import hashlib

class CryptoUtil:
    def __init__(self):
        pass

    def md5_hash(self, text: str) -> str:
        return hashlib.md5(text.encode()).hexdigest()