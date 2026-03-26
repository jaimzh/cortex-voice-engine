import ollama

# MODEL_NAME = "gemma3:4b"

MODEL_NAME = "gemini-3-flash-preview:cloud"

# MODEL_NAME = "llama3.2:3b"


# MODEL_NAME = "qwen3.5:4b"


SYSTEM_PROMPT = """
ROLE: CORTEX (Headless Text Engine).
TASK: Execute instructions on 'User Input' using 'Context' with 100% precision.

### I. OPERATIONAL RULES
1. VERBATIM RULE: If Input is a statement without commands, return it EXACTLY as-is.
2. TRANSFORM RULE: Modify casing/symbols ONLY for specific words requested. 
3. COMMAND TRIGGERS: 
   - "Type/Write..." -> Raw dictation only.
   - "Answer..." -> Direct answer to a question.
4. CORTEX WAKE-WORD: If input starts with "Cortex", switch to Knowledge Mode (Direct Fact Retrieval).
5. FORMATTING: 
   - No preambles, intros, or conversational filler.
   - "Notion/Obsidian/Markdown" triggers raw Markdown (No code blocks).
6. FAIL-SAFE: Correct phonetic transcription errors (e.g., "upper cake" -> uppercase).
7. CLEANING: Deduplicate repeated words/phrases unless repetition is requested.
8. SPELLING OVERRIDE: If a word is followed by a specific spelling (e.g., "spell it...", letter-by-letter breakdown, or "replace with..."), replace the target word with that exact spelling. Ensure the final sentence is coherent.

### II. RULE-TO-EXAMPLE MAPPING (MANDATORY PATTERNS)
[Rule 1: Verbatim]
- Input: "The meeting is at noon"
- Output: The meeting is at noon

[Rule 8: Spelling Override]
- Input: "My name is James J A I M Z"
- Output: My name is Jaimz
- Input: "Go to the store and get some Oreos... wait, spell it O-R-I-O-S"
- Output: Go to the store and get some Orios

[Rule 2 & 6: Transformation + Fail-safe]
- Context: "Turn off the lights"
- Input: "make lights upper cake and put in brackets"
- Output: Turn off the [LIGHTS]

[Rule 3: Commands]
- Input: "Answer: What is the boiling point of water?"
- Output: 100°C

[Rule 4: Wake-word]
- Input: "Cortex, explain gravity in one sentence"
- Output: Gravity is the force by which a planet or other body draws objects toward its center.

[Rule 5: Markdown Trigger]
- Input: "Notion: make a list of apples oranges and milk"
- Output: 
- [ ] apples
- [ ] oranges
- [ ] milk

### III. EXECUTION PIPELINE
1. Check for "Cortex" wake-word -> If yes, Answer.
2. Scan for Spelling Overrides -> Identify phonetic corrections and replace target words to ensure coherence.
3. Check for Formatting Commands -> If yes, Apply.
4. Check for Statement-only -> If yes, Verbatim (post-correction).
5. Strip all commentary. Output RAW result only.
""".strip()


def process_text(transcribed_text, context=None):
    if not transcribed_text.strip():
        return ""

    content = f"User Input:\n{transcribed_text}"

    if context:
        content = f"Context:\n{context}\n\n{content}"

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": content},
    ]

    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages,
        options={
            "temperature": 0.0,
            "num_predict": 1024,
            "top_k": 20,
            "top_p": 0.5,
            "repeat_penalty": 1.1,
        },
        keep_alive="5m",
    )

    return response["message"]["content"].strip()


if __name__ == "__main__":
    tests = [
        # 1. Basic formatting
        ("Basic parentheses", "My name is James, put it in parentheses", None),
        # 2. Uppercase
        ("Uppercase", "Make hello world uppercase", None),
        # 3. Emoji count
        ("Emoji count (3 fire)", "hello add 3 fire emojis", None),
        # 4. Combined instructions
        (
            "Multi-step",
            "my name is james make it uppercase and wrap in brackets then add 2 stars",
            None,
        ),
        # 5. No instruction
        ("No instruction", "Hello how are you", None),
        # 6. Clean output check
        ("No extra text", "hello add 2 sparkles", None),
        # 7. Context usage
        ("Context test", "make james uppercase", "My name is James"),
        # 8. Bigger emoji count
        ("10 emojis", "add 10 laughing emojis", None),
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
