# Northwind Progress Log

> **Source of truth:** this file. Claude reads only this copy. The [Confluence Progress Log](https://dhanushpixel.atlassian.net/wiki/spaces/NWFDE/pages/622895/Progress+Log) is a synced copy, updated on save.

**Last updated:** Thu 29 Oct 2026

## Status

|                       |                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------- |
| **Current week**      | 1, still open. On vacation 30 Oct – 14 Nov. Week 1 closes **Sun 15 Nov** once KAN-13 (Vercel page) ships |
| **Rank · XP**         | Intern · **43 XP**                                                                                        |
| **Next up**           | Sun 15 Nov: recap quiz → explain-back → read-only RLS rule → Vercel page + root README (KAN-13)          |
| **North Star metric** | Average first response time: **4 days → under 24 hours** (dataset baseline: 95 hrs)                       |

## Schedule

- **Time zone:** Singapore (SGT). Avoid the 7:45–8:05 pm handover.
- **Vacation:** 30 Oct – 14 Nov 2026. The pre-vacation Week 2 slot (26–29 Oct) wasn't used, so the whole plan moved **+1 week** (re-plan 29 Oct).
- **From Mon 16 Nov:** fixed 14-day shift rotation (2 on, 2 off, 3 on, 2 off, 2 on, 3 off), marked "Workday" in Google Calendar. **No study on Workdays.**
- **Study weeks run Wed–Tue.** Split weeks (W2, 4 … 30, S1, S3) are off Wed, Thu, Mon, Tue; block weeks (W3, 5 … 31, S2, W32) are off Fri, Sat, Sun.
- **Sun 15 Nov:** close Week 1. **W2 starts Wed 18 Nov**, W3 Wed 25 Nov.
- **Board panel** by Tue 13 Jul 2027.
- **Rank targets:** Junior FDE 15 Dec · FDE 19 Jan · Senior FDE 6 Apr · Lead FDE 15 Jun · Principal 13 Jul 2027.
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
| Sun 15 Nov      | Recap quiz + read-only RLS rule + Vercel page + root README (KAN-13)                      | ⏳ To do |

**Wrap-up (25 Oct)**

- **Shipped:** ticket generator v2 and 500 tickets in Supabase, data README, boss-fight write-up.
- **Struggled with:** the generator code itself. 15+ new Python ideas in one afternoon.
- **Missed:** skipped every prediction prompt.
- **Energy:** 4/5.

## Re-plan (29 Oct): nothing done 26–29 Oct, plan moves +1 week

| Day        | Plan                                                                                                   |
| ---------- | ------------------------------------------------------------------------------------------------------ |
| Sun 15 Nov | **Close Week 1:** recap quiz · 15-min explain-back on the generator · read-only RLS rule · Vercel page + root README (KAN-13). Overrun: page can slip to Wed 18 |
| Wed 18 Nov | **W2 Learn:** tokens, input vs output price, cost per answer, model landscape. Cost sheet by hand, no code. Finish sign-ups (KAN-11: OpenRouter key, LangSmith/Langfuse, AWS + $10 alert) |
| Thu 19 Nov | **W2 Boss fight:** stakeholder map (spot the blocker) + the four status updates                         |
| Mon 23 Nov | **W2 Read code:** prompting basics, first OpenRouter call (predict, then run), one small Ollama model   |
| Tue 24 Nov | **W2 Mission:** 3 models × 20 tickets → cost per 1,000 tickets for Helen · end-of-week debrief          |

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
- Daniel's demo (Mon 26 Oct, 9 a.m., Helen attending) **slipped**: no page to show yet. The Sun 15 Nov catch-up episode opens with Daniel asking where it is.
- **Open threads:** "There's another number the board will ask about. Probably with Helen." · Layoffs: "not THIS part of it, anyway." · Kenji: Sofia's team handles ~60 tickets a day "now. Before... well. Ask her."
- **Still unpinned:** the deadline for under 24 hrs; how "right answers" is measured.
- **Secrets uncovered:** none yet.

## Python Gym (FDE 35)

- Switched 29 Oct from LeetCode 75 to the **FDE 35** list (Confluence → Python Gym: FDE 35): arrays/hashing, parsing/intervals/binary search, OOP and design, bits and linked lists, trees, graphs, plus 295 as an optional stretch.
- Workday habit: 1 problem per Workday, 30–45 min. Starts Mon 16 Nov. Runs in parallel, doesn't gate the FDE path.
- Target 35/35 by Thu 21 Jan 2027. Checkpoints: 9 by 1 Dec · 18 by 19 Dec · 26 by 3 Jan · 31 by 15 Jan · 35 by 21 Jan.
- Status: **0/35**. The 6 LeetCode 75 problems solved in Oct (#1–6 Array/String) aren't on the new list; kept as bonus reps.

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
