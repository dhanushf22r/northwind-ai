# data/

Synthetic Northwind Logistics data. **Nothing here is real company data.**

## tickets.csv

500 synthetic customer support tickets, made by `generate_tickets.py`.

| Column | Type | Example | Notes |
| --- | --- | --- | --- |
| `ticket_id` | text | `NW-0001` | `NW-` plus a zero-padded number, 0001–0500 |
| `customer` | text | `Harbour Foods Ltd` | One of 20 fictional customers |
| `order_id` | text | `ORD-48213` | Text, not a number: it's a label, never used for maths |
| `complaint` | text | `Driver left the goods at the wrong dock.` | One of 55 complaints in 8 groups |
| `urgency` | text | `high` | `low` / `medium` / `high`, weighted per category (damage and customs lean high, account questions lean low) |
| `category` | text | `damage` | The answer key for triage (week 3) and evals (week 7) |
| `created_at` | text (date) | `2026-10-16 09:00` | Spread over the 60 days before the reference date, 25 Oct 2026 09:00 |
| `first_response_hours` | number or blank | `81` | Hours until support first replied. Clusters near 68, averages ~96 (4 days), max 216 (9 days). **Blank** = no reply yet |
| `status` | text | `answered` | `answered` or `awaiting_response` |

**Categories (8):** `delays`, `tracking`, `damage`, `wrong_delivery`, `billing`, `refunds_claims`, `customs_hazardous`, `account_general`.

**Baseline (the North Star metric):** 479 answered tickets, average first response **95 hours (about 4 days)**. Daniel's target is under 24 hours. The 21 tickets still awaiting a reply aren't in that average, so the true figure is slightly worse.

**Seeded story ticket:** `NW-0001` is the Harbour Foods pallet shown as "in Rotterdam" for 9 days. It never left Leeds.

## How to regenerate

From the repo root:

```bash
python data/generate_tickets.py
```

`random.seed(42)` makes the output identical on every run, so evals and debugging always use the same data. Changing the customer or complaint lists changes the tickets, even with the same seed.
