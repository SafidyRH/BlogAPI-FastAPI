from passlib.context import CryptContext

pwp_cxt = CryptContext(schemes = ["bcrypt"], deprecated="auto")


class Hash():
    def bcrypt(password:str):
        return pwp_cxt.hash(password)

    def verify(hashed_password, plained_password):
        return pwp_cxt.verify(plained_password,hashed_password )