from passlib.context import CryptContext


passowrd_context = CryptContext(schemes='bcrypt', deprecated='auto')

class Hash():
    def bcrypt(password:str):
        return passowrd_context.hash(password)
    def verify(hashed_password, plain_password):
        return passowrd_context.verify(hashed_password,plain_password)
        