from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

SECRET_KEY = "token_key"
ALGORITHM = "HS256"

class UserAuthentication:

    def __init__(self):
        pass

    def createToken(self, payload):
        payload["iat"] = datetime.now(timezone.utc)
        payload["exp"] = datetime.now(timezone.utc) + timedelta(hours=1)

        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return token

    def validToken(self, token):
        try:
            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=[ALGORITHM]
            )

            print("Token is valid")
            print(payload)

            return payload

        except JWTError as e:
            print("Invalid or Expired Token")
            print(e)
            return {"status":"1"}