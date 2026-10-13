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

## Later prompts, verbatim

2. `You are right let's do a final correction but in compliance with the framework and ensuring no actual evidence has been removed assuring integrity of the record`
   (Claude then added the corrections to entry 15 without changing entries 1 to 14.)
3. `I think that we should be good to close out based on the recommendations which I agree with.`
   Claude asked how to finish the four remaining pieces (the two REPORT.md q07 sentences
   and the review fields of entries 14 and 15). My answer: `You draft, I approve`.
4. `Approve - minor issues identified but important to clear the record and ensure accuracy`
   (My approval of Claude's drafts of the two REPORT.md sentences and the review fields
   of entries 14 and 15, which I read before approving.)

## How the first choices were carried out

To keep the record append-only, entry 5 was not rewritten: its correction is item 3 of
entry 15. The q08 note is item 9 of entry 15, not a change to an earlier risk field. The
first choice, `You write, I verify`, was replaced by `You draft, I approve` for the last
four pieces.
