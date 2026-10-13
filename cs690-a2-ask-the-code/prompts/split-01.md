# split-01: Step 2, askcode/split.py

Tool: Claude Code in VS Code with the agentic-sdlc plugin 0.3.3, model Claude Opus 5.5 (claude-opus-5-5), 2026-10-12.

## Context (session summary)

Before this prompt, in the same session, I asked Claude Code to set up the agentic-sdlc
plugin, map the codebase (`/agentic-sdlc:knowledge-extract`) and write a requirements
list from the handout and docstrings (`/agentic-sdlc:requirements`). The requirements
list maps every docstring rule to the public test that checks it and marks the rules no
public test checks. None of that output is submitted; it lives in a local folder
(`.agentic-sdlc/`) that git ignores.

## Prompts, verbatim

1. `/agentic-sdlc:orchestrate`
2. Claude Code asked how much AI help I wanted on the graded code (reviewer only, tutor,
   pair programmer, or stop). My answer: `Pair programmer`
   (Claude drafts a function; I read every line, change or reject it, and log it.)

Claude Code then drafted `split_file` and `split_corpus`, ran `pytest tests/test_split.py`,
and ran a throwaway script (outside the repo) for rules no public test checks.

3. `I've reviewed the split.py so let's draft it`
