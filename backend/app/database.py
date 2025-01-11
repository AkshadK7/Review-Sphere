import sqlite3
from .nlp_utils import generate_clusters

DB_PATH = "store.db"

def add_product(product):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Product (name) VALUES (?)", (product.name,))
    conn.commit()
    product_id = cursor.lastrowid
    conn.close()
    return {"id": product_id, "name": product.name}

def list_products():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM Product")
    products = cursor.fetchall()
    conn.close()
    return [{"id": p[0], "name": p[1]} for p in products]

def add_comment(comment, sentiment, tags):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Comment (product_id, user_id, comment_text, sentiment, tags) VALUES (?, ?, ?, ?, ?)",
                   (comment.product_id, comment.user_id, comment.comment_text, sentiment, ",".join(tags)))
    conn.commit()
    comment_id = cursor.lastrowid
    conn.close()
    return {"id": comment_id, "product_id": comment.product_id, "user_id": comment.user_id, "comment_text": comment.comment_text, "sentiment": sentiment, "tags": tags}

def list_comments(product_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, comment_text, sentiment, tags, cluster_id, timestamp FROM Comment WHERE product_id = ? ORDER BY timestamp DESC", (product_id,))
    comments = cursor.fetchall()
    conn.close()
    return [{"id": c[0], "text": c[1], "sentiment": c[2], "tags": c[3].split(","), "cluster_id": c[4], "timestamp": c[5]} for c in comments]

def update_comment_clusters():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, comment_text FROM Comment")
    comments = cursor.fetchall()

    if not comments:
        conn.close()
        return {"message": "No comments to cluster."}

    comment_ids = [c[0] for c in comments]
    comment_texts = [c[1] for c in comments]

    clusters = generate_clusters(comment_texts)

    for comment_id, cluster_id in zip(comment_ids, clusters):
        cursor.execute("UPDATE Comment SET cluster_id = ? WHERE id = ?", (cluster_id, comment_id))
    
    conn.commit()
    conn.close()
    return {"message": "Clusters updated successfully!"}
