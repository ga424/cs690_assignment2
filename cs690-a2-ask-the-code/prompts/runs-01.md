# runs-01: Steps 3, 5, 6 and 7, the six experiment runs

Tool: Claude Code in VS Code with the agentic-sdlc plugin 0.3.3, model Claude Opus 5.5 (claude-opus-5-5), 2026-10-12.
Claude Code typed the run_eval commands; the pipeline itself called OpenAI gpt-5.6-luna.

## Prompts I typed to Claude Code, verbatim

1. `I've added 10 questions required and now we can proceed with the checks and validation.  I think we already validated the key so we should be good`
2. `We are using openai and there is only one key here`
3. `I've looked up the prices of both and now we should be good to check which I also ran with check_setup and all checks passed.`
4. `yes, let's commit and run the four paid runs`

## Prompts the pipeline sent to the model

Not typed by me. The five-part prompt is built by askcode/prompt.py at commit 47e3902;
the minimal prompt by build_prompt_minimal in askcode/core.py (given code). Every reply
is saved in ai_replies/.
