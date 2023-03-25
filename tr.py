import torch
from transformers import AutoTokenizer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM 

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ROMANCE-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ROMANCE-en")


def translate(text):
    
    tokenized_text = tokenizer.prepare_seq2seq_batch([text], return_tensors='pt')

    # Perform translation and decode the output
    translation = model.generate(**tokenized_text)
    translated_text = tokenizer.batch_decode(translation, skip_special_tokens=True)[0]

    return {"trText":translated_text}
