import nltk
import string
import wikipedia

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------- NLTK SETUP (run once) --------------------
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# -------------------- TEXT PREPROCESSING --------------------
def preprocess(text: str) -> str:
    tokens = nltk.word_tokenize(text.lower())
    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word not in stop_words and word not in string.punctuation
    ]
    return " ".join(tokens)

# -------------------- KNOWLEDGE BASE --------------------
qa_pairs = {
    "what is nlp": "NLP stands for Natural Language Processing.",
    "what is python": "Python is a popular programming language.",
    "what is machine learning": "Machine Learning allows systems to learn from data.",
    "what can you do": "I can answer questions using NLP and Wikipedia."
}

questions = [preprocess(q) for q in qa_pairs.keys()]
answers = list(qa_pairs.values())

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# -------------------- WIKIPEDIA FUNCTION --------------------
def get_wikipedia_answer(query: str) -> str:
    try:
        wikipedia.set_lang("en")
        return wikipedia.summary(query, sentences=2)

    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your question is ambiguous. Try one of these: {e.options[:3]}"

    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find information on that topic."

    except Exception:
        return "Wikipedia service is currently unavailable."

# -------------------- CHATBOT LOGIC --------------------
def get_bot_response(user_input: str) -> str:
    greetings = ["hi", "hello", "hey", "good morning", "good evening"]

    cleaned_input = user_input.lower().strip()

    # 1️⃣ Greeting handling
    if cleaned_input in greetings:
        return "Hello! 👋 How can I help you?"

    # 2️⃣ TF-IDF similarity check
    processed_input = preprocess(user_input)
    user_vec = vectorizer.transform([processed_input])

    similarity = cosine_similarity(user_vec, X)
    best_match = similarity.argmax()
    best_score = similarity[0][best_match]

    if best_score >= 0.3:
        return answers[best_match]

    # 3️⃣ Wikipedia fallback
    return get_wikipedia_answer(user_input)