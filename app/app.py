import json

from flask import Flask, jsonify, request

from app.config import LOG_FILE
from app.utils import clean_text, load_faiss, load_retriever, retrieve

app = Flask(__name__)

faiss_index = None
medical_questions = None
retriever = None


def load_resources():
    global faiss_index, medical_questions, retriever
    if faiss_index is None or medical_questions is None:
        faiss_index, medical_questions = load_faiss()
    if retriever is None:
        retriever = load_retriever()
    return faiss_index, medical_questions, retriever


def load_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_log(log_data):
    with open(LOG_FILE, "w", encoding="utf-8") as handle:
        json.dump(log_data, handle, ensure_ascii=False, indent=2)


def log_conversation(question, response):
    log_data = load_log()
    log_data.append({
        "question": question,
        "retrieved_answer": response,
    })
    save_log(log_data)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    user_question = str(data.get("question", "")).strip()

    if not user_question:
        return jsonify({"error": "يرجى إدخال سؤال"}), 400

    try:
        _, _, retriever_instance = load_resources()
        clean_q = clean_text(user_question)
        response = retrieve(clean_q, faiss_index, medical_questions, retriever_instance)
    except FileNotFoundError as exc:
        return jsonify({
            "error": "البيانات الداعمة غير موجودة.",
            "details": str(exc),
            "hint": "قم بتشغيل: python scripts/build_faiss_index.py"
        }), 503

    log_conversation(user_question, response)
    return jsonify({"response": response})


@app.route("/log", methods=["GET"])
def show_log():
    return jsonify(load_log())


@app.route("/clear_log", methods=["DELETE"])
def clear_log():
    save_log([])
    return jsonify({"status": "تم مسح سجل المحادثات بنجاح."})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=False)
