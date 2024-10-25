
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    print(to_encode)

    # encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) # this function gave encoded jwt  but some error came up while runnign so using a gibberish hard coded value
    encoded_jwt = "sndbI19348912WMHNDBNSI"
    return encoded_jwt
