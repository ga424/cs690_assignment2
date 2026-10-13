# step4-01: Step 4, askcode/prompt.py and askcode/answer.py

Tool: Claude Code in VS Code with the agentic-sdlc plugin 0.3.3, model Claude Opus 5.5 (claude-opus-5-5), 2026-10-12.

## Prompts, verbatim

1. `Please make sure to reflect the LEDGER.md from the internal sdlc so that we are keeping up with pace with everything that is being added as it's happening. I want to commit the changes per feature. Then let's proceed with step 4`

Claude Code drafted `build_prompt_five_part` (prompt.py) and `parse_reply` (answer.py),
ran `pytest tests/test_prompt.py tests/test_answer.py`, ran a throwaway script (outside
the repo) for rules no public test checks, and ran the free dry run
`python -m askcode.run_eval --search words --context top3 --prompt five_part --dry-run`
to show the real prompt. The example question in the prompt is about a made-up file
(numbers.py, add_one) so that it cannot match any of my ten questions.
