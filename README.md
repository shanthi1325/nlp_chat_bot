# 🤖 NLP Chatbot with Wikipedia Integration

## Project Title

**Intelligent NLP Chatbot using TF-IDF and Wikipedia**

---

## 📖 Project Description

This project implements an **intelligent chatbot** using **Natural Language Processing (NLP)** techniques.
The chatbot answers user queries using:

1. **Predefined knowledge base** (TF-IDF + cosine similarity)
2. **Wikipedia API** as a fallback for unknown questions

If a question is not confidently matched with the internal dataset, the chatbot automatically fetches a concise explanation from **Wikipedia**, making it more informative and dynamic.

---

## Objectives

- To understand NLP preprocessing techniques
- To implement TF-IDF and cosine similarity
- To integrate an external knowledge source (Wikipedia)
- To build a real-time question-answering chatbot

---

## Technologies Used

- **Python 3**
- **NLTK**
- **Scikit-learn**
- **Wikipedia API**
- **TF-IDF Vectorizer**
- **Cosine Similarity**

---

## System Requirements

### Software

- Python 3.8 or higher
- pip (Python package manager)

### Libraries

- nltk
- scikit-learn
- wikipedia

---

## 📂 Project Structure

```
project/
│
├── main.py             #run server
├── chatbot.py          # Core chatbot logic
├── requirements.txt    # Dependency list
└── README.md           # Project documentation
```

---

## 🛠️ Installation Steps

### Step 1️⃣: Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### Step 2️⃣: Install Dependencies

```bash
pip install nltk scikit-learn wikipedia
```

---

### Step 3️⃣: Run the Chatbot

```bash
python main.py
```

> 📌 Note: NLTK resources (`punkt`, `stopwords`, `wordnet`) will be downloaded automatically on first run.

---

## 🧩 How the Chatbot Works

### 1️⃣ Text Preprocessing

- Converts text to lowercase
- Tokenizes sentences
- Removes stopwords and punctuation
- Applies lemmatization

### 2️⃣ Knowledge Base Matching

- Uses **TF-IDF Vectorizer**
- Measures similarity using **Cosine Similarity**
- Returns best matched answer if similarity ≥ threshold

### 3️⃣ Wikipedia Fallback

- If similarity score is low
- Fetches a **2-sentence summary** from Wikipedia
- Handles ambiguity and missing pages gracefully

---

## 💬 Example Interaction

| User Input                  | Chatbot Output                              |
| --------------------------- | ------------------------------------------- |
| hello                       | Hello! 👋 How can I help you?               |
| what is nlp                 | NLP stands for Natural Language Processing. |
| wikipedia is also comes nlp | Wikipedia-based explanation                 |
| artificial intelligence     | Wikipedia summary                           |

---

## 📌 Key Features

- Greeting recognition
- NLP-based question answering
- Wikipedia-powered responses
- Error handling for ambiguous queries
- Lightweight and fast execution

---

## 🚀 Applications

- Academic mini project
- NLP learning tool
- Chatbot prototype
- Resume / portfolio project
- Base for AI assistants

---

## 🔮 Future Enhancements

- Speech-to-text integration
- Database for chat history
- User authentication
- Deployment using FastAPI + React
- Replace Wikipedia with LLM APIs

---
