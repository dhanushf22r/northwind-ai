# Northwind Progress Log

> **Source of truth:** this file. Claude reads only this copy. The [Confluence Progress Log](https://dhanushpixel.atlassian.net/wiki/spaces/NWFDE/pages/622895/Progress+Log) is a synced copy, updated on save.

**Last updated:** Sun 25 Oct 2026

## Status

|                       |                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------- |
| **Current week**      | 1 (compressed: Thu 22 – Sun 25 Oct 2026). Closes Tue 27 Oct once KAN-13 (Vercel page) ships |
| **Rank · XP**         | Intern · **43 XP**                                                                          |
| **Next up**           | Mon 26: explain-back quiz → read-only RLS rule → Vercel page (KAN-13)                       |
| **North Star metric** | Average first response time: **4 days → under 24 hours** (dataset baseline: 95 hrs)         |

## Schedule

- **Time zone:** Singapore (SGT). Avoid the 7:45–8:05 pm handover.
- **Vacation:** 30 Oct – 14 Nov 2026. Week 2 is compressed into Mon 26 – Thu 29 Oct.
- **From Mon 16 Nov:** fixed 14-day shift rotation (2 on, 2 off, 3 on, 2 off, 2 on, 3 off), marked "Workday" in Google Calendar. **No study on Workdays.**
- **Study weeks run Wed–Tue.** Split weeks (W3, 5 … 31, S2, W32) are off Wed, Thu, Mon, Tue; block weeks (W4, 6 … 30, S1, S3) are off Fri, Sat, Sun.
- **W3 starts Wed 18 Nov.** Sun 15 Nov is a spare catch-up day.
- **Board panel** by Tue 6 Jul 2027.
- **Rank targets:** Junior FDE 8 Dec · FDE 12 Jan · Senior FDE 30 Mar · Lead FDE 8 Jun · Principal 6 Jul 2027.
- Claude builds each week's Google Calendar blocks on off days only. I flag shift swaps or overtime at the end-of-week debrief.

## Week 1 · "Show me something by Friday"

| When            | What                                                                                      | Status   |
| --------------- | ----------------------------------------------------------------------------------------- | -------- |
| Thu 22          | Karpathy talk → LLM basics quiz, 4/5                                                      | ✅ Done  |
| Sat 24          | Repo skeleton (`0b7258b`)                                                                 | ✅ Done  |
| Sun 25          | Accounts: Supabase (Asia-Pacific, automatic RLS), Vercel (Hobby), OpenRouter (no key yet) | ✅ Done  |
| Sun 25          | Ticket generator v1 → v2 → CSV → Supabase (KAN-12)                                        | ✅ Done  |
| Sun 25          | Boss fight: Daniel, C+ pass (KAN-14)                                                      | ✅ Done  |
| Sun 25          | GitHub for Jira connected; debrief (KAN-15)                                               | ✅ Done  |
| Mon 26 – Tue 27 | Read-only RLS rule + Vercel page + root README (KAN-13)                                   | ⏳ To do |

**Wrap-up (25 Oct)**

- **Shipped:** ticket generator v2 and 500 tickets in Supabase, data README, boss-fight write-up.
- **Struggled with:** the generator code itself. 15+ new Python ideas in one afternoon.
- **Missed:** skipped every prediction prompt.
- **Energy:** 4/5.

## Week 2 plan (about 1 hr/day, Mon 26 – Thu 29)

| Day        | Plan                                                                                  |
| ---------- | ------------------------------------------------------------------------------------- |
| Mon 26     | 15-min explain-back on the generator · read-only RLS rule · start Vercel page         |
| Tue 27     | Finish Vercel page + root README → Week 1 closed                                      |
| Wed 28     | Concepts: tokens, input vs output price, cost per answer. Cost sheet by hand, no code |
| Thu 29     | Boss fight: stakeholder map (spot the blocker)                                        |
| Sun 15 Nov | Catch-up: OpenRouter 3-model × 20-ticket mission                                      |

Pending: exact daily start times (for calendar blocks); carry-over notes for KAN-17 (messy complaint text, week 3) and KAN-20 (orders dataset, week 6).

## Data

See [`data/README.md`](data/README.md) for the full schema.

- `tickets.csv`: 500 rows, `random.seed(42)`, reference date 25 Oct 2026 09:00.
- **Baseline:** 479 answered tickets, average first response **95 hrs (~4 days)**. 21 tickets still awaiting a reply, so the true figure is worse (survivorship bias).
- Verified in Supabase SQL: `select round(avg(first_response_hours)) from tickets;` → 95.
- Supabase `tickets` table: `ticket_id` primary key, RLS on, no policies yet.
- **Known gaps (on purpose):** order IDs not linked to an orders table (week 6); complaint text too clean (week 3).

## Shipped

| Date       | What                               | Commits              |
| ---------- | ---------------------------------- | -------------------- |
| Sat 24 Oct | Repo skeleton                      | `0b7258b`            |
| Sun 25 Oct | Ticket generator + 500 tickets     | `6007067`, `8d66280` |
| Sun 25 Oct | Generator v2 + data README         | `575fc99`            |
| Sun 25 Oct | Boss-fight write-up                | `d7357fc`            |
| Sun 25 Oct | Supabase `tickets` table, 500 rows | —                    |

## Boss fights

| Week | Character | Win condition              | Grade     | XP  | Missed / practise                                                                                                          |
| ---- | --------- | -------------------------- | --------- | --- | -------------------------------------------------------------------------------------------------------------------------- |
| 1    | Daniel    | Get him to name one number | C+ (pass) | +6  | Got the 9-day story wrong; no "by when?"; "right answers" unmeasured; ignored Helen. **Practise: ask, then stop talking.** |

Full write-ups: [`consulting/boss-fights/`](consulting/boss-fights/).

## Story state

- **NW-0001** is the Harbour Foods pallet shown "in Rotterdam" for 9 days. Kenji says it never left Leeds (open thread: how does he know?).
- The old bot answered in seconds and was **wrong**; the people took 9 days to fix it.
- Daniel wrote **"4 days → < 24 hrs"** under NEVER AGAIN.
- Daniel's demo: Mon 26 Oct, 9 a.m., Helen attending.
- **Open threads:** "There's another number the board will ask about. Probably with Helen." · Layoffs: "not THIS part of it, anyway." · Kenji: Sofia's team handles ~60 tickets a day "now. Before... well. Ask her."
- **Still unpinned:** the deadline for under 24 hrs; how "right answers" is measured.
- **Secrets uncovered:** none yet.

## Python Gym (LeetCode 75)

- Workday habit: 1 problem per Workday, 30–45 min. Runs in parallel, doesn't gate the FDE path.
- Target 75/75 by Tue 30 Mar 2027. Checkpoints: 10 by 21 Nov · 25 by 20 Dec · 40 by 20 Jan · 55 by 18 Feb · 75 by 30 Mar.
- Status: 6/75 (assumed #1–6 Array/String; confirm).

## Self-ratings (1–5, 19 Oct 2026)

Python 2 · APIs 3 · LLMs 0 (likely higher) · Cloud 2.5 · Discovery 2 · Specs 2 · Pricing 2

## Trainer adjustments

- **Python pace (25 Oct):** max 3 new concepts per session; open each session with a 15-min explain-back; prediction before every run is required. Goal: read and change code, not write it from memory.
- **Python:** guided builds, explain each line first. AI coding tools from week 2, with review.
- **Git:** start of session `git pull --rebase`. With uncommitted changes: commit first, then pull, then push. Commit messages start with the Jira key: `KAN-<n> <what>`.
- **Terminal:** paste output after each step; use Tab completion to avoid typos.
- **Discovery:** one-line hint card before boss fights until week 5.
- **Specs:** templates first, own versions from week 7.
- **Overruns:** ship the script/data first; UI can slip a day.
- **Big jumps:** slow down at weeks 11 (RAG), 17 (LangGraph), 30 (fine-tuning).
- **After breaks:** open with a recap quiz before new material.

## Records

- Repo: [github.com/dhanushf22r/northwind-ai](https://github.com/dhanushf22r/northwind-ai), local at `~/Desktop/northwind-ai`.
- Each session: `cd` repo → `conda deactivate` → `source .venv/bin/activate` (Python 3.11.4).
- Jira project KAN (epics KAN-4..8 = acts; stories KAN-2, KAN-16..49 = weeks; KAN-50 = vacation).
- End of session: "save progress" → Claude updates Confluence and Jira. Start of a new chat: "check progress".
- Chat deletion rule: only delete a chat after the log is updated and keepers are committed.
