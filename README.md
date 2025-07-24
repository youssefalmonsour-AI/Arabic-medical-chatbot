Sure! Here’s a professional English version of the README.md for your Arabic Medical Chatbot graduation project:

⸻

 Arabic Medical Chatbot

An Arabic-language AI-powered medical assistant
 Graduation Project – Faculty of Computers and Information
 Selected as one of the top graduation projects of 2025

⸻

 Project Description

Arabic Medical Chatbot is an AI-based system designed to answer medical questions in Arabic using semantic retrieval techniques.
The chatbot provides quick and informative responses to health-related queries based on a large medical knowledge base.

⸻

 Main Components
 •  Medical Knowledge Base: Over 800,000 Arabic medical Q&A pairs.
 •  Embedding Model: SBERT-based sentence transformer for semantic representation.
 •  FAISS Index: For fast similarity search and retrieval of relevant answers.
 •  Flask API: A lightweight web server for sending questions and receiving answers.

⸻

 Getting Started

1. Install Requirements
pip install -r requirements.txt
2. Run the Flask API
cd app
python app.py
3. Example API Request
POST http://localhost:5000/predict/
Content-Type: application/json

{
  "question": "ما هو علاج ارتفاع ضغط الدم؟"
}
4. Example API Response
{
  "response": {
    "input": "ما هو علاج ارتفاع ضغط الدم؟",
    "output": "يجب متابعة ضغط الدم بانتظام، تقليل الملح، ممارسة الرياضة، وتناول أدوية الضغط تحت إشراف الطبيب."
  }
}
Project Structure
Arabic-medical-chatbot/
├── app/                  ← Flask API source code
│   ├── app.py
│   ├── utils.py
│   └── config.py
│
├── embeddings/           ← FAISS index and question embeddings
│   ├── faiss_index.bin
│   └── medical_questions.npy
│
├── models/               ← Pretrained SBERT model
│   └── sbert_model/
│
├── notebooks/            ← Jupyter Notebooks for data preparation & model training
│   ├── 01_prepare_data.ipynb
│   ├── 02_train_generator.ipynb
│   └── 03_build_faiss_index.ipynb
│
├── requirements.txt
└── README.md
Disclaimer

This chatbot is not a replacement for professional medical advice. It is intended for educational and research purposes only.
Contact
 • GitHub: youssefalmonsour-AI
 • Email: youssefalmonsour222@gmail.com
 