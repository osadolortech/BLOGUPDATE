from fastapi import APIRouter
from config.db import collections_post,collection_comments
from models.blog_mod import Blog,Comment
from schemas.blog_sch import blog_schema,blogs_schema,comment_schema,comments_schema
from bson import ObjectId

blog_api_router = APIRouter()

@blog_api_router.get("/")
async def get_post():
    blog = blogs_schema(collections_post.find())
    return{"status":"ok","data":blog}

@blog_api_router.post("/")
async def blog_post(blog: Blog):
    _id =collections_post.insert_one(dict(blog))
    blog = blogs_schema(collections_post.find({"_id": _id.inserted_id}))
    return {"status":"ok", "data": blog}

@blog_api_router.get("/{id}")
async def get_single_post(id: str):
    blog = blogs_schema(collections_post.find({"_id": ObjectId(id)}))
    return{"status":"ok","data":blog}

@blog_api_router.put("/{id}")
async def update_post(id: str,blog: Blog):
    collections_post.find_one_and_update({"_id": ObjectId(id)},{
        "$set": dict(blog)
    })
    blog = blogs_schema(collections_post.find({"_id": ObjectId(id)}))
    return{"status":"ok","data":blog}

@blog_api_router.delete("/{id}")
async def delete_post(id: str):
    collections_post.find_one_and_delete({"_id": ObjectId(id)})
    return{"status":"ok","data":[]}

@blog_api_router.post("/comment")
async def comment_on_post(comment: Comment):
    _id = collection_comments.insert_one(dict(comment))
    comment = comments_schema(collection_comments.find({"_id": _id.inserted_id}))
    return {"status":"ok","data":comment}

@blog_api_router.get("/comment/{id}")
async def single_comment(id: str):
   comment = comments_schema(collection_comments.find({"_id": ObjectId(id)}))
   return {"status":"ok","data":comment}
#all comments WORKS
@blog_api_router.get("/comment/all_comments/comments")
async def all_comment():
   comment = comments_schema(collection_comments.find())
   return {"status":"ok","data":comment}


