# report-check-01: Step 8, checking REPORT.md, the marks and the ledger

Tool: Claude Code in VS Code with the agentic-sdlc plugin 0.3.3, model Claude Opus 5.5 (claude-opus-5-5), 2026-10-12.

## Prompts, verbatim

1. `I believe I'm done with the task to independently run the python -m askcode.summary task and reflect in the REPORT.md`
2. `great let's finish the ledger entry and close`

## What Claude Code did

Checked, without changing REPORT.md or the marks: that every row is marked; that only
the correct column changed in the four CSVs; that Tables 1 and 2 match
`python -m askcode.summary` row for row; that the section 1 fault labels follow the
Step 5 rule; and spot-checked three claims in the report against the CSVs. It found
problems only in ledger entry 1 (tool and prompts fields), which it corrected.
