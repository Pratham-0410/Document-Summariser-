import re

def split_sentences(text: str):
    return [s.strip() for s in re.split(r'(?<=[.!?]) +', text) if s.strip()]

def rule_based_summary(text: str, mode="short"):
    sentences = split_sentences(text)

    short = sentences[0] if sentences else ""

    bullets = sentences[:3]

    long = " ".join(sentences[:5])

    return {
        "short": short,
        "bullet": bullets,
        "long": long
    }