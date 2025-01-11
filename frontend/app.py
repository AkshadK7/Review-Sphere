import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("ReviewSphere")

# Dropdown to select a product
products = requests.get(f"{API_URL}/products/").json()
product_names = [product["name"] for product in products]
selected_product = st.selectbox("Select a Product", product_names)

# Add a review
st.subheader("Add Your Review")
review_text = st.text_area("Write your review")
if st.button("Submit Review"):
    product_id = next(
        product["id"] for product in products if product["name"] == selected_product)
    response = requests.post(
        f"{API_URL}/comments/", json={"product_id": product_id, "user_id": 1, "comment_text": review_text})
    st.success("Review submitted!" if response.status_code ==
               200 else "Failed to submit review")

# Clustered comments
st.subheader("Clustered Comments")
if st.button("Generate Clusters"):
    response = requests.post(f"{API_URL}/comments/clusters/")
    st.success(response.json().get("message"))
