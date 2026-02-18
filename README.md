# 🤖 Intelligent NLP Chatbot using TF-IDF and Wikipedia

## 📖 Project Description
This project implements an **intelligent chatbot** using **Natural Language Processing (NLP)** techniques.  
The chatbot answers user queries using:  
1. **Predefined knowledge base** (TF-IDF + cosine similarity)  
2. **Wikipedia API** as a fallback for unknown questions  

If a question is not confidently matched with the internal dataset, the chatbot automatically fetches a concise explanation from **Wikipedia**, making it more informative and dynamic.

---

## Objectives
- Understand NLP preprocessing techniques
- Implement TF-IDF and cosine similarity
- Integrate an external knowledge source (Wikipedia)
- Build a real-time question-answering chatbot

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
project/
│
├── main.py # Run server
├── chatbot.py # Core chatbot logic
├── requirements.txt # Dependency list
└── README.md # Project documentation

---

## 🛠️ Installation Steps

### Step 1️⃣: Create Virtual Environment (Recommended)
```bash
python -m venv venv
```
Activate the environment:
Windows
```bash
venv\Scripts\activate
```
Linux / macOS
```bash
source venv/bin/activate
```
### Step 2️⃣: Install Dependencies
```bash
pip install nltk scikit-learn wikipedia
uvicorn main:app --reload

```
### Step 3️⃣: Run the Chatbot
```bash
python main.py
```

