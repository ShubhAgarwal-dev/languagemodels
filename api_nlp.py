import openai
openai.api_key = "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"

def get_answer(question:str, context:str):
    prompt = f"question:{question}\ncontext:{context}"
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=0.4,
    max_tokens=256
    )
    return response
    
if __name__ == "__main__":
    que = "What show that the latter are significantly better predictors of translated sentences than the former?"
    con = "We investigate the differences between language models compiled from original target-language\
    texts and those compiled from texts manually translated to the target language. Corroborating\
    established observations of Translation Studies, we demonstrate that the latter are significantly\
    better predictors of translated sentences than the former, and hence fit the reference set better.\
    Furthermore, translated texts yield better language models for statistical machine translation\
    than original texts."
    res = get_answer(que, con)
    print(res) 

