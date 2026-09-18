from pwdlib import PasswordHash


password_hash=PasswordHash.recommended()


def hash_password(password:str):
    return password_hash.hash(password)

def verify_password(p1:str,hashed_p:str):
    return password_hash.verify(p1,hashed_p)