# Scenario analysis — report template

Follow this structure. Keep the section order. Probabilities must sum to ~100% and every value needs its bridge shown. Add inline citations `[1]`, `[2]` immediately after claims, hyperlinked to the document URL.

---

```markdown
# Scenario Analysis: [Company Name] ([Ticker])
Spot price: [$X] | Report Date: [Date]

## Executive Summary
[2-3 sentences: the probability-weighted expected value, the expected return versus spot, and whether the distribution is skewed up or down.]

## Swing Variables
The scenarios turn on these; everything else is held roughly constant.

| # | Variable | Why it decides the outcome | Current consensus assumption |
|---|----------|----------------------------|------------------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Assumptions by Scenario

| Assumption | Bear | Base | Bull |
|------------|------|------|------|
| Revenue growth | | | |
| Operating margin | | | |
| [Swing variable 3] | | | |
| Exit multiple / terminal assumption | | | |
| [Other material input] | | | |

**Base vs consensus:** [Is the base case consensus? If it diverges, say where and why — that gap is itself a finding.]

## Scenario Values

### Bull — [X]% probability
- **Assumptions:** [The specific line items from above]
- **Bridge to value:** [Multiple applied to which earnings, or DCF inputs changed — show the arithmetic]
- **Value / price:** [$X]
- **Return vs spot:** [+X%]
- **Probability justification:** [One line, evidence-based]

### Base — [X]% probability
[Same structure]

### Bear — [X]% probability
[Same structure]

## Summary Table

| Scenario | Probability (%) | Key assumptions | Value / price | Return vs spot |
|----------|-----------------|-----------------|---------------|----------------|
| Bull | | | | |
| Base | | | | |
| Bear | | | | |
| **Total** | **~100%** | | | |

## Expected Value

**EV = (p_bull × V_bull) + (p_base × V_base) + (p_bear × V_bear)**

    EV = ([X]% × $[X]) + ([X]% × $[X]) + ([X]% × $[X]) = $[X]

- **Expected value:** $[X]
- **Expected return vs spot ($[X]):** [+/-X%]
- **Upside / downside ratio:** (bull − spot) / (spot − bear) = [X.Xx]
- **Distribution:** [Symmetric / skewed up / skewed down] — [what that means for the setup]

## What Moves Probability

| Development | Observable signal | Shifts weight toward |
|-------------|-------------------|----------------------|
| | | Bull / Base / Bear |
| | | |
| | | |

## Net Assessment
**Closing (structured):** Net assessment: [Positive/Negative/Neutral] because [specific]; key risk: [X]; next catalyst: [Y].

## Sources
  ALWAYS include a "Sources" section listing ALL documents referenced with:
   - Reference number matching the inline superscript number
   - Source name and publication date (MMM DD, YYYY) hyperlinked to the URL

   **Example:**
   [1] (NVIDIA Q3 2026 Earnings Call - Nov 19, 2025)[https://www.benzinga.com/node/...]
   [2] (Benzinga - Nov 20, 2025)[https://www.benzinga.com/node/...]

---

**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.
```

---

## Footer rule

The **Powered by Bigdata.com** line and the **Disclaimer** block above are mandatory and must be reproduced **verbatim**, after the Sources section, in every user-facing deliverable.
