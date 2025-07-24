# config.py

# مسارات التضمينات وفهرس FAISS
EMBEDDINGS_PATH = "../embeddings/medical_questions.npy"
FAISS_INDEX_PATH = "../embeddings/faiss_index.bin"

# نموذج الاسترجاع الدلالي المستخدم
RETRIEVER_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"