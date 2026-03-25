from fastapi import FastAPI,HTTPException
from app.schemas import PostCreate,Response
from app.db import create_db_and_tables,get_async_session,Post
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_db_and_tables()
    yield
    # here we can write the code for closing the database connection

app = FastAPI(lifespan=lifespan )

# @app.get("/hello")
# def hello():
#     return {"message": "hello kashish"}
 
text_post={
    
    1:"hello kashish ",
    2:"how are you",
    3:"fine",
    4:"good day",
    5:"good night",
    6:"miss universe",
    7:"miss world",
    8:"goat",
    9:"mamal",
    10:"raja raghuvanshi"
}
# here we have enter the lage no. of posts with ids

@app.get("/posts")
def get_all_posts():
    return text_post


# learning about the path parameter
@app.get("/posts/{id}")
def get_post_by_id(id : int) ->Response:
    if id not in text_post:
        raise HTTPException(status_code=404,detail="id not found")
    
    return text_post.get(id)


# how to use query parameter inside the function
@app.get("/hello_miss")
def fetch(limit:int=None):
    if limit:
        # return text_post[:limit] this line will throw error because we are applying list operation on dict
        return list(text_post.values())[:limit]
    return text_post



# we can createt the post using the body or by sending the request
@app.post("/createpost")
def createpost(post: PostCreate) -> Response:
    new_post={"title":post.title,"content":post.content}
    # because we are using the pydantic model the api knows that we are sending the request
    text_post[max(text_post.keys())+1]=new_post
    return new_post

#  here we have created an endpoint
# for deleting the data
@app.delete("/deletepost/{id}")
def delete_post(id:int):
    if id not in text_post:
        raise HTTPException(status_code=404,detail="id not found")
    del text_post[id]
    return {"message":f"post with id {id} has been deleted"}




