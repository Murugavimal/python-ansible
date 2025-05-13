from pydantic import BaseModel

class userdata(BaseModel):
    username: str
    email : str
    city: str 