from pydantic import BaseModel
# schemas for request and response data 
# the basemodle is used to define the structure of the data that will be sent and recived from the API endpoints
# here we uset the class 
class PostCreate(BaseModel):
    title:str
    content:str