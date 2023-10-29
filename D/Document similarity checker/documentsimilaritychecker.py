pip install nltk
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

# Sample documents
document1 = "Natural language processing is a field of study in artificial intelligence."
document2 = "NLP focuses on the interaction between computers and human languages."

def preprocess_text(text):
    # Tokenization
    words = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Stemming
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    return " ".join(words)

# Preprocess the documents
document1 = preprocess_text(document1)
document2 = preprocess_text(document2)

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the documents into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform([document1, document2])

# Calculate the cosine similarity between the documents
cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

# Similarity score ranges from 0 (not similar) to 1 (identical)
print("Cosine Similarity:", cosine_sim[0][0])

if cosine_sim[0][0] >= 0.7:
    print("The documents are highly similar.")
else:
    print("The documents are not very similar.")
