---
name: bigdata-credit
description: >-
  Credit analysis of a company: leverage, coverage, maturities, covenants, refinancing risk,
  agency ratios, recovery. Use for debt, credit quality, bankruptcy risk, counterparty or supplier
  checks. Not equity downside: bigdata-risk.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, credit, earnings-quality, capital-allocation
  bigdata-sector-primer: auto
---

# Credit

This skill writes the credit note a portfolio manager reads before owning a company's bonds, or before owning its equity when the balance sheet is the question: how stable the cash flow is, how much debt sits on it, whether the company can meet its maturities through a downturn and a closed market, what each layer of the capital structure recovers if it cannot, and what all of that means for a bondholder and for an equity holder. Credit risk is leverage times the instability of cash flow, so the note judges the business before it computes a ratio. It sizes to the question: "can they refinance the notes due next year?" gets the maturity table, the liquidity line and the coverage line, not the full note. It gives no rating of its own and no call on any security.

## Before starting

- If the Bigdata.com tools are not available in this conversation, say so and tell the user to connect the Bigdata.com connector and sign in. Give no figures, dates or view from memory or the web in the meantime, because an unsourced answer would look like Bigdata.com data.
- Pass `plugin_slug: "bigdata-credit"` on every Bigdata.com call that accepts it.
- Read `references/working-with-bigdata.md` before the first call: it maps each data need below to a tool, with fallbacks when a tool is not available, and the tools' own descriptions decide the arguments.
- Treat this skill as guidelines. Skip a step that does not apply, and research further where the task needs it.

## Scope the request

Resolve the company to its Bigdata.com entity, with its listing status taken from the lookup. Establish three things from the request: the claim the user cares about (a named bond or loan, senior unsecured debt in general, or the equity), the legal entity that owes it when the group has a holding company and operating subsidiaries, and the horizon (the next refinancing, the next downturn, or a stated date). Assume senior unsecured debt of the listed parent and a horizon through the next 24 months of maturities when the user does not say, and state both in the header.

Ask one question only if the answer changes the work: the user names a bond that the filings do not identify, or the group has several issuers and the user's claim could sit at more than one. Otherwise state the assumption and proceed.

If the company is a bank or an insurer, the leverage and coverage tests in this skill do not apply as written, because interest is an operating item and there is no net debt. Say so and run the bank variant: capital (CET1, leverage ratio), liquidity (LCR, loan-to-deposit, uninsured-deposit share), asset quality (NPL, coverage, charge-offs) and the rank of the claim (deposits, senior preferred, senior non-preferred or TLAC, Tier 2, AT1), with the metrics and ranges from the banks or insurance section of `references/sector-primers.md`; the note keeps the view, the maturities, the claims outside the debt line and the two holder paragraphs. If the lookup returns the company as Private, its numbers may be thin; work from filings and news and say which figures are missing.

## Gather

1. **The company's numbers.** The profile and five fiscal years of annual statements first (annual periods, since the default is quarters), then ratios, key metrics, consensus, dividends and the next report date. Done when five fiscal years of debt, leases, cash, current assets and liabilities, EBIT, EBITDA, interest expense, cash from operations, capex, depreciation, dividends, buybacks and issuance are in hand, with the market cap, net debt, Altman Z and Piotroski fields, consensus EBIT and EBITDA to the furthest year given, and the next report date. Five fiscal years is the most the tool returns; if the cycle is longer, say so in Gaps.
2. **Credit news signals.** The company's credit news signals over the monthly horizon: the strongest positive and negative credit-news catalysts (event type, score, direction). Done when the top catalysts are listed with their dates and direction for the distress-signals section. The signals carry no prices, yields or spreads; those come from step 4 or go in the Gaps line.
3. **The debt note and the credit agreement.** The latest annual filing and the latest quarterly filing, with the period fixed rather than inferred, each read in full for the debt, lease, pension, commitments and contingencies notes, and the liquidity section of MD&A. Search separately for the credit agreement or its amendments (an 8-K exhibit or a news item). Done when every instrument has an amount, a coupon or margin, a maturity date, a rank and an obligor; the fixed-floating split and hedges are noted; the guarantor group and the share of EBITDA and assets outside it are noted where the filing gives them; covenant terms, baskets and current headroom are quoted where disclosed; undrawn facilities and their expiry are listed; leases, the pension deficit, guarantees, receivables sold or factored and deconsolidated entities are each found or marked not found.
4. **Rating actions, market access and quoted yields.** A search for rating agency actions on the company over the last two years, a second search for new issuance, tenders, exchange offers, amend-and-extend deals and drawn revolvers, and a third for the yield or spread at which the company's bonds have been quoted or issued. Done when the latest reported rating from each agency is dated with its source, or the note says none was found, each recent financing event is dated, and a quoted yield or spread is dated with its source or marked not found.
5. **What management says.** The full transcript of the last earnings call, with the period fixed rather than inferred. Done when the stated leverage target, the refinancing plan, the capital allocation priorities and any comment on covenants or ratings are quoted verbatim with the date.
6. **Peers, when the comparison matters.** Annual statements, ratios and key metrics for three to six named peers (from the company profile's competitors block or the user), pulled as a set rather than one company at a time where the account allows. The credit-news ranking across companies scores news, not ratios, so it only says which peers carry the worst news. Done when the company's coverage and leverage sit next to a peer median built the same way.
7. **Sector primer.** Find the company's sector in `references/sector-primers.md` (grep the slug from its contents list, read to the next `## ` heading) for how the sector's statements differ and which leverage measure the sector uses. Done when the sector's leverage measure is noted, or its absence is stated.

## Analyse

Steps 1 to 10 follow `references/credit.md`, which carries the formulas, the rating tables and the distress list. Load it before step 1.

1. **Fix the claim.** Name the security, its rank (senior secured, senior unsecured, subordinated, preferred, common) and the legal entity that owes it, from the debt note. Holding-company debt can default while operating subsidiaries carry on, so state the guarantor coverage (share of EBITDA and assets inside the guarantor group) and any covenant baskets that let collateral or assets move away from existing lenders. Done when the obligor, the rank, the guarantor coverage and the baskets are stated with the source, or marked not disclosed.

2. **Judge the stability of the business.** The five-year EBITDA range and its worst year, the sector's EBITDA volatility from table 5 of `references/credit.md` (labelled with its source and period, historical), and one paragraph on what drives the variability: demand, pricing, input costs, contract length, customer concentration. A stable record is not proof of a stable business. Done when the note says how much cash flow the debt can lean on in a bad year and why.

3. **Check that the EBITDA is real.** From `references/earnings-quality.md`, run step 2 (accrual ratio and cash from operations against net income), step 4 (one-off charges that recur, counted by years) and step 6 (pensions, leases, stock compensation, receivables sold) on the five years. Credit ratios built on EBITDA that excludes recurring charges or includes sold receivables overstate capacity. Done when the EBITDA used in the ratios is either the reported figure or an adjusted figure with each adjustment cited.

4. **Leverage and coverage.** Formulas 1 to 5 of `references/credit.md`, all on the same period: EBIT, EBITA and EBITDA over total interest (never cash interest only); EBITDAR over interest plus rent for lessees; adjusted debt over EBITDA and FFO over adjusted debt as table 3 defines them; net debt over EBITDA with leases and excess cash treated as the file sets out; free cash flow over total debt; the market value of equity over funded debt. Done when each ratio shows its numerator, denominator and period, for each of the five years and the latest twelve months.

5. **Against the rating tables.** Place FFO over debt and debt over EBITDA on table 3 of `references/credit.md` (the agency's cash-flow and leverage ranges) first; then EBIT over interest and debt over total capital on table 1 (S&P medians of three-year averages, 2011 to 2013, US companies) as the cross-check; then the five-year default probabilities in table 2 (S&P, 1981 to 2003, order of magnitude only). State the implied bucket on each measure separately, labelled derived, next to the actual rating from step 4 of Gather, and say when the tables disagree. Done when the note says whether the reported rating sits above, at or below what the ratios imply, and every table carries its source and period.

6. **The stress test, earnings and refinancing.** Cut EBIT by an assumed shock and recompute coverage (formula 6), with a shock at least as large as the worst year in the window or the sector's volatility, and a second, harsher case. Then formula 6a: re-price the maturities within 24 months and the floating-rate share at the yield from step 4 of Gather (or an assumed yield for the rating, labelled), recompute interest, coverage and FCF over debt, alone and combined with the EBIT shock. Done when coverage after each case is shown against the level the rating bucket needs, with every shock labelled assumed and its basis stated.

7. **The maturity wall and liquidity.** Every maturity in the next 24 months with its amount, date and funding source (cash, free cash flow, an undrawn facility, or refinancing), then the full ladder by year beyond that. Short-term bank debt and notes payable, the current and quick ratios, undrawn facilities and their own expiry, and covenant headroom where disclosed. Done when the note states whether repayment depends on market access and how much free cash flow covers before the company needs a market.

8. **Claims outside the debt line.** Leases, the after-tax pension deficit, contingent liabilities, guarantees, deconsolidated entities, sold receivables and related-party loans, each present with an amount, absent, or unknown. Run the balance-sheet checks in step 7 of `references/credit.md`: goodwill share of equity, PP&E growth against revenue growth, a shift from short-term to long-term debt, deconsolidations. Done when each item has a status and a source.

9. **Cash flow and what it is spent on.** Free cash flow per year (formula 7: cash from operations less capex, the agency convention, with stock compensation left as the non-cash add-back it is and said so), capex against depreciation, and dividends and buybacks against free cash flow. From step 9 of `references/capital-allocation.md`, check whether payouts were financed by borrowing; from step 1, build the short sources-and-uses table if the debt grew. Done when the note says whether shareholder payouts have been competing with debt reduction, with the years and amounts.

10. **Distress signals.** Run the list under "Distress signals" in `references/credit.md` item by item: short-term bank debt rising, large maturities within 24 months, coverage below 1.0, debt above tangible assets, receivables and inventories building while cash falls, dividends held while free cash flow is weak, PIK or interest-reset features, new yield measures, an equity collapse raising market leverage, related-party or off-balance-sheet loans, interim reporting dropped. Quote the Altman Z and Piotroski fields as FactSet reports them, with no zones attached, since the sources give no cutoffs, and list the credit-news catalysts from step 2 of Gather with their dates. Done when each signal is marked present, absent or unknown with its evidence.

11. **Recovery, for stressed cases only.** When coverage is near or below the level a B rating implies, maturities exceed liquidity, or two or more distress signals are present, run step 9 of `references/credit.md`: split the ongoing business from assets available for distribution, value the business at two or more stated enterprise values, list claims by seniority at face value, compute recovery per layer (formula 9) and name the fulcrum security. Done when each layer has a recovery in each scenario, and the enterprise values are labelled assumed with their basis.

12. **Do the layers agree?** If step 4 of Gather found a dated quoted price or yield for a bond, compute the enterprise value that layer implies (formula 10) and compare it with the value the equity implies. Done when the implied values are shown, or the missing prices are named in the Gaps line.

13. **What it means for each holder.** For a bondholder: the gain is capped at the promised yield and the loss can be total, so the question is the likelihood of payment through the next maturity and the recovery if not; name what protects the claim (rank, security, covenants, the equity cushion beneath it) and what erodes it. For an equity holder: from the leverage identity (formula 5), how much leverage adds to the return on equity and to its sensitivity; whether a refinancing, a covenant or a rating cut could force a dilutive raise, a dividend cut or asset sales; and whether the equity is a claim on a going concern or, in a stressed case, an option on the enterprise value exceeding the debt. Done when each holder gets one paragraph with the two or three facts that decide it.

Special cases. Cyclicals: use mid-cycle EBITDA and the sector volatility row, and say where in the cycle the latest year sits. Loss-making companies: coverage on a deficit is meaningless; state the cash burn and the runway as derived and the funding assumption as assumed, since the sources give no runway method. High inflation: use EBITDA over interest. REITs: use the leverage tests in the REIT section of `references/sector-primers.md` (net debt to EBITDA, fixed-charge coverage, unencumbered assets) and the filings' own covenant definitions. Project finance and securitisation vehicles are outside the sources; say so and work from the filings' own covenant definitions.

## Write

Follow `references/output-standard.md`. The note:

```
# <Company> (<ticker>) credit: <claim analysed>, <date>
Data as of: statements <period>; estimates <date>; newest filing <date>; ratings <date>.

## The view
Four to eight sentences: how stable the cash flow is, the leverage and coverage on it, whether the
next 24 months of maturities are covered without the market, where the ratios sit against the rating
medians, the stress result, and what it means for a bondholder and for an equity holder. No rating
of the note's own, no call on the securities.

## Business stability
EBITDA range and worst year, the sector volatility row with its label, and the drivers.

## Leverage and coverage
| Measure | FY-4 | FY-3 | FY-2 | FY-1 | FY0 | LTM | Basis | Source |
Rows: net debt, EBITDA used (reported or adjusted), EBIT / interest, EBITDA / interest,
EBITDAR / (interest + rent) where relevant, net debt / EBITDA, FCF / debt, equity value / funded debt.
A note under the table names any EBITDA adjustment and its source.

## Against the rating tables
| Measure | Company | Implied bucket | Range or median for reported rating | Table and period | Basis | Source |
Then the reported rating(s) with dates, and one sentence on the gap.

## Stress test
| Case | EBIT shock | Refinancing yield | Coverage after | FCF / debt after | Level needed for bucket | Basis |
Cases: EBIT shock alone, refinancing alone, both; a note under the table carries the sources.

## Maturities and liquidity
| Instrument | Obligor | Rank | Amount | Coupon and fixed or floating | Maturity | Funding source | Source |
A note under the table carries the basis (reported from the debt note unless marked) and the guarantor coverage.
Cash, undrawn facilities and their expiry, covenant terms and headroom, current and quick ratios.
One sentence on dependence on market access.

## Claims outside the debt line
| Item | Amount | Status | Basis | Source |

## Cash flow and payouts
Free cash flow, capex against depreciation, dividends and buybacks against free cash flow, by year.

## Distress signals
| Signal | Present / absent / unknown | Evidence | Basis | Source |
Altman Z and Piotroski as reported by FactSet.

## Recovery (stressed cases only)
| Layer | Claim at face | Recovery at EV A | Recovery at EV B | Basis | Source |
The fulcrum security; the layer comparison if prices exist.

## For a bondholder / For an equity holder
One paragraph each.

## What would change this reading
Two to five dated or observable conditions: a maturity, a covenant test date, a rating review,
an EBITDA level that breaks a coverage threshold.

## Gaps
Bond prices, yields and spreads are not in a Bigdata.com data set: say whether a quoted figure was found; covenant terms not disclosed; anything else.

## Sources
Numbered sources, the Data line, then the footer verbatim.
```

Length: two to four pages. A narrow question gets its step in the method with the relevant table and the sources, and keeps the footer.

## Checks before sending

1. The claim, its rank and its obligor are named, and every ratio refers to that claim's perspective.
2. Coverage uses total interest, and every ratio shows numerator, denominator and period.
3. Every rating table is labelled with its source and period (S&P 2013 criteria ranges, 2011 to 2013 medians, 1981 to 2003 default rates) and described as historical, and the implied bucket is labelled derived.
4. The EBIT shock and the refinancing yield are labelled assumed, with their basis; the shock is at least as large as the worst year or the sector volatility.
5. Each maturity in the next 24 months has an amount, a date and a funding source, from a cited filing.
6. Covenant headroom is quoted from a filing or marked not disclosed; it is never estimated silently.
7. Altman Z and Piotroski are quoted as reported, with no zones.
8. Both holders get their paragraph, and neither paragraph recommends buying, selling or holding a security.
9. Every figure has a Basis label and a source number, or appears in the Gaps line.
10. Bond prices, yields and spreads appear only with the dated document they were quoted from, never from memory.

## Hand-offs

- The user wants the equity downside more broadly (floors, the risks ranked): `bigdata-risk`.
- A corporate user asking whether to refinance, term out or de-lever gets the maturity table, the two stress cases and the trade-offs of each option side by side; that is a corporate decision, not a securities call.
- The question is how management allocates capital, not the debt: `bigdata-capital-allocation`. Whether the earnings behind the EBITDA are real: `bigdata-earnings-quality`.
- The company is in a restructuring, an exchange offer or bankruptcy and the user wants the payoff of a security: `bigdata-special-situations`.
- After delivering, make one offer: a monitor on the company's filings, rating actions and refinancing news until the next maturity. Act only on a clear yes.
