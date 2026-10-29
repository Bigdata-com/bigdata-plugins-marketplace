---
name: bigdata-credit
description: >-
  Credit analysis of a company: leverage, coverage, maturities, covenants, refinancing risk,
  agency ratios, recovery. Use for debt, credit quality, bankruptcy risk, counterparty or supplier
  checks. Not equity downside: bigdata-risk.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, credit, earnings-quality
  bigdata-sector-primer: auto
---

# Credit

Never a rating of its own and never a call on any security: how stable the cash flow is, how much debt sits on it, whether the company meets its maturities through a downturn and a closed market, what each layer recovers if it does not, and what that means for a bondholder and for an equity holder. Two readers ask different questions: a supplier or customer checking a counterparty asks how likely payment is over its own exposure horizon, and a treasury team deciding whether to refinance, term out or de-lever needs the maturity table, the stress cases and each option's arithmetic side by side. Size the work to the question: "can they refinance the notes due next year" gets the maturities, the liquidity and the coverage after a refinancing at today's yield, not the recovery analysis.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-credit"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts first.** The parts the user asked for come first, in the user's order, each answered in full; the choices below apply where the question reaches them, and a note that answers the question with fewer tables and pieces is the better note.
- **The claim and its obligor first.** Name the security, its rank and the legal entity that owes it, with the guarantor group's share of EBITDA and assets and any covenant baskets that let assets or collateral move away from existing lenders, because holding-company debt can default while the operating subsidiaries carry on. Without a named claim, take senior unsecured debt of the listed parent and the next 24 months of maturities, and the note says which claim it covers (`references/credit.md`, the claim and its obligor).
- **The business before the ratios.** Credit risk is leverage times the instability of cash flow, so the five-year EBITDA range, its worst year, the sector's EBITDA volatility and what drives the variability come before any ratio. A stable record is not proof of a stable business (`references/credit.md`, stability of the business).
- **EBITDA checked before it is used.** Accruals against cash, one-off charges that recur, pensions, leases, stock compensation and receivables sold, because ratios on EBITDA that excludes recurring charges or includes sold receivables overstate capacity (`references/earnings-quality.md`, accrual ratio and cash conversion; recurring one-offs; pensions, leases, R&D, stock compensation, sold receivables).
- **The debt once, from the latest filing.** The inputs appear once on the page (the instruments that matter with their rank, amount and maturity, leases, the after-tax pension deficit, cash and the net figure) so the reader can rebuild every ratio, and every ratio, stress and recovery figure later in the note uses them.
- **The agency's ranges first, the medians second.** Funds from operations to adjusted debt and debt to EBITDA on the agency's cash-flow and leverage ranges, then EBIT to total interest and debt to capital on the rating medians as a cross-check. Where these place the company against its published rating is a plain sentence, with any disagreement stated. Default rates give the order of magnitude only, and appear only where they change the reading (`references/credit.md`, placing the company on the rating scales; coverage and leverage ratios).
- **Two stresses, and both together, when the question is whether the company meets its obligations through a downturn.** An EBIT shock at least as large as the worst year in the window or the sector volatility; a refinancing stress that re-prices every maturity within 24 months and the floating-rate share at a quoted current yield; then both combined. The size of each shock is stated once in plain words where the result is given (`references/credit.md`, coverage stress and refinancing stress).
- **Every near maturity with a funding source, when the question reaches liquidity or refinancing.** Each maturity in the next 24 months with its amount, date and source (cash, free cash flow, an undrawn facility with its own expiry, or the market), then the ladder beyond; the note says how much free cash flow covers before the company needs a market (`references/credit.md`, liquidity and the maturity wall).
- **Claims outside the debt line, searched one by one.** Leases, the after-tax pension deficit, guarantees, contingencies, deconsolidated entities, sold receivables and related-party loans. Those found go into the debt figure with their amount; those that could not be checked are named in one line; the rest stay in the working (`references/credit.md`, claims outside the debt line and cash flow).
- **The distress signals run item by item in the working.** The note names the signals present, each with its evidence in a sentence, and in one line those that could not be checked, never a present, absent or unknown label per item; the dated credit-news catalysts that bear on the question go beside them (`references/credit.md`, distress signals).
- **Recovery only when stressed.** When coverage is near the level a B rating implies, maturities exceed liquidity, or two distress signals are present: the business valued at two or more enterprise values, each with the EBITDA and multiple behind it stated once, claims at face by seniority from the debt figures above, recovery per layer, and the security that sits where value runs out named. Where a bond price is quoted, the enterprise value that layer implies is set against the equity's (`references/credit.md`, recovery by layer; comparing the layers).
- **Each holder separately, where the question reaches them.** A bondholder's gain is capped at the promised yield and the loss can be total, so the question is payment through the next maturity and recovery if not. An equity holder's question is how much leverage adds to the return and its sensitivity, whether a refinancing, covenant or rating cut could force a dilutive raise, a dividend cut or asset sales, and whether the equity is an option on value above the debt. Each is answered with the two or three facts that decide it.
- **Special cases.** Banks and insurers: interest is an operating item and there is no net debt, so the note runs on capital, liquidity, asset quality and the rank of the claim, with the metrics from the sector primer. Cyclicals: mid-cycle EBITDA. Loss-making companies: cash burn and runway against maturities, with the funding the runway rests on stated once. High inflation: EBITDA to interest. REITs: the primer's leverage tests and the filings' covenant definitions. Project finance and securitisations: these ratios do not apply as written; say so (`references/credit.md`, where the method changes).

## Where it goes wrong

- **A total that does not add from its own inputs.** A liquidity or sources line is re-added from the rows beneath it before it goes in the opening.
- **Coverage on cash interest only.** It flatters companies with PIK or low-coupon debt that will reprice; coverage uses total interest.
- **Covenant headroom estimated.** Definitions in the credit agreement differ from the published figures; headroom is quoted from a filing or the note says it is not disclosed.
- **Altman Z or Piotroski read against zones.** The data set's definitions are not documented; quote the fields as given, with no cut-offs of your own.
- **Rating medians and default rates quoted as current.** They are historical; each carries its population and period in the sentence.
- **A yield or spread from memory.** It appears only with the dated document it was quoted in.
- **The decision buried.** For a refinancing question, the maturities and the stress result carry the decision and come first.
- **Citations assembled at the end.** The link goes next to each instrument and covenant as it is taken from the debt note.

## What the data has, and does not

Five fiscal years of annual statements, ratios and key metrics, five periods being the limit, so a longer cycle is a gap the note names; consensus EBIT and EBITDA up to four years out as a snapshot with its date. The debt, lease, pension and contingency notes, the guarantor note and the liquidity discussion come from the latest annual and quarterly filings read in full with the period fixed; the credit agreement and its amendments from a separate search. Rating actions, new issues, tenders, exchanges and drawn revolvers come from news, dated. The credit tools give news-catalyst scores (event type, score, direction) for one company or a ranking across many, not prices, yields, spreads or ratios, so a peer ranking from them says which peers carry the worst news, nothing more. There is no structured field for bond prices, yields or spreads; news, research and filings often carry them, so search before stating a gap, and a refinancing yield is either a dated quote or one stated figure for the rating. The corporate calendar carries the next earnings date; covenant test dates, rating reviews and maturities come from the filings. Peers are pulled as a set in one batch. A private company's numbers may be thin; the note works from filings and news and names what is missing. Sector leverage measures and the bank and insurer metrics are in `references/sector-primers.md`.

## Write

`references/output-standard.md` holds the rules. The title carries the finding in one line ("Cable One covers its 2026 maturities from cash flow; the 2028 wall needs the market"). The opening answers the question first: how stable the cash flow is, the leverage and coverage on it, whether the next 24 months of maturities are covered without the market, the stress result, and what it means for a bondholder and for an equity holder, as far as the question asks; for a counterparty check, the likelihood of payment over their horizon instead. The body follows the question, the user's parts in the user's order. Dated conditions close the note: a maturity, a covenant test, a rating review, the EBITDA level that breaks a coverage threshold. Sub-headings state the finding ("Coverage falls to 2.1 times if the 2026 notes reprice"), never the step.

## Before sending

- The user's parts are answered in the user's order, each findable by its name, and every table on the page is one the reader needed.
- The claim, its rank and its obligor are named, and every ratio is from that claim's perspective, on total interest, with numerator, denominator and period.
- Every maturity in the next 24 months that the question reaches has an amount, a date and a funding source from a cited filing.
- Every number in the opening agrees with its table, every total adds from its own rows, every ratio and recovery figure can be rebuilt from the inputs stated once, and the net debt is the same figure everywhere.
- No signal, claim or rating placement appears as a label or a bolded category; each is a sentence with its evidence.
- Every instrument nickname or contract term (a basket, a springing maturity) is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure is tagged with how it was obtained; no sentence describes how the note was made.
