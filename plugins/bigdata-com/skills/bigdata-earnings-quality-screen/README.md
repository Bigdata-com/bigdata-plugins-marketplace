# Bigdata Earnings Quality Screen

Part of the **Bigdata.com** plugin.

A focused skill that produces a cited **earnings quality screen** — cash conversion, accruals, and accounting red flags, with a verdict on how trustworthy reported earnings are — powered by **Bigdata.com MCP**.

---

## What It Produces

- Cash conversion: OCF/NI and FCF/NI across several periods
- Accruals analysis and the balance-sheet accrual ratio
- Working-capital signals: DSO, DIO, DPO versus revenue growth
- Revenue-recognition and capitalization red flags
- GAAP versus non-GAAP gap and the nature of the add-backs
- Optional Beneish M-Score with inputs shown
- Overall quality verdict with the specific evidence behind it
- Sources with inline citations, plus the standard footer and disclaimer

---

## Usage

Ask in natural language, or use the namespaced command within the plugin:

    /bigdata-com:earnings-quality-screen

---

## Structure

    bigdata-earnings-quality-screen/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/report-template.md
    ├── references/
    │   └── quality-of-earnings.md
    │   └── red-flags-checklist.md
    └── scripts/
        └── earnings_quality.py

---

## Requirements

An active **Bigdata.com MCP** connection configured in your agent platform.
The skill uses `find_securities`, `bigdata_company_tearsheet`, `bigdata_search`.

---

## Related Skills

- **Earnings digest**
- **Risk assessment**
- **Investment memo**
- **Valuation snapshot**

---

## License

See the root `LICENSE` file of the plugin repository for details.
