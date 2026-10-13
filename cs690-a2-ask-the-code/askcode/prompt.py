"""Step 4, part A: the five-part prompt from the Week 3 slides.

YOUR CODE. Read HANDOUT.md, Step 4, first.
Check your work with:  pytest tests/test_prompt.py
"""

from __future__ import annotations

from askcode.core import NO_CODE, Chunk, Prompt, format_chunk

# The stable part of every prompt: the same text for every question, so it goes first.
# The example question is about a made-up file, so it can never be one of the ten.
SYSTEM = """\
Goal: Answer a developer's question about the Python library requests, using only the code shown, and point to the line that proves the answer.

Inputs and outputs: The input is some source code from requests, then a question. Each piece of code starts with a header "### file, function, lines A to B", and every line of code starts with its line number. The output is one JSON object that answers the question and names the file and the line that support the answer.

Rules:
- Answer only from the code shown. Do not use anything else you know about requests.
- Write the file exactly as it appears in the header, and the line number exactly as it is printed at the start of the line.
- If the code shown does not answer the question, reply with the answer "not found in the code shown" and null for both file and line.
- Keep the answer to one or two sentences.

Example:
Question: What does add_one return when it is called with 2?
Reply: {"answer": "It returns 3, because add_one returns x + 1.", "file": "numbers.py", "line": 2}

Reply format: Reply with exactly one JSON object with the keys "answer" (a string), "file" (a string or null) and "line" (an integer or null). Write nothing before or after the object."""


def build_prompt_five_part(question: str, chunks: list[Chunk]) -> Prompt:
    """Build the prompt your pipeline sends to the AI.

    Requirements. The tests check each one.

    1. prompt.system holds the five parts from slide 6. Each part starts on its own
       line with its label, in this order:
           Goal:
           Inputs and outputs:
           Rules:
           Example:
           Reply format:
    2. Rules tell the model to answer only from the code shown, and, when that code
       does not answer the question, to reply with the answer
       "not found in the code shown" and null for both file and line.
    3. Example holds one sample question and its correct reply written as a JSON
       object with the keys "answer", "file" and "line". Do not use one of your own
       ten questions.
    4. Reply format asks for exactly one JSON object with the keys "answer" (a string),
       "file" (a string or null) and "line" (an integer or null), with nothing before
       or after it.
    5. prompt.system is the same text for every question and every set of chunks.
       It is the stable part of the prompt, so it goes first (slide 26).
    6. prompt.user is a line "Code:", then every chunk shown with format_chunk(chunk)
       in the order given, separated by blank lines, then a line "Question:", then
       the question. The question comes last. If chunks is empty, put NO_CODE under
       "Code:" instead.
    """
    code = "\n\n".join(format_chunk(c) for c in chunks) or NO_CODE
    user = f"Code:\n{code}\n\nQuestion:\n{question}"
    return Prompt(system=SYSTEM, user=user)
