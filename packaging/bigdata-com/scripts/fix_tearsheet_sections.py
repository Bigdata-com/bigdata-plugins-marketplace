#!/usr/bin/env python3
"""Map the old tearsheet section names to the live `sections` values, inside code spans only."""
import re, sys
MAP = {"price_performance": "company_overview", "analyst_data": "analyst_ratings", "estimates": "analyst_estimates",
       "events_calendar": "earnings_calendar", "fundamentals": "financial_statements, financial_ratios, key_metrics",
       "company_funds_holders": "fund_trends_history", "jobs_data": "hiring_trends", "esg_data": "esg_performance"}
VALID = {"company_overview", "c_level_leadership", "financial_ratios", "key_metrics", "dividends", "analyst_estimates", "latest_earnings",
         "earnings_calendar", "financial_statements", "revenue_segmentation", "analyst_ratings", "fund_trends_history", "hiring_trends",
         "esg_performance", "mergers_acquisitions"}
def fix_span(s):
    inner = s[1:-1]
    toks = [t.strip() for t in inner.split(",")]
    if not all(re.fullmatch(r"[a-z_]+", t) for t in toks): return s
    if not any(t in MAP or t in VALID for t in toks): return s
    out = []
    for t in toks:
        for m in (MAP.get(t, t)).split(", "):
            if m not in out: out.append(m)
    return "`" + ", ".join(out) + "`"
changed = 0
for path in sys.argv[1:]:
    t = open(path, encoding="utf-8").read()
    new = re.sub(r"`[^`\n]+`", lambda m: fix_span(m.group(0)), t)
    if new != t:
        open(path, "w", encoding="utf-8").write(new); changed += 1; print("fixed", path)
print("files changed:", changed)
