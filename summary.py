from transformers import pipeline
from question_generation.pipelines import pipeline as npl_pipeline

summarizer = pipeline(
    "summarization",
    "pszemraj/long-t5-tglobal-base-16384-book-summary",
    device= -1,
)

nlp = npl_pipeline("multitask-qa-qg")

def generate_qna(long_text: str):
    return nlp(long_text)

def summary_using_t5(long_text: str):
  max_len = len(long_text.split(" "))
  return summarizer(long_text,  max_length = max_len)

