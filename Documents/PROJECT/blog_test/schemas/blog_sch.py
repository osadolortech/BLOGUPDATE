def blog_schema(blog) -> dict:
    return{
        "id": str(blog["_id"]),
        "name": blog["name"],
        "title": blog["title"],
        "content": blog["content"]    
    }

def blogs_schema(blogs) ->list:
    return [blog_schema(blog) for blog in blogs]

def comment_schema(comment) -> dict:
    return{
        "content": comment["content"]
    }

def comments_schema(comments) ->list:
    return [comment_schema(comment) for comment in comments]