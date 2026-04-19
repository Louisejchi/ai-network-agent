from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

model_name = "google/flan-t5-large"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)

def analyze_network(data):
    prompt = f"""
You are a senior network engineer.

Analyze the following network logs:

{data}

Provide:
- Network status
- Issues
- Root cause
- Suggestions
"""

    result = pipe(prompt, max_length=512)
    return result[0]["generated_text"]
