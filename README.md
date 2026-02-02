# 📄 Resume Evaluation System

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

## 📷 Images
<img width="1366" height="681" alt="Screenshot 2025-12-24 165202" src="https://github.com/user-attachments/assets/c07eebc9-4911-4542-9939-20f7b3d38811" />
<img width="1365" height="684" alt="Screenshot 2025-12-24 165125" src="https://github.com/user-attachments/assets/dc106e86-1b9c-4381-989e-572949fb85fe" />
<img width="1365" height="683" alt="Screenshot 2025-12-24 165104" src="https://github.com/user-attachments/assets/0835f7ae-cd69-4ac5-b693-26d66cb40a44" />
<img width="1363" height="685" alt="Screenshot 2025-12-24 165045" src="https://github.com/user-attachments/assets/ffcff08c-1809-414b-b0c3-c761f4f513eb" />

---

### 📥 Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/<your-username>/<your-repo-name>.git
    cd <your-repo-name>
2. Create and activate a virtual environment
   ```bash
    python -m venv rcs-venv
    rcs-venv\Scripts\activate

3. Install dependencies
    ```bash
    pip install -r requirements.txt

4. Configuration
Create a .env file in the project root:
OPENROUTER_API_KEY=your_api_key_here

5. Running the Application
    ```bash
    streamlit run frontend/app.py
