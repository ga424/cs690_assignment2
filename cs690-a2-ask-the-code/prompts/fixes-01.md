# fixes-01: correcting REPORT.md and LEDGER.md after the review

Tool: Claude Code in VS Code with the agentic-sdlc plugin 0.3.3, model Claude Opus 5.5 (claude-opus-5-5), 2026-10-12.

## Prompts, verbatim

1. `I would like to now work on the fixes for these items identified and then reflect the changes we've been able to make to correct the record`

Claude Code then asked four questions. My answers:

- How should the false statements in REPORT.md and LEDGER.md be corrected?
  `You write, I verify`: I write the corrected text; Claude shows what the data says and
  checks my text against the results files and git history.
- Ledger entry 5 says a file value of " " should be rejected, but answer.py accepts it.
  `Keep code, fix entry`: answer.py stays as committed; I correct entry 5.
- q08's expected answer describes prepare_url, not the function I named.
  `Note it in the ledger`: I add a note to the risk field.
- The local planning folder (not submitted) has bookkeeping errors.
  `Correct my errors only`: Claude fixes its own records; nothing is approved on my behalf.

Later prompts in this correction are added below when Claude checks the corrected text.
