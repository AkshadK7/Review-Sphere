# **ReviewSphere**

_A dynamic review management platform integrating NLP-powered sentiment analysis, clustering, and recommendation systems to enhance user insights and product feedback._

---

## Features

- **Sentiment Analysis**  
  Automatically detect and classify reviews as positive or negative using a threshold-based sentiment model.
- **Tag Extraction**  
  Extract the most common tags from user reviews using Named Entity Recognition (NER).
- **Review Clustering**  
  Group similar reviews using K-Means clustering, enabling better insights into customer opinions.
- **Recommendation Engine**  
  Suggest products to users based on their review history and preferences.
- **Data Visualization**
  - View common tags in a horizontal stack and a pie chart.
  - Explore overall sentiment in bar and pie charts.
- **User-Friendly Interface**
  - Add, view, and manage reviews through an interactive UI.
  - See scrollable lists of reviews sorted by timestamps.

---

## Tech Stack

### **Backend**

- **FastAPI**: Handles API endpoints and CRUD operations.
- **SQLite**: Lightweight database for persisting product, review, and user data.
- **Spacy**: Used for Named Entity Recognition (NER) and generating text embeddings for clustering.
- **TextBlob**: Provides sentiment analysis of review text.
- **Scikit-Learn**: Implements K-Means clustering for grouping reviews.

### **Frontend**

- **Streamlit**: Offers a clean, interactive UI for submitting and visualizing review data.

---

## Folder Structure

````plaintext
ReviewSphere/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI entry point
│   │   ├── database.py          # Database models and operations
│   │   ├── models.py            # Database schema initialization
│   │   ├── nlp_utils.py         # NLP and clustering utilities
│   ├── requirements.txt         # Backend dependencies
│   └── uvicorn_runner.py        # Script to start FastAPI server
│
├── frontend/
│   ├── app.py                   # Streamlit frontend application
│   ├── requirements.txt         # Frontend dependencies
│
└── store.db                     # SQLite database

---

## Setup Instructions

### **1. Backend Setup**
1. Navigate to the `backend` directory:
   ```bash
   cd backend
2. Install dependencies:
   ```bash
    pip install -r requirements.txt
3. Start the FastAPI server:
   ```bash
    uvicorn app.main:app --reload

### **2. Frontend Setup**
1. Navigate to the `frontend` directory:
   ```bash
    cd frontend
2. Install dependencies:
   ```bash
    pip install -r requirements.txt
3. Run the Streamlit app:
   ```bash
    streamlit run app.py

### **3. Using the Application**
- Open your browser at the URL provided by Streamlit (default is [http://localhost:8501](http://localhost:8501)).
- Select a product from the dropdown, submit reviews, and explore visualizations for sentiment analysis, tags, and clusters.
- View personalized recommendations for similar products.

---

## Future Enhancements
- **Deep Learning Integration**: Replace traditional models with Transformer-based architectures for improved sentiment analysis and tagging.
- **Collaborative Filtering**: Enhance the recommendation engine with collaborative filtering for better user-product matching.
- **Language Support**: Add support for multiple languages in reviews.
- **Customizable Dashboards**: Allow users to create custom reports and dashboards.

---

## Contributing

Contributions are welcome! Please fork the repository, create a branch, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Enjoy Reviewing the world of Natural Language Processing! 🚀
````
