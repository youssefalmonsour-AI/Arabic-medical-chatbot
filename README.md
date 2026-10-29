# Arabic Medical Chatbot

A lightweight Arabic medical Q&A chatbot built with semantic retrieval and FAISS.

## Project status

This repository was cleaned up and made easier to run from a standard Python project layout.

## Quick start

1. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

2. Generate or place the embedding files if they are missing:
   ```bash
   python scripts/build_faiss_index.py
   ```

3. Start the API:
   ```bash
   python app.py
   ```

4. Test the endpoint:
   ```bash
   curl -X POST http://localhost:4000/predict \
     -H "Content-Type: application/json" \
     -d '{"question":"ما هو علاج ارتفاع ضغط الدم؟"}'
   ```

## Structure

```text
.
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   └── utils.py
├── scripts/
│   └── build_faiss_index.py
├── data/
├── embeddings/
├── app.py
├── config.py
├── utils.py
├── requirements.txt
├── README.md
└── conversations.json
```

## Notes

- The app expects the generated FAISS index and the cleaned medical Q&A CSV to be available under `embeddings/` and `data/`.
- If the files are missing, the API returns a clear error and tells you which command to run.
- The old duplicate root/app layout is kept for compatibility, while the real project code now lives under `app/`.
