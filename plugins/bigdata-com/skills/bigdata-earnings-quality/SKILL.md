---
name: bigdata-earnings-quality
description: >-
  Quality of earnings: accruals, cash conversion, EBITA rebuild, recurring one-offs, revenue
  recognition, flags by severity. Use for are earnings real, QoE, forensic accounting, red flags.
  Not one quarter: bigdata-earnings-recap.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, earnings-quality, roic
  bigdata-sector-primer: auto
---

# Earnings quality

A note on how much of a company's profit is backed by cash, how much will recur, whether it is fairly stated, and what earning power a valuation should therefore use, for someone who will act on it. Never an accusation and never a call on the stock. A flag is a question for the notes, set beside the company's own explanation. When the company is a counterparty or an acquisition target, the question becomes the cash it really generates or the earnings base a purchase price rests on, and the findings are drawn out for that. Size the work to the question: "is cash conversion healthy at Nike" gets the accrual series, cash from operations against net income and the working-capital lines, not the EBITA rebuild or the severity scale.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-earnings-quality"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts first,** in the user's order, each answered in full. The choices below apply where the question reaches them; a note that answers it with fewer tables and tests is the better note.
- **One accrual definition, the cash-flow form.** Net income minus cash from operations over average total assets, for every period and every peer, read on sign, trend and the peer median, because no fixed cut-off separates good from bad. Balance-sheet accruals are distorted by acquisitions, disposals and currency, so they are not used (`references/earnings-quality.md`, accrual ratio and cash conversion).
- **EBITA rebuilt from the notes, when the question is whether operating profit is fairly stated or a valuation rests on it.** From operating profit as published, add back only the amortisation of acquired intangibles; remove impairments, restructuring, litigation, asset-sale gains and pension gains, including those buried in cost of sales or SG&A; pair each gain with losses booked the same year or charged to equity. Each adjustment links to the note it came from (`references/earnings-quality.md`, rebuilding EBITA).
- **One-offs judged by recurrence.** A type of special item charged in two or more of the five years is an operating cost and goes in the forecast, because a charge that keeps coming back is part of running the business. The note states that cut-off once in plain words where it changes a figure; the count and size per type appear only where the reader needs to compare them (`references/earnings-quality.md`, recurring one-offs).
- **Reserve releases sized, when provisions moved.** Each provision classified and rolled forward in the working; the page carries the contribution of releases to EBITA in currency and as a percent of EBITA, and to any beat of consensus, because a beat made of releases does not recur (`references/earnings-quality.md`, provisions).
- **Stock compensation stays an expense.** It is already inside net income, so it is never added back and never deducted a second time in steady-state free cash flow; an add-back in the company's adjusted figures is removed (`references/earnings-quality.md`, steady-state free cash flow).
- **Tax tested three ways, not one; a test reaches the page when it finds a gap.** Tax-implied profit against pretax profit as published; the rate reconciliation item by item for one-off benefits and "one-time" items that recur; cash taxes against the book charge, with the deferred-tax change that explains the gap (`references/earnings-quality.md`, taxes).
- **Profit tested against the change in equity,** because charges made straight to equity show up here and nowhere else: the residual between the change in book equity and income, dividends, issuance and buybacks, as a percent of cumulative net income. It reaches the page when the residual is material; otherwise it stays in the working (`references/earnings-quality.md`, earnings-to-equity reconciliation).
- **Normalised earning power on the average, not the trend.** Over the five annual periods, nonrecurring items kept in the multi-year average; a trend is not used until its cause is shown; mid-cycle margins for a cyclical; the latest year placed in the range (`references/earnings-quality.md`, normalised earning power).
- **Returns on adjusted profit, only when the question reaches valuation.** NOPAT at the operating tax rate, ROIC with and without goodwill, before and after the lease and capitalised R&D adjustments, with a ROIC lifted by write-offs that shrink capital called out (`references/roic.md`, NOPAT, goodwill, leases and capitalised R&D).
- **Severity judged by what a flag does to the numbers.** From minor and explained, through flags that change adjusted EBITA or free cash flow and several flags pointing the same way, to evidence of misstatement, at which the figures cannot be adjusted and are not relied on. The overall judgment follows the most serious flag and grows more serious when two flags point the same way. It is stated as a plain sentence about what the numbers can be relied on for, with the flags behind it as evidence, never as a level, a grade or a bolded category, and never presented as an external standard (`references/earnings-quality.md`, red flags and severity).
- **Every flag that changes a figure mapped to the input it changes:** EBITA and NOPAT, invested capital and ROIC, free cash flow, debt-like claims in the equity bridge, or the earnings base for a multiple, each with the figure as published and as adjusted.
- **Special cases.** Banks and insurers: the accrual, EBITA and working-capital tests do not apply; the equity reconciliation, reserve adequacy and loan-loss provisioning do. Acquirers: organic and pro forma figures. Cross-border listings: local accounting against foreign peers. Loss-making companies: cash from operations and cash burn (`references/earnings-quality.md`, interpretation and limits).

## Where it goes wrong

- **Five accrual ratios from five years.** Each ratio needs the prior year's total assets, so five annual periods give four, plus the last twelve months.
- **Stock compensation added back, or deducted twice.** Both misstate free cash flow.
- **A fitted score or zones.** No manipulation score is computed, and Piotroski and Altman Z are quoted as the data set computes them, with no zones attached.
- **A vendor ROIC field and a hand-built ROIC in one comparison.** They differ in tax rate, goodwill and leases.
- **"Fraud" or "manipulation" in the note.** A filing or regulator may say it, cited; otherwise the note describes the figures, and the most serious finding is written as evidence of misstatement, which describes the numbers, not intent.
- **Citations assembled at the end.** Each adjustment carries the link to its note as it is captured.

## What the data has, and does not

Five fiscal years of annual statements, ratios and key metrics, the limit, so earning power through a longer cycle goes in Gaps; five quarters of statements, from which the last twelve months is the sum of the last four. The notes (special items, provisions, pensions, leases, tax, revenue policy, other comprehensive income, related parties) and the auditor's report come from the latest two annual filings read in full, each with its fiscal year fixed, so the policy wording can be compared year on year. Non-GAAP reconciliations come from each year's results releases; management's explanations from the last two calls; auditor changes, restatements, material weaknesses, late filings, dropped KPIs and short-seller research from news and filings over the window. Peers are pulled as a set in one batch for the peer medians. A private company carries different tearsheet content; the note uses what statements and filings exist and names the tests it could not run. Sector accounting traps are in `references/sector-primers.md`.

## Write

`references/output-standard.md` holds the rules. The title carries the finding in one line ("Half of Acme's operating profit growth came from reserve releases"). The opening gives how much of profit is backed by cash, the rebuilt EBITA against operating profit as published, the flags that matter and how far they let the numbers be relied on, and what the findings change in the earning power a valuation should use. The body follows the question: each flag with its value, period, the company's explanation and whether the numbers support it. What would change that judgment closes the note. Sub-headings state the finding, never the test that produced it.

## Before sending

- The user's parts are answered in the user's order, and every table on the page is one the reader needed.
- Every number in the opening agrees with the body, and every EBITA adjustment links to its note.
- Stock compensation is an expense throughout.
- The overall judgment follows from the flags and reads as a sentence with its evidence, never a level or a label, and each flag that changes a figure shows the published and adjusted figure.
- Every code name or internal term (a segment name, a non-GAAP measure) is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure is tagged with how it was obtained; no sentence describes how the note was made.
