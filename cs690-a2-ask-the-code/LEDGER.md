# Provenance Ledger

Write one entry per reviewable change or experiment, when the work is done. Use exactly
the schema in HANDOUT.md. Put the prompts you typed into AI tools in `prompts/` and name
the file in the entry's `prompts` field.

## Worked example (not graded; leave it here and add your entries under "My entries")

This shows the level of detail expected. The commit SHAs, dates and numbers are made up.

```
## Entry 2
artifact:  askcode/split.py at commit 3f2a9c1
tool:      GitHub Copilot Chat in VS Code, model Claude Haiku 4.5, 2026-09-22
prompts:   asked for an ast loop that returns methods with class-qualified names;
           prompts/split-01.md
review:    read every line; rejected its use of ast.walk, which also returned nested
           functions and broke rule 1; rewrote the loop over tree.body and class bodies
           myself; kept its decorator handling after checking it against rule 3
checks:    pytest tests/test_split.py: 8 passed
evidence:  HANDOUT Step 2, split.py docstring rules 1 to 6
risk:      I did not test a file with Windows line endings

## Entry 5
artifact:  results/top3_words_five_part.csv at commit 8d41e07
tool:      askcode run_eval, anthropic claude-haiku-4-5-20251001, 2026-09-23
prompts:   the five-part prompt in askcode/prompt.py at commit 8d41e07;
           prompts/five-part-v1.md
review:    read all ten replies and marked the correct column against questions.json
checks:    python -m askcode.run_eval --search words --context top3 --prompt five_part:
           valid JSON 10 of 10, right place 6 of 10
evidence:  HANDOUT Step 5
risk:      one run only; a fresh run may answer differently
dataset:   questions/questions.json at commit 51c0e2a; corpus requests v2.32.3
result:    correct 6 of 10, 24,113 input tokens; results/top3_words_five_part.csv
changed:   two misses were retrieval failures, so I looked at why word search missed
           them before touching the prompt
```

## My entries

## Entry 1
artifact:
tool:
prompts:
review:
checks:
evidence:
risk:

## Entry 2
artifact:  askcode/split.py at commit 311a190
tool:      Claude Code in VS Code with the agentic-sdlc plugin 0.3.3, model Claude Opus 5.5
           (claude-opus-5-5), 2026-10-12
prompts:   chose "pair programmer" AI help; asked Claude to draft split_file and
           split_corpus; prompts/split-01.md
review:    read every line of the AI draft against split.py rules 1 to 6; made no changes.
           [ga424: add in your own words what you checked and why you accepted it]
checks:    pytest tests/test_split.py: 8 passed (run by Claude Code, 2026-10-12);
           a throwaway script for rules the public tests do not check (async def, nested
           functions and classes, defs inside if/try/with, two decorators, empty file,
           subfolder sort order): all passed
evidence:  HANDOUT Step 2; split.py docstring rules 1 to 6
risk:      not tested on a file that starts with a UTF-8 byte order mark or on a file
           ast cannot parse

## Entry 3
artifact:  askcode/search_words.py at commit 762e664
tool:      Claude Code in VS Code with the agentic-sdlc plugin 0.3.3, model Claude Opus 5.5
           (claude-opus-5-5), 2026-10-12
prompts:   asked Claude to draft the next step, search_words; prompts/search-words-01.md
review:    [ga424: PENDING. Read every line against search_words.py steps 1 to 6; say
           what you changed or rejected, and whether you keep the k <= 0 guard, which the
           docstring does not ask for]
checks:    pytest tests/test_search_words.py: 7 passed (run by Claude Code, 2026-10-12);
           weights match HANDOUT Step 3: authorization log(230/8) = 3.36, self
           log(230/155) = 0.39; a throwaway script for rules the public tests do not check
           (word in every chunk weighs 0, empty chunks, repeated question word, k larger
           than matches): all passed
evidence:  HANDOUT Step 3; search_words.py docstring steps 1 to 6
risk:      order of weights in the sum is not fixed; relies on round(score, 6) to make
           ties exact, as the docstring says

## Entry 4
artifact:  askcode/prompt.py at commit 47e3902
tool:      Claude Code in VS Code with the agentic-sdlc plugin 0.3.3, model Claude Opus 5.5
           (claude-opus-5-5), 2026-10-12
prompts:   asked Claude to draft Step 4, build_prompt_five_part; prompts/step4-01.md
review:    [ga424: PENDING. Read the five parts against prompt.py requirements 1 to 6 and
           the Week 3 slides; say what you changed or rejected. Confirm the example
           (made-up numbers.py, add_one) is not one of your ten questions]
checks:    pytest tests/test_prompt.py: 7 passed (run by Claude Code, 2026-10-12);
           python -m askcode.run_eval --search words --context top3 --prompt five_part
           --dry-run: prompt printed, about 3,914 input tokens for the 2 example questions;
           a throwaway script checked the exact user layout and the empty-code case: passed
evidence:  HANDOUT Step 4 part A; prompt.py docstring requirements 1 to 6
risk:      the prompt has not been sent to a model yet, so whether it gets valid JSON and
           the "not found" reply in practice is unmeasured until Step 5

## Entry 5
artifact:  askcode/answer.py at commit bb68992
tool:      Claude Code in VS Code with the agentic-sdlc plugin 0.3.3, model Claude Opus 5.5
           (claude-opus-5-5), 2026-10-12
prompts:   asked Claude to draft Step 4, parse_reply; prompts/step4-01.md
review:    [ga424: PENDING. Read every check against answer.py rules 1 to 5; say what you
           changed or rejected. Decide whether file " " (spaces only) should be bad: the
           draft follows the rule's wording, "non-empty string", and accepts it]
checks:    pytest tests/test_answer.py: 15 passed (run by Claude Code, 2026-10-12);
           a throwaway script for cases the public tests do not check (bare ``` fence,
           unclosed fence, text outside a fence, JSON number/string/null, whitespace-only
           or non-string answer, empty or non-string file, negative or float line, null
           file with a line, 100,000 nested brackets, returns a new dict): all passed
evidence:  HANDOUT Step 4 part B; answer.py docstring rules 1 to 5
risk:      a fence line with extra words, such as ```python, is rejected; the docstring
           allows only ``` or ```json
