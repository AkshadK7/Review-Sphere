from fastapi import FastAPI
from pydantic import BaseModel
from .database import add_product, list_products, add_comment, list_comments, update_comment_clusters

app = FastAPI()

class Product(BaseModel):
    name: str

class Comment(BaseModel):
    product_id: int
    user_id: int
    comment_text: str

@app.post("/products/")
def create_product(product: Product):
    return add_product(product)

@app.get("/products/")
def get_products():
    return list_products()

@app.post("/comments/")
def create_comment(comment: Comment):
    from .nlp_utils import analyze_sentiment, extract_tags
    sentiment = analyze_sentiment(comment.comment_text)
    tags = extract_tags(comment.comment_text)
    return add_comment(comment, sentiment, tags)

@app.get("/comments/")
def get_comments(product_id: int):
    return list_comments(product_id)

@app.post("/comments/clusters/")
def cluster_comments():
    result = update_comment_clusters()
    return result
