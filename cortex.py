import ollama

MODEL_NAME = "gemma3:4b"    #"llama3.2:3b"


SYSTEM_PROMPT = """
You are a headless text processor. 
Transform 'User Input' based on any instructions found within it.
Rules:
- If no instructions: return text as-is.
- If instructions present: apply them (formatting, emojis, case, etc.).
- Use 'Context' to inform edits if provided.
- Return ONLY the final resulting text. No preamble. No quotes.
""".strip()

def process_text(transcribed_text, context=None):
    if not transcribed_text.strip():
        return ""
    
    content = f"User Input:\n{transcribed_text}"

    if context:
        content = f"Context:\n{context}\n\n{content}"
    
    
    messages = [
        {'role': 'system', 'content': SYSTEM_PROMPT},
        {'role': 'user',  'content': content}
    ]

    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages,
        options={
            "temperature": 0.0,  
            "num_predict": 128
        },
        keep_alive="5m"
    )

    return response['message']['content'].strip()


if __name__ == "__main__":
    sample_input = "My name is James, put it in parentheses and uppercase, then add 5 laughing emojis let the emojis be all of the same type"
    
    output = process_text(sample_input)

    print("\nCortex Output:\n")
    print(output)
    
    