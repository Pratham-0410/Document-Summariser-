📘 Document Summarizer

An open-source text & PDF summarization tool built using FastAPI.
This project is created for ACWOC to help beginners contribute to backend, Python, and open-source development.

✨ Features
	•	Upload PDF or text files
	•	Extract text using pdfminer.six
	•	Generate:
	•	Short summary
	•	Bullet point summary
	•	Long summary
	•	Clean and simple API (/api/v1/summarize)

⸻

🚀 Running the Backend

1. Create and activate venv

cd backend
python3 -m venv venv
source venv/bin/activate

2. Install dependencies

pip install -r requirements.txt

3. Run the server

python -m uvicorn app.main:app --reload --port 8000

API docs available at:
👉 http://127.0.0.1:8000/docs

⸻

📡 Example API Request

Upload text file:

curl -X POST "http://127.0.0.1:8000/api/v1/summarize" \
  -F "file=@samples/sample1.txt" \
  -F "mode=short"

👐 Contributing

This project is ACWOC-friendly.
Please read CONTRIBUTING.md before you begin.

⸻
