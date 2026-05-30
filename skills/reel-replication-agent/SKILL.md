---
name: reel-replication-agent
description: Analyses top-performing Reels from a list of creators the user provides, then rescripts each one 3 ways in the voice of either Nick Hancock (@runwithnick) or Josh Laker (@joshc.laker). Use when the user says "replicate these creators," "rescript top videos," "analyse and rescript," "give me 3 versions," or "find what worked and rewrite it for my coach."
---

# Reel Replication Agent

You take a list of Instagram creators, find their top performing Reels, extract what made each one work, then produce 3 rescripted versions for either Nick Hancock or Josh Laker — ready to film and import into the dashboard.

---

## Step 1 — Collect Inputs

Before doing anything, confirm you have:

1. **Creator handles** — the list of Instagram accounts to analyse (e.g. @trackclubbabe, @runningexplained)
2. **Target coach** — Nick Hancock (@runwithnick) OR Josh Laker (@joshc.laker)
3. **Number of top videos per creator** — default is 3 per creator
4. **Timeframe** — default is last 90 days; specify if different

If any are missing, ask before proceeding.

---

## Step 2 — Research Each Creator

For every creator handle provided:

### Find their top performing Reels

Search for:
```
[handle] instagram reels [current year]
site:instagram.com [handle]
[handle] viral reel running coaching
```

For each creator, identify their **top 3 Reels** by:
- Highest view count relative to their follower count (virality score = views ÷ followers × 100)
- High comment volume (especially comments like "how do I work with you", "I just DM'd you", "saving this")
- High save rate signals (people saying "saving this" in comments)

### Extract per-Reel data

For each top Reel, capture:

| Field | What to get |
|-------|------------|
| Creator handle | @username |
| Follower count | Current |
| View count | Approximate |
| Virality score | Views ÷ followers × 100 |
| Hook | Exact opening line — first 2–3 seconds |
| Hook type | Story / Contrarian / Consequence / Number / Question / Myth bust |
| Script structure | How it flows: hook → amplifier → problem → diagnosis → fix → CTA |
| CTA type | DM / Comment / Save / Link in Bio / Follow / Direct Offer |
| CTA exact wording | Word for word |
| Format | Talking head / B-roll + voiceover / Text on screen |
| Topic | Training tips / Transformation / Nutrition / Race strategy / Mindset / Gear |
| Why it worked | 1–2 sentences: what made this stop the scroll and drive action |

---

## Step 3 — Analyse What Made Each Reel Work

Before rescripting, write a brief **Replication Brief** for each original Reel. This is the bridge between their version and your coach's version.

```
REPLICATION BRIEF
Original creator: @handle
Original hook: "exact words"
Why it worked: [the mechanism — what belief it broke, what emotion it triggered, what problem it named]
Hook type: [from the six types]
Script skeleton: [the structural flow stripped of their specific content]
CTA mechanic: [what action it drove and why]
Adaptation notes: [what needs to change for Nick/Josh — topic, audience, credentials, language]
```

The script skeleton is the most important output here. Strip away their specific content and keep the structure. This is what you replicate — not their words, their architecture.

---

## Step 4 — Rescript for the Target Coach

For each original Reel, produce **3 script versions** using the target coach's voice, framework, and real content.

### Which framework to use

**For Nick Hancock (@runwithnick / MaxMile):**
- British English throughout
- His phrases: "Simple as that." "Trust me, I get it." "Knackered." "Rubbish." "Consistency is king." "Hard, easy, hard."
- His credentials: sub-3 marathoner, 2:50 at London at 43, former smoker, coached athletes from 5K to 100 miles, MaxMile app
- Hook rule: never start with "If you..." or "Are you..." — statement, number, or story first
- No motivational language. No hedging.
- Script length: 90–175 words. Tight. Spoken, not written.
- CTA: ManyChat keyword comment format preferred. "comment '[KEYWORD]' to try it for free"

**For Josh Laker (@joshc.laker):**
- American English throughout
- His phrases: "Train with purpose." "The gray zone." "Stimulus, feedback, recovery, harder stimulus." "Back-to-back long runs." "Aerobic base first."
- His credentials: USATF Level 1 & 2, UESCA certified, MS in Human Performance, just retired US Coast Guard, 220+ miles at Ohio Backyard Ultra 2023, 20 ultras, 13 trophies, coaching 16 athletes at $400/month
- Five archetypes — prioritise Structured Staller and Redemption Runner (highest converting from call data)
- Hook rule: never start with "If you..." — statement, story, or number
- No motivational language. Diagnose and fix.
- Script length: 90–160 words.
- CTA: "comment '[KEYWORD]' and I'll send you details on working together"

### The 3 versions

Each version uses a **different hook type** from the six:
1. Story open / Contrarian statement
2. Consequence threat / Specific number
3. Genuine question / Myth bust

The body structure and CTA can vary between versions — use whichever fits the hook best.

### Script output format (repeat for each version)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SOURCE: @[original creator handle]
ORIGINAL HOOK: "[exact original hook]"
WHY IT WORKED: [1 sentence]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

VERSION 1 — [Hook type used]

HOOK
[hook line(s)]

BODY

[SECTION LABEL]
[2–4 sentences]

[SECTION LABEL]
[2–4 sentences]

[SECTION LABEL]
[2–4 sentences]

CALL TO ACTION
[CTA]

Word count: [X] · Est. duration: [X sec]

---

VERSION 2 — [Hook type used]

HOOK
[hook line(s)]

BODY
...

CALL TO ACTION
[CTA]

Word count: [X] · Est. duration: [X sec]

---

VERSION 3 — [Hook type used]

HOOK
[hook line(s)]

BODY
...

CALL TO ACTION
[CTA]

Word count: [X] · Est. duration: [X sec]
```

---

## Step 5 — Output Importable JSON

After all scripts are written, output a single JSON block for importing into the dashboard. Each version is a separate content idea.

```json
{
  "clientId": "cl1",
  "contentIdeas": [
    {
      "title": "[Coach name] × @[original creator] — V1",
      "hook": "Exact hook line from the script",
      "scriptOutline": "Source: @[handle] | Hook type: [type] | Why it worked: [reason]",
      "scriptTemplate": "Full script here with [BRACKETS] for fill-in sections",
      "ctaRecommendation": "Exact CTA wording",
      "ctaType": "DM",
      "status": "Idea"
    }
  ],
  "reels": [
    {
      "coachHandle": "@[original creator]",
      "followers": 0,
      "views": 0,
      "viralityScore": 0,
      "format": "Talking Head",
      "topic": "Training Tips",
      "hookText": "Original hook",
      "scriptSummary": "What the original script covered and why it worked",
      "ctaWording": "Original CTA",
      "link": ""
    }
  ]
}
```

Use `"clientId": "cl1"` for Nick Hancock, `"clientId": "cl2"` for Josh Laker.

**Naming convention for titles:** `[Coach first name] × @[source] — V[number]`
Examples: `Nick × @trackclubbabe — V1`, `Josh × @mr.ultrarunner — V2`

---

## Step 6 — Import to Dashboard

Tell the user:

1. Copy the JSON block above
2. Open the dashboard (dashboard.html)
3. Click **⬇ Import** in the top bar
4. Paste and import — all scripts land in the Content Pipeline as Ideas
5. Click any card to see the full script with [BRACKETS] highlighted
6. Click **Copy Full Brief** to hand off to the coach for filming

---

## Quality Rules — Apply to Every Script

**Never replicate:**
- Their specific personal anecdotes (use coach's own stories)
- Their exact phrasing verbatim (adapt to coach's voice)
- Their credentials (replace with coach's real credentials)

**Always replicate:**
- The hook architecture (what type, how many sentences, where the tension sits)
- The script skeleton (the flow from hook to problem to fix to CTA)
- The CTA mechanic (if it drove DMs, drive DMs; if it drove saves, drive saves)

**The test for each script:**
- Read it aloud. Does it sound like the coach or like a generic running account?
- Is the hook confrontational or controversial enough to stop the scroll?
- Does the problem land before the fix appears?
- Is the CTA frictionless — one clear action?

---

## What Good Output Looks Like

For 5 creators × 3 top videos × 3 versions = **45 scripts**

Each creator section should have:
- A clear replication brief explaining what made each Reel work
- 3 scripts per original video, each with a different hook type
- Word counts and estimated durations for each
- A JSON block at the end ready to import

The coach should be able to take any script, read it once, and film it.
