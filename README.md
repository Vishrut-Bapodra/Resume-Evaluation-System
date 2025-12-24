# 📄 Resume Screening System

A resume screening system built with **Streamlit** that analyzes resumes and job descriptions in PDF and DOCX formats. The system uses **LLM-based reasoning via the OpenRouter API** to evaluate candidate fit and generate clear, explainable insights.

---

## 🧠 Project Overview

This project provides a simple web-based interface where users can upload a job description and multiple resumes for evaluation. Text is extracted from the documents and passed to a large language model, which compares candidate skills and experience against job requirements and returns structured screening results.

---

## ✨ Key Features

- 📂 **Resume & JD Upload:** Supports PDF and DOCX files  
- 🤖 **LLM-Based Evaluation:** Uses structured prompting to assess candidate fit  
- 📊 **Explainable Results:** Generates match scores, skill gaps, and reasoning  
- 🧪 **Streamlit Interface:** Lightweight UI for testing and demonstration  
- 🧩 **Modular Backend:** Clean separation of extraction and evaluation logic  

---

## 🔄 Application Flow
- Upload a job description
- Upload one or more resumes
- Text is extracted from documents
- Resume content is evaluated against the job description
- Results are displayed with scores and explanations

---

## 🛠️ Built With

| Technology | Description |
|------------|-------------|
| **Python 3.x** | Core programming language |
| **Streamlit** | Frontend UI |
| **PyMuPDF** | PDF text extraction |
| **python-docx** | DOCX parsing |
| **OpenRouter API** | LLM-based evaluation |
| **Requests** | API communication |
| **python-dotenv** | Environment variable management |

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- Git
- OpenRouter API Key

---

### 📥 Installation

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
Create and activate a virtual environment

bash
Copy code
python -m venv rcs-venv
rcs-venv\Scripts\activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
⚙️ Configuration
Create a .env file in the project root:

env
Copy code
OPENROUTER_API_KEY=your_api_key_here
▶️ Running the Application
bash
Copy code
streamlit run frontend/app.py
Open your browser at:

arduino
Copy code
http://localhost:8501
