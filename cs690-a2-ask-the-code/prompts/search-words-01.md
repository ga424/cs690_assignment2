# search-words-01: Step 3, askcode/search_words.py

Tool: Claude Code in VS Code with the agentic-sdlc plugin 0.3.3, model Claude Opus 5.5 (claude-opus-5-5), 2026-10-12.

## Prompts, verbatim

1. `I've reviewed the split.py so let's draft it`
   (Claude Code took "it" to mean the next step and drafted `search_words`.)
2. `Please make sure to reflect the LEDGER.md from the internal sdlc so that we are keeping up with pace with everything that is being added as it's happening. I want to commit the changes per feature. Then let's proceed with step 4`

Claude Code drafted `search_words`, ran `pytest tests/test_search_words.py`, and ran a
throwaway script (outside the repo) for rules no public test checks and for the two
weights given in HANDOUT Step 3.
