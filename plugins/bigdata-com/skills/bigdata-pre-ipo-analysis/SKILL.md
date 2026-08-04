---
name: bigdata-pre-ipo-analysis
description: >
  Produce a balanced pre-IPO research note on an upcoming, not-yet-listed company using its
  S-1/F-1 plus Bigdata.com data. Covers deal structure (price range, shares, greenshoe, implied
  valuation, underwriters, lock-ups, share classes), two years plus interim financials, business
  model and funding history, TAM and listed comparables, IPO-window conditions, and 90-day
  sentiment — closing with bull and bear debates and watch points, never a participate/avoid
  call. Triggers: "analyze the IPO of X", "S-1 analysis", "upcoming listing for X", "IPO report
  on X", "should I look at X's IPO", "pre-IPO research on X", "X IPO valuation".
---

# Bigdata Pre-IPO Analysis

Institutional-style research note on an **upcoming** listing. Use Bigdata.com plugin tools plus web search for filings and market data.

**Use this skill when** the company has not yet priced. Not this skill when:

| Request | Use instead |
|---------|-------------|
| The company already listed and is trading | Post-IPO day 1 / 14 / 179 / 365 |
| An established public company's valuation | Valuation snapshot |
| A recommendation on whether to participate | Nothing — this deliverable is balanced by design |

## Scope rules (non-negotiable)

- **Upcoming IPOs only.** If the company has already listed, say this skill covers pre-listing analysis and offer a post-IPO note instead before proceeding.
- **Balanced framing only.** Never give a participate/wait/avoid recommendation, price target, or conviction rating. Present bull case, bear case, and watch points; let the reader decide.
- **No invented data.** If a figure (price range, offer size) is not yet public, write "not yet disclosed" rather than estimating. Label every third-party estimate as such.

## Data foundation (plugin tools + web)

| Tool | Purpose | Prerequisite |
|------|---------|--------------|
| `bigdata_search` | Company background, IPO window conditions, sentiment | None |
| `find_securities` | Entity resolution when a tearsheet is needed | None |
| `bigdata_company_tearsheet` | Financial baseline where the entity is covered | `find_securities` |
| Web search | S-1/F-1 terms, financials, comparables, recent debuts | None |

**Fallback:** if Bigdata.com tools are unavailable, complete every step with web search alone and note in the footer that sentiment data was limited to public news.

## Workflow

### Step 1 — Clarify the input

Company name is required. If ambiguous, confirm with the user. Note the expected exchange and geography if known.

### Step 2 — Research (complete BEFORE building the report)

Run searches in this order, one focus and one time period per search. Record source name and date for every material fact as you go.

**a. Filing facts (web).** Latest S-1/F-1/prospectus: price range, shares offered (primary vs secondary), greenshoe, implied valuation, underwriters, expected pricing and listing date, exchange, ticker, use of proceeds, lock-up terms, share-class structure, cornerstone investors.

**b. Financials (web + filing).** Two most recent fiscal years plus the latest interim period: revenue, gross margin, operating income/loss, net income, operating cash flow, FCF, cash and debt.

**c. Company background (`bigdata_search` + web).** Business model, segments, customers, management, funding history and last private-round valuation.

**d. Industry and peers (web).** TAM estimates, competitive set, and 3–6 listed comparables with current EV/Sales, EV/EBITDA, or P/E as applicable.

**e. IPO window (`bigdata_search` + web).** Current IPO market conditions, recent debuts in the same sector, and how they traded in the aftermarket.

**f. Sentiment (Bigdata.com).** News flow and sentiment on the issuer over the last 90 days.

### Step 3 — Build the report

Follow [assets/report-template.md](./assets/report-template.md). Do not start document generation until research is complete.

### Step 4 — Verify before delivering

- Every number traces to a recorded source
- Internal consistency: implied valuation = price × post-offering shares outstanding
- All template sections present
- No recommendation language slipped in ("we recommend", "attractive entry", "avoid")

## Output

- Length: 6–10 pages.
- Cover: company name, "Pre-IPO Research Note", date, "Prepared with Claude".
- Add inline citations `[1]`, `[2]` after every claim from a source, hyperlinked to the document URL. Brand Bigdata.com content exactly "Bigdata.com", linked to the `url` from the `bigdata_search` response.
- Full **Sources** section, then the **Powered by Bigdata.com** line and **Disclaimer**, verbatim.
- Default format is Markdown; offer PDF, Word (.docx), or presentation output.

## Quality bar

Non-negotiables in every pre-IPO note:

- Deal structure sourced from the filing, not from press summaries
- "Not yet disclosed" used wherever the filing is silent — never an estimate presented as fact
- Comparables named with their multiples, so the valuation framing is checkable
- Bull and bear both specific and falsifiable
- No participate/avoid call, no price target, no conviction rating
- Facts separated from analysis and implications
