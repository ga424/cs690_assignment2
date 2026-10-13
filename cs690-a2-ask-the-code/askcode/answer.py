"""Step 4, part B: check the AI's reply before your program trusts it.

YOUR CODE. Read HANDOUT.md, Step 4, first.
Check your work with:  pytest tests/test_answer.py
"""

from __future__ import annotations

import json

from askcode.core import BadReply


def parse_reply(text: str) -> dict:
    """Check the model's reply and return {"answer": ..., "file": ..., "line": ...}.

    Accept the reply only if every rule holds. Otherwise raise BadReply with a short
    message that says which rule failed. Never let a different exception escape.

    1. After stripping whitespace, the reply is one JSON object. The only thing
       allowed around it is a single Markdown code fence: a first line of ``` or
       ```json, and a last line of ```. Any other text before or after the object
       makes the reply bad.
    2. The object has exactly the keys "answer", "file" and "line": none missing,
       none extra.
    3. "answer" is a string that is not empty or only whitespace.
    4. "file" is a non-empty string or null. "line" is an integer or null; true and
       false do not count as integers, and an integer line must be at least 1.
    5. "file" and "line" are both null, or both set.

    Return a new dict with exactly the three keys and the values from the reply.
    """
    if not isinstance(text, str):
        raise BadReply("rule 1: the reply is not text")
    body = text.strip()
    lines = body.split("\n")
    if lines[0].strip() in ("```", "```json"):
        if len(lines) < 2 or lines[-1].strip() != "```":
            raise BadReply("rule 1: the code fence is not closed on the last line")
        body = "\n".join(lines[1:-1]).strip()

    try:
        data = json.loads(body)
    except (ValueError, RecursionError) as exc:
        raise BadReply(f"rule 1: the reply is not one JSON object ({exc})") from None
    if not isinstance(data, dict):
        raise BadReply("rule 1: the reply is JSON but not an object")

    if set(data) != {"answer", "file", "line"}:
        raise BadReply(f"rule 2: the keys must be answer, file and line, not {sorted(data)}")

    answer, file, line = data["answer"], data["file"], data["line"]
    if not isinstance(answer, str) or not answer.strip():
        raise BadReply("rule 3: answer must be a non-empty string")
    if file is not None and (not isinstance(file, str) or file == ""):
        raise BadReply("rule 4: file must be a non-empty string or null")
    if line is not None and (isinstance(line, bool) or not isinstance(line, int) or line < 1):
        raise BadReply("rule 4: line must be an integer of at least 1, or null")
    if (file is None) != (line is None):
        raise BadReply("rule 5: file and line must both be null or both be set")

    return {"answer": answer, "file": file, "line": line}
