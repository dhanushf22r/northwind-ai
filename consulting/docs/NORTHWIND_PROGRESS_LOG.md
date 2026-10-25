Current week: 1 (compressed: Thu 22 – Sun 25 Oct 2026, AWS exam Thu 22 Oct morning — PASSED)
Rank: Intern | XP: 13
Time zone: Singapore (SGT). Avoid the 7:45–8:05 pm handover.
SCHEDULE (set 25 Oct): Vacation 30 Oct – 14 Nov. Week 2 compressed Mon 26 – Thu 29 Oct. From Mon 16 Nov: fixed 14-day shift rotation (2 on, 2 off, 3 on, 2 off, 2 on, 3 off), marked "Workday" in Google Calendar. NO study on Workdays. Study weeks run Wed–Tue: split weeks (W3, 5 … 31, S2, W32) are off Wed, Thu, Mon, Tue; block weeks (W4, 6 … 30, S1, S3) are off Fri, Sat, Sun. W3 starts Wed 18 Nov; Sun 15 Nov is a spare catch-up day. Board panel by Tue 6 Jul 2027. Day-by-day rhythm: Confluence "How We Work"; off days per week: Confluence "Roadmap"; Jira stories carry start/due dates.
Planning: Claude builds each week's Google Calendar blocks on off days only (private, 15-min reminder, prompt in description). I flag shift swaps or overtime at the end-of-week debrief.
Source of truth: Confluence Progress Log (space NWFDE). This file is a backup copy.

TRACKING
- Confluence space NWFDE (dhanushpixel.atlassian.net/wiki): Mission Control, Roadmap, How We Work, Progress Log, Toolbox, Story Cast and Secrets
- Jira project KAN: epics KAN-4..8 = acts, stories KAN-2, KAN-16..49 = weeks/sprints, KAN-50 = vacation
- 25 Oct re-plan: all story/epic dates moved to Wed–Tue off-day weeks; Roadmap lists off days per week; rank targets: Junior FDE 8 Dec, FDE 12 Jan, Senior FDE 30 Mar, Lead FDE 8 Jun, Principal 6 Jul 2027
- Holiday flags: W08 off days include Christmas Day; W09 off days include New Year's Eve (decide if lighter)

WEEK 1 PLAN (calendar blocks created 19 Oct)
- Thu 22, 6:30–7:40 pm: Karpathy video + 5 surprises → DONE (said "nothing surprised"; replaced by LLM basics quiz, 4/5 on Sat 24 Oct, +10 XP; missed question number not yet reported)
- Fri 23 blocks (concept lesson; accounts + repo) → not done Friday; repo setup moved to Sat 24 evening
- Sat 24 evening: repo setup DONE (see SHIPPED); accounts (Supabase, Vercel, OpenRouter) after 8:05 pm handover — pending
- Sun 25, 10:00 am–12:30 pm: build steps 1–5 (ticket dict → randomise → 500 loop → CSV → Supabase)
- Sun 25, 1:30–3:30 pm: Vercel page + README
- Sun 25, 4:00–5:00 pm: Daniel boss fight (hint card first), then "save it"
- Sun 25, 5:15–6:00 pm: debrief, updated log, Mon 26 – Thu 29 availability for Week 2
- Open: tonight's Week 1 blocks and Week 2 blocks are NOT in Google Calendar yet; send free hours at the debrief

SELF-RATINGS (1–5, set 19 Oct 2026)
Python 2 · APIs 3 (fluent using, basic building) · LLMs 0 · Cloud 2.5 (follows instructions)
Discovery 2 · Specs 2 · Pricing 2
Note 24 Oct: says the Karpathy talk held no surprises → LLM basics likely above 0; raise the bar on concept work.

TRAINER ADJUSTMENTS
- Python: guided builds, explain each line before I write it; I type code by hand in week 1 (no AI autocomplete), AI coding tools from week 2 with me reviewing their output
- LLMs: Karpathy first, then concept lesson + quiz
- Discovery: one-line hint card before boss fights until week 5
- Specs: templates first, own versions from week 7
- If a mission runs over: ship the script/data first, UI can slip a day
- Slow down at the big jumps: weeks 11 (RAG), 17 (LangGraph), 30 (fine-tuning)
- Terminal: makes small paste mistakes (extra words, commas in mkdir) — have him paste output after each step
- After breaks: open the first week back with a recap quiz before new material

REPO & RECORDS
- Repo: https://github.com/dhanushf22r/northwind-ai (public, MIT, Python .gitignore), local at ~/Desktop/northwind-ai
- Env: Anaconda installed; Python 3.11.4; project venv at .venv. Each session: cd repo → conda deactivate → source .venv/bin/activate
- GitHub: Claude commits the progress log to consulting/docs/NORTHWIND_PROGRESS_LOG.md whenever I ask ("commit the log"). Other files: Claude writes them, I commit
- After each boss fight/debrief I say "save it"; Claude reminds me if I forget
- Layout: data/, consulting/boss-fights/wNN-name.md, consulting/debriefs/wNN-debrief.md, consulting/docs/ (.gitkeep in each)
- Boss-fight file: setup, transcript (my lines verbatim), grade + XP, what I missed, one thing to practise
- Chat deletion rule: only delete a chat after this log is updated and keepers are committed

STORY STATE
- Kenji told me the old chatbot invented delivery dates (Rotterdam pallet)
- Lobby teaser: Kenji says the pallet "was never in Rotterdam, it never left Leeds", then left before I could ask how he knows (open thread)
- Day 1: Kenji's sticky note "Why did it lie?" — answered. My Daniel line (+3 XP): "The previous bot did not look where the pallet was — ours will before answering." Polished: "The old bot never checked where the pallet was, so it made up an answer that sounded right. Ours will check before it answers."
- The Rotterdam pallet will be seeded in my synthetic ticket data
- Daniel pushed the Friday demo to Monday 26 Oct morning
- Secrets uncovered: none yet

SHIPPED
- Sat 24 Oct: northwind-ai repo skeleton (folders, venv) — pushed to GitHub as "Week 1: repo skeleton" (0b7258b), confirmed 25 Oct
BOSS FIGHTS: none yet
