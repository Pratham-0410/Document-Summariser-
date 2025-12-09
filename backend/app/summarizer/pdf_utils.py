# backend/app/summarizer/pdf_utils.py
import logging
from typing import Optional

logger = logging.getLogger(__name__)

# lazy import so server doesn't crash at import time if package is missing
try:
    from pdfminer.high_level import extract_text as _extract_text_pdfminer
    _HAS_PDFMINER = True
except Exception as ex:
    _HAS_PDFMINER = False
    _PDFMINER_IMPORT_ERROR = ex
    logger.warning("pdfminer.six not available: %s", ex)


def extract_text_from_pdf(path: str) -> str:
    """
    Extract text from PDF file.

    If pdfminer is unavailable or extraction fails, this function returns
    an empty string and logs the error (does not raise at import time).
    """
    if not _HAS_PDFMINER:
        logger.error("pdfminer.six not installed or failed to import: %s", _PDFMINER_IMPORT_ERROR)
        return ""

    try:
        text = _extract_text_pdfminer(path)
        return text or ""
    except Exception as e:
        logger.exception("Failed to extract text from PDF %s: %s", path, e)
        return ""