"""
Philippine Law Assistant - Flask (slim) version.
Python 3.14 compatible - no pydantic, no chromadb, no compilation.

Run: python app_slim.py
"""
from flask import Flask, request, jsonify, Response
from flask_cors import CORS

from app.services.llm_simple import chat, chat_stream
from app.services.test_simple import generate_question, evaluate_answer

app = Flask(__name__)
# Allow localhost and common dev origins; use * for mobile/same-network access
CORS(app, origins=["*"], supports_credentials=False)


@app.route("/")
def root():
    return jsonify({"message": "Philippine Law Assistant API", "status": "ok"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json() or {}
    msg = (data.get("message") or "").strip()
    if not msg:
        return jsonify({"detail": "Message cannot be empty"}), 400
    history = data.get("history") or []
    response = chat(msg, history)
    return jsonify({"response": response})


@app.route("/api/chat/stream", methods=["POST"])
def api_chat_stream():
    data = request.get_json() or {}
    msg = (data.get("message") or "").strip()
    if not msg:
        return jsonify({"detail": "Message cannot be empty"}), 400
    history = data.get("history") or []

    def generate():
        for chunk in chat_stream(msg, history):
            yield f"data: {chunk}\n\n"

    return Response(
        generate(),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive", "X-Accel-Buffering": "no"},
    )


@app.route("/api/voice/chat", methods=["POST"])
def api_voice_chat():
    data = request.get_json() or {}
    msg = (data.get("message") or "").strip()
    if not msg:
        return jsonify({"detail": "Message cannot be empty"}), 400
    history = data.get("history") or []
    response = chat(msg, history)
    return jsonify({"response": response})


@app.route("/api/test/generate", methods=["POST"])
def api_test_generate():
    data = request.get_json() or {}
    topic = data.get("topic")
    difficulty = data.get("difficulty") or "moderate"
    return jsonify(generate_question(topic=topic, difficulty=difficulty))


@app.route("/api/test/submit", methods=["POST"])
def api_test_submit():
    data = request.get_json() or {}
    question = data.get("question") or {}
    answer = data.get("answer") or ""
    return jsonify(evaluate_answer(question, answer))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
