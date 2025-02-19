from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

# Download NLTK stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords

# Sample Documents
documents = [
    "The cat in the hat.",
    "The quick brown fox jumps over the lazy dog.",
    "The dog barks at the cat in the park.",
    "Foxes are wild animals that live in forests."
]

# Query
query = "cat in the park"

# Step 1: Preprocess the documents and query by removing stopwords
stop_words = stopwords.words('english')

# Function to remove stopwords
def preprocess(text):
    return ' '.join([word for word in text.lower().split() if word not in stop_words])

# Preprocess documents and query
documents = [preprocess(doc) for doc in documents]
query = preprocess(query)

# Step 2: Create the TF-IDF model
vectorizer = TfidfVectorizer()

# Fit the model on the documents
tfidf_matrix = vectorizer.fit_transform(documents)

# Step 3: Convert the query to the same vector space
query_vector = vectorizer.transform([query])

# Step 4: Calculate cosine similarities between the query and each document
cosine_similarities = cosine_similarity(query_vector, tfidf_matrix)

# Step 5: Rank documents based on cosine similarity
sorted_indices = cosine_similarities[0].argsort()[::-1]

# Print the documents sorted by relevance to the query
print("Query:", query)
print("\nRanked Documents:")
for index in sorted_indices:
    print(f"Document: '{documents[index]}' - Similarity Score: {cosine_similarities[0][index]:.4f}")
