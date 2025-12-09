from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from app.summarizer.rule_based import rule_based_summary
from app.summarizer.pdf_utils import extract_text_from_pdf
import uuid, os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/summarize")
async def summarize(file: UploadFile = File(...), mode: str = Form("short")):
    if file.content_type not in ("application/pdf", "text/plain"):
        raise HTTPException(status_code=400, detail="Only PDF or TXT allowed")

    job_id = str(uuid.uuid4())
    filename = f"{job_id}_{file.filename}"
    filepath = os.path.join(UPLOAD_DIR, filename)

    with open(filepath, "wb") as f:
        f.write(await file.read())

    # extract text
    if file.content_type == "application/pdf":
        text = extract_text_from_pdf(filepath)
    else:
        text = open(filepath, "r", encoding="utf-8").read()

    summaries = rule_based_summary(text)

    return JSONResponse({
        "id": job_id,
        "status": "done",
        "summaries": summaries
    })