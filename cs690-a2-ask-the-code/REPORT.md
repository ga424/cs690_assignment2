# Assignment 2 Report: Ask the Code

Name: Gustavo Abreu
Provider and model: OpenAI, gpt-5.6-luna
Prices used (per million tokens, input and output), and the page you found them on:
$0.10 input / $0.50 output per 1M tokens, from the OpenAI pricing page for GPT-5.6-luna

## Table 1. Finding the right function

Table 1. Finding the right function

| Run | Right function in top 3 |
| --- | --- |
| retrieval_words | 5 of 9 |
| retrieval_meaning | 6 of 9 |

## Table 2. Answers

Table 2. Answers

| Run | Valid JSON | Right place | Correct (your marks) | Input tokens | Output tokens | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- |
| top3_words_five_part | 10 of 10 | 5 of 10 | 7 of 10 | 21,865 | 521 | 0.0024 |
| whole_five_part | 10 of 10 | 8 of 10 | 10 of 10 | 548,025 | 548 | 0.0551 |
| gold_five_part | 10 of 10 | 10 of 10 | 10 of 10 | 7,896 | 486 | 0.0010 |
| top3_words_minimal | 1 of 10 | 0 of 10 | 0 of 10 | 19,076 | 3,077 | 0.0034 |

## 1. Whose fault is it? (Step 5)

One row for every question marked `no` in top3_words_five_part. Take the first three
columns from Table 3 of `python -m askcode.summary`. Fault is retrieval, generation or
both, following the rule in Step 5. Evidence is one sentence about what you saw in the
reply or the retrieved functions.

| Question | Hit in top 3 | Correct with gold context | Fault | Evidence |
| --- | --- | --- | --- | --- |
| q03 | no | yes | retrieval | The right function was not in the top 3, and the answer explained the behavior using a redirect-header rule instead of the case-insensitive dict implementation. |
| q05 | no | yes | retrieval | The top-3 context did not include the JSON preparation function, so the model answered with a generic "not found" response instead of the actual serialization logic in PreparedRequest.prepare_body. |
| q07 | no | yes | retrieval | The top-3 context held extract_zipped_paths, HTTPAdapter.send and Response.__init__ but not SessionRedirectMixin.resolve_redirects, so the model answered "not found in the code shown" with null file and line instead of describing the TooManyRedirects guard. |

## 2. Paste everything or search? (Step 5)

Compare top3_words_five_part with whole_five_part: correct answers, input tokens and cost
for each, from Table 2. In two or three sentences: did pasting the whole codebase give
better answers, and was the difference worth the price?

Pasting the whole codebase gave a clear improvement: the top-3 words run got 7 of 10 correct, while the whole-corpus run got 10 of 10 correct. The tradeoff was cost: the whole run used 548,025 input tokens and cost $0.0551, versus 21,865 input tokens and $0.0024 for the top-3 run, so it is not worth it unless retrieval is clearly failing or a single missed answer is unacceptable.

## 3. Minimal prompt against five-part prompt (Step 6)

Which prompt did better on right place, and which on correct? Give both numbers for both
prompts. Name one question where the two prompts' replies differed, and say what
differed.

The five-part prompt did better on both metrics: it had 5 of 10 right place and 7 of 10 correct, while the minimal prompt had 0 of 10 right place and 0 of 10 correct, with only 1 of 10 valid JSON replies. One example of disagreement was q07: with the same top-3 code, which did not include `SessionRedirectMixin.resolve_redirects`, the five-part prompt answered "not found in the code shown" with null file and line, while the minimal prompt answered with a generic explanation from adapters.py that mentioned `redirect=False` but did not mention the actual `TooManyRedirects` guard.

## 4. Word search against meaning search (Step 7)

Name one question meaning search ranked higher than word search, and one question word
search ranked higher than meaning search, with the ranks from Table 4 of
`python -m askcode.summary`. If no such question exists, say so. In one sentence each,
say why you think each search won.

Meaning search ranked higher than word search on q07: words ranked it not in top 3, while meaning ranked it 1. I think meaning search won because the question is about redirect-loop prevention and the relevant code is expressed in terms of redirect counts and exceptions rather than the exact words "infinite redirect" or "too many redirects." Word search ranked higher than meaning search on q02: words ranked it 1 and meaning ranked it not in top 3. I think word search won because q02 is phrased around a literal `Location` header and url resolution behavior, which matches tokens and function names more directly than the embedding-driven semantic match.

## 5. Your decision rule (Step 8)

One rule for this codebase: when would you paste everything, and when would you search?
Cite the measured cost and the measured correct count of both designs.

For this codebase, I would use a top-3 search first because it is much cheaper and still strong: the top-3 words run achieved 7 of 10 correct at $0.0024, while the whole-corpus run achieved 10 of 10 correct but cost $0.0551, about 23x more. I would paste the whole codebase only when the retrieval step is clearly failing or the question is important enough that the extra cost is justified, because the accuracy gain from 7/10 to 10/10 is real but not worth the cost for routine use.
