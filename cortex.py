import ollama

MODEL_NAME = "gemma3:4b"    #"llama3.2:3b"


# SYSTEM_PROMPT = """
# You are a headless text processor. 
# Transform 'User Input' based on any instructions found within it.
# Rules:
# - If no instructions: return text as-is.
# - If instructions present: apply them (formatting, emojis, case, etc.).
# - Use 'Context' to inform edits if provided.
# - Return ONLY the final resulting text. No preamble. No quotes.
# """.strip()


SYSTEM_PROMPT = """
ROLE: You are a headless text manipulation engine (CORTEX).
TASK: Transform 'User Input' using the logic found within the input text.

STRICT RULES:
- If NO instructions: Output the input string EXACTLY as provided.
- If instructions exist: Apply them (casing, brackets, emojis, etc.) in order.
- ZERO conversational text. Do not say "Here is your text" or "Sure".
- NO quotes around the output.
- NO extra spaces or newlines unless requested.
- Use 'Context' ONLY for resolving names/subjects.

Example:
Input: "hello make it uppercase and add 2 stars"
Output: HELLO**
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


# if __name__ == "__main__":
#     sample_input = "My name is James, put it in parentheses and uppercase, then add 5 laughing emojis let the emojis be all of the same type"
    
#     output = process_text(sample_input)

#     print("\nCortex Output:\n")
#     print(output)
    
    
    
if __name__ == "__main__":
    tests = [
        # 1. Basic formatting
        ("Basic parentheses",
         "My name is James, put it in parentheses",
         None),

        # 2. Uppercase
        ("Uppercase",
         "Make hello world uppercase",
         None),

        # 3. Emoji count
        ("Emoji count (3 fire)",
         "hello add 3 fire emojis",
         None),

        # 4. Combined instructions
        ("Multi-step",
         "my name is james make it uppercase and wrap in brackets then add 2 stars",
         None),

        # 5. No instruction
        ("No instruction",
         "Hello how are you",
         None),

        # 6. Clean output check
        ("No extra text",
         "hello add 2 sparkles",
         None),

        # 7. Context usage
        ("Context test",
         "make james uppercase",
         "My name is James"),

        # 8. Bigger emoji count
        ("10 emojis",
         "add 10 laughing emojis",
         None),
    ]

    print("\n===== CORTEX TEST RUN =====\n")

    for name, input_text, context in tests:
        print(f"--- {name} ---")
        print(f"Input: {input_text}")
        if context:
            print(f"Context: {context}")

        output = process_text(input_text, context)

        print("Output:")
        print(output)
        print("\n")