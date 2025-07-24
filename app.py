import json
from flask import Flask, request, jsonify
from utils import (
    load_faiss,
    load_retriever,
    clean_text,
    retrieve,
)

app = Flask(__name__)

# تحميل الموارد عند التشغيل
print("تحميل قاعدة المعرفة...")
faiss_index, medical_questions = load_faiss()

print("تحميل نموذج الاسترجاع...")
retriever = load_retriever()

print("كل الموارد تم تحميلها بنجاح.")

# مسار السجل
LOG_FILE = "conversations.json"

# إنشاء أو تحميل السجل
def load_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_log(log):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)

# إضافة محادثة للسجل
def log_conversation(question, response):
    log = load_log()
    log.append({
        "question": question,
        "retrieved_answer": response
    })
    save_log(log)

#  نقطة الاسترجاع والتسجيل
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    user_question = data.get("question", "").strip()
    
    if not user_question:
        return jsonify({"error": "يرجى إدخال سؤال"}), 400
    
    clean_q = clean_text(user_question)
    retrieved = retrieve(clean_q, faiss_index, medical_questions, retriever)

    # تسجيل
    log_conversation(user_question, retrieved)

    return jsonify({"response": retrieved})

#  نقطة عرض السجل
@app.route("/log", methods=["GET"])
def show_log():
    log = load_log()
    return jsonify(log)

#  نقطة حذف السجل
@app.route("/clear_log", methods=["DELETE"])
def clear_log():
    save_log([])
    return jsonify({"status": "تم مسح سجل المحادثات بنجاح."})

#  نقطة التأكد من صحة السيرفر
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

#  تشغيل الخادم
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=False)