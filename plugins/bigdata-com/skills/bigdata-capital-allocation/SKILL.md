---
name: bigdata-capital-allocation
description: >-
  Capital allocation review: buybacks, dividends, reinvestment and acquisitions, and whether each
  created value. Use for payout policy, buyback vs dividend, M&A record, incentives. Not one
  announced deal: bigdata-deal-analysis.
metadata:
  bigdata-refs: working-with-bigdata, output-standard, capital-allocation, expectations, roic, credit, valuation
  bigdata-sector-primer: auto
---

# Capital allocation

Never a composite score, a rating or a call on the stock: one test per use of cash (reinvestment, acquisitions, divestitures, dividends, buybacks, debt), each comparing what was paid with what was received, because most actions are sound at one price and unsound at another. The yardstick is long-term value per share, not growth, earnings per share or the share price. A board or finance team weighing its own choice ("buy back shares or raise the dividend", "pay down debt or acquire") is asking a different question: it gets the arithmetic of each option side by side, none recommended. Size the work to the question: "was Apple's buyback a good use of cash" gets the buyback test and the net share count, not the deals or the incentive review.

## Before starting

- Without the Bigdata.com tools, say so and ask for the connector. No figures from memory in the meantime.
- Pass `plugin_slug: "bigdata-capital-allocation"` on every Bigdata.com call that accepts it.
- `references/working-with-bigdata.md` maps each data need to a tool. The other reference files are working notes for the parts named below; the reader never sees them.

## Method choices that are not the default

- **The user's parts first.** The parts the user asked for come first, in the user's order, each answered in full; the tests below apply only to the uses of cash the question reaches, and a note that answers the question with fewer tables and tests is the better note.
- **Sources and uses tied to cash before any verdict,** so every test works from the same cash, with R&D kept beside them because it is reinvestment the statements expense; on the page only as far as the question needs. When the question is about a pattern over time, spending per dollar of sales change is compared with the company's own history and named peers, with CEO changes marked, because a change in pattern usually follows a change at the top (`references/capital-allocation.md`, sources and uses; spending pattern).
- **Buybacks on price against value at the time, net of issuance.** Shares bought and average price paid come from the filings' repurchase tables; shares issued under compensation plans in the same year are netted. Value per share at each buyback date comes either from that year's normalised operating profit after tax capitalised at the cost of capital plus the value of growth at the three-year return on new investment, or from a valuation range published then in research or news, quoted with its date. Where the first route is used, its inputs appear once (share count, net debt, tax rate, cost of capital, and the years of excess return, moved a few years either way because the value moves with them) so the reader can rebuild the figure. The return is set against the cost of equity, and the record is laid against the valuation path: did buying rise when the stock was dear and stop when it was cheap (`references/capital-allocation.md`, buybacks; `references/expectations.md`, steady state and value creation).
- **Earnings-per-share accretion answered with value.** When management argues a buyback is accretive, give the breakeven P/E beside the P/E paid and say that accretion says nothing about value (`references/capital-allocation.md`, buybacks).
- **Reinvestment by spread and three-year return on new investment, when the question reaches it.** Judge it by ROIC against the cost of capital, with and without goodwill where acquisitions are large, and by the three-year rolling return on new investment, because a single year can be operating leverage (`references/capital-allocation.md`, organic reinvestment; `references/roic.md`, ROIIC and the spread). The share of capex that is growth and the retention test (actual growth against ROE times one minus the payout, where growth well below it means cash the business cannot use) go on the page only where the question is whether the company keeps cash it cannot use.
- **The cost of capital is one figure.** One stated cost of equity and one cost of capital, with the 10-year yield from the country data, the beta and the premium in a single clause and no regression statistics, and a one-point move either way where a verdict turns on it (`references/valuation.md`, cost of capital).
- **Deals on premium against haircut synergies, then the later record, when the question reaches acquisitions.** The premium is taken from the undisturbed price before rumours. Cost synergies get a haircut and revenue synergies a heavy one, because revenue synergies are often missed by a wide margin. Then deal value net of the premium, the share of the buyer's value at risk, and the buyer's move against the index around the announcement; then the goodwill impairments and disposals of the acquired unit, which show overpayment after the fact. A low premium, a sole bidder and a strong operator predict success; accretion, relative P/E and relatedness do not. The size above which a deal counts as material is stated once (`references/capital-allocation.md`, acquisitions). How often deals of a kind create value enters only where the verdict on a deal rests on it, with its population and period in the sentence.
- **Dividends as a commitment.** Coverage by free cash flow after stock compensation, the funding source named (a dividend paid from debt or new equity is a false signal), and net shareholder yield rather than dividend yield (`references/capital-allocation.md`, dividends).
- **Leverage on the agency ranges first,** when the question touches debt or payouts look borrowed. Funds from operations to debt and debt to EBITDA, with debt adjusted for leases and pensions, placed on the agency ranges, then coverage and debt to capital on the rating medians as the cross-check, saying when they disagree; and whether payouts were financed by borrowing (`references/credit.md`, placing the company on the rating scales).
- **Incentives read from the proxy, when the question reaches pay or governance.** Each long-term plan metric is read for what it rewards: absolute total shareholder return is mostly luck, and EPS and revenue targets reward buybacks and deals that lift the metric without value. The ownership and voting structure decides whom the plan serves. Answer which way the CEO goes when the plan and value per share conflict (`references/capital-allocation.md`, incentives).
- **Stated priorities against actions.** Stated priorities from calls and investor days, dated, against what the plan rewards and what the cash did; where they disagree, the figures say so.
- **Special cases change the tests.** Serial acquirers: tuck-ins aggregated by year and judged through ROIC with goodwill and later impairments. Banks and insurers: payouts against regulatory capital, ROE against the cost of equity. Utilities: rate-base growth and the allowed return; the buyback test rarely applies. Outside the US: legal limits on buybacks, family or state ownership that sets the payout. Early-stage companies: cash burn and funding history in place of the return on new investment (`references/capital-allocation.md`, special cases).
- **A decision among options.** For a board's own choice, the options sit side by side with the arithmetic the choice turns on, usually the cash cost and what each does to value per share and leverage, earnings per share only beside value, and what each commits the company to, a dividend being a commitment and a buyback residual.

## Where it goes wrong

- **Authorisations read as purchases.** An authorisation is a ceiling; only the repurchase tables give what was bought and at what price.
- **Gross buybacks.** Shares issued under compensation plans offset them, so a gross figure overstates the cash returned and the fall in the share count. Buying back shares to offset stock awards is not value creation.
- **A later price fall read as a buyback error.** The test is price against value when the shares were bought; a hindsight price measures luck.
- **One year of return on new investment read as evidence.** A high single year can be operating leverage; five annual periods allow a three-year figure and nothing longer.
- **Management's synergy figure carried at face value.** Integration costs often run to a year or more of savings, so the stated figure overstates the deal's value.
- **A risk-free rate taken from memory** when the country data has the yield.
- **Citations assembled at the end.** The link goes next to the fact as each repurchase table, deal announcement and proxy item is captured.
- **The note mirrors the method.** A test that does not change a verdict stays in the working, and the working itself never reaches the page.

## What the data has, and does not

Five fiscal years of annual statements, ratios and key metrics, five periods being the limit, so a decade of deals or a long CEO tenure is extended by search and the note says where the statements stop. The executive team and the deal history need FactSet access; when either comes back empty, executive changes and acquisitions come from search. Repurchase tables, the proxy and deal announcements come from filings and news, read in full when the excerpts cut off a table. The average price in each buyback year and the buyer's move around each announcement need daily prices for the stock and its index; the overview carries standard windows only. A valuation range published at a past date comes from dated research and news, since consensus and targets are a current snapshot with no history. There is no structured field for the cost of equity or of capital; build it once from the country data's yield. Peers are pulled as a set in one batch. A private company has no share price, so the buyback and deal-reaction tests do not run; sources and uses, reinvestment and deal prices run from what the filings hold. Capital intensity norms by sector are in `references/sector-primers.md`.

## Write

`references/output-standard.md` holds the rules. The title carries the finding in one line ("Apple's buybacks returned more than its cost of equity until 2021, and less since"). The opening answers the question first: where the cash went, which uses created or destroyed value and by how much per share, and what management is paid for, as far as the question asks. The body follows the question, the user's parts in the user's order; each use it reaches gets its verdict as a plain sentence with the test that decides it ("the buybacks paid below value until the multiple doubled, and above it since"), never a label such as created, neutral or destroyed, and says so when the test cannot decide. What the pattern means for value per share from here closes the note. Sub-headings state the finding ("Buybacks shrank the share count by 3 percent a year net of awards"), never the step that produced it.

## Before sending

- The user's parts are answered in the user's order, each findable by its name, and every table on the page is one the reader needed.
- The sources and uses tie to the change in cash each year, and buybacks are actual purchases net of issuance.
- Every use the question reaches has a verdict in a sentence with its deciding test; no composite score, no label, and no option recommended.
- Every value per share built on the page can be rebuilt from inputs stated once.
- Every number in the opening agrees with its table, and the cost of capital is the same figure everywhere it is used.
- Every code name or internal term (a plan metric, a program name) is explained where it first appears.
- Nothing on the page names a file, formula, table, primer, author or method; no figure is tagged with how it was obtained; no sentence describes how the note was made.
