# setup-01: Step 0 setup, environment and planning

Tool: Claude Code in VS Code with the agentic-sdlc plugin 0.3.3, model Claude Opus 5.5 (claude-opus-5-5), 2026-10-12.

## What Claude Code did

- Showed the installed plugin version and configuration.
- Set up a local planning folder (`.agentic-sdlc/`, ignored by git, not submitted),
  mapped the codebase, and wrote a requirements list from HANDOUT.md and the docstrings.
- Deleted two virtual environments on Python 3.14 (unsupported), and later rebuilt
  `.venv` on Python 3.12.12 after `pip install -r requirements.txt` failed because the
  old `.venv` mixed Python 3.12 and 3.14.
- Ran `python -m askcode.check_setup --skip-ai`: All checks passed.
- Explained the rest of the assignment using the two example questions and the given
  code only.

## Prompts, verbatim

1. `perfect - let's check in which version of the aise plugin we have`
2. `perfect let's begin by viewing a summary of the current model configuration etc that we have installed and agents/skills, etc.`
3. `what's the best way to get started with the agentic-sdlc`
4. `/agentic-sdlc:init`
5. `/agentic-sdlc:knowledge-extract`
6. `Answer 1. keep it local 2. we will use the Opus 5.5, I think the regulated data and state controsl are to be marked not applicable here. 4. Yes please delete the incompatible virtual envs - I'm assuming the grader will indeed run hidden tests`
7. `Yes, let's first write the 10 questions (if this is not requried to be written by AI, please do not enter in ledger)`
   (Claude Code explained that any AI help on the questions must be logged; I wrote the
   ten questions myself.)
8. `Let's maintain academic integrity at all times`
9. `ok let's say we go with the existing questions 2 of them let's try to see the rest of the process`
10. A paste of my terminal output. The command and the error lines, verbatim:
    ```
    (.venv) ➜  cs690-a2-ask-the-code git:(main) pip install -r requirements.txt
    ...
    ERROR: Could not find a version that satisfies the requirement onnxruntime>=1.24.2; python_version >= "3.14" (from fastembed) (from versions: none)
    ERROR: No matching distribution found for onnxruntime>=1.24.2; python_version >= "3.14"
    ```
11. `what are the hidden tests?`
12. `/agentic-sdlc:requirements`

Later I changed the provider plan from Anthropic to OpenAI (prompts/runs-01.md, prompt 2).
