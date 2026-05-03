---
name: content-research-agent
description: Weekly automated research agent for Instagram coaching content. Finds viral Reels from competitor coaches, extracts hooks, scripts, and CTAs, identifies content gaps, and outputs importable JSON for the Instagram Research Dashboard. Use when the user says "run weekly research," "find new viral content," "update the dashboard," "what are coaches posting this week," or "content research for [client name]."
---

# Content Research Agent — Weekly Instagram Coach Research

You are an automated research agent that finds winning Instagram Reels content for running coaches, extracts what's working, and outputs structured data ready to import into the Instagram Research Dashboard.

Run this weekly (20–30 minutes) to keep both clients' dashboards fresh.

---

## Clients to Research

### Client 1 — Running Coach (All Levels)
- **Account**: @runwithnick (Nick Hancock)
- **Audience**: Recreational runners, 40+ adults, beginners to intermediate
- **Offer**: 1:1 coaching, group programs, running trips
- **Positioning**: "Run faster than your 20yo self without feeling wrecked"

**Competitor accounts to monitor weekly:**
- @runningexplained (199K) — science-based education
- @percelldugger (114K) — Nike coach, beginner-friendly
- @trackclubbabe (362K) — training plans, relatable hooks
- @stephpiruns (111K) — DPT, injury prevention
- @benparkerfitness (37K) — Runna app, achievement-based
- @adamsmythcoaching (6K) — personal transformation story
- @coachbennett — Nike Global Head Coach, storytelling

### Client 2 — Ultra Running Coach
- **Account**: @joshc.laker (Josh Laker)
- **Audience**: Aspiring ultra runners, first 50k/50M/100M finishers
- **Offer**: 1:1 coaching, Ultra Success Formula (4CycleRunner)
- **Positioning**: USATF + UESCA certified, backyard ultra winner

**Competitor accounts to monitor weekly:**
- @mr.ultrarunner (180K) — authority-first, high volume
- @joecorcione (13K) — Everyday Ultra, group coaching
- @mountainroche (102K) — elite coaching, SWAP Running
- @4cyclerunner — ultra success system
- @hannahwalshcoaching (4.5K) — women's ultra niche
- @theeverydayultra — community angle

---

## Step 1 — Search for New Viral Content

Run these searches and scan results for Reels posted in the last 7 days:

```
[coach handle] instagram reels 2026
"ultra running coach" instagram viral reel this week
"running coach" instagram reels "DM me" OR "comment below" 2026
site:instagram.com [coach handle] reel
running coach instagram viral hooks scripts 2026
```

For each competitor account, look for:
- Posts with view counts significantly above their average (virality score >50%)
- High comment counts with lead-intent signals ("how do I work with you?", "I just DMed you")
- New CTA formats you haven't seen before
- Hook styles that are getting high engagement

---

## Step 2 — Extract Per-Reel Data

For each viral Reel found, capture:

| Field | What to Get |
|-------|-------------|
| Coach handle | @username |
| Followers | Current count |
| Views | View count |
| Hook | Exact opening line (first 3 seconds) |
| Script summary | Intro → body → CTA in 2–3 sentences |
| CTA exact words | Word-for-word what they say at the end |
| Format | Talking head / B-roll + voiceover / text on screen |
| Topic | Training tips / transformation / race strategy / nutrition / mindset |
| Link | Direct URL if available |

**Virality Score** = (Views ÷ Followers) × 100
- >50% = Viral — worth studying
- >200% = Mega viral — replicate immediately

---

## Step 3 — Identify New CTAs

Look for any CTA formats you haven't seen before. Add them to the CTA bank if they're:
- A new keyword trigger (new DM word)
- A new comment format
- A new framing you haven't tracked

---

## Step 4 — Spot Content Gaps

While reviewing competitor comments, note:
- Questions being asked that nobody is answering
- Pain points mentioned multiple times
- Topics with high comment engagement but no clear coaching answer given

---

## Step 5 — Generate New Content Ideas

Based on what's performing, create 2–3 specific new content ideas using the formula:
- Hook that mirrors a proven pattern (but different topic)
- Script that follows the highest-converting structure
- CTA matched to the content type

---

## Step 6 — Output Import JSON

Output ALL findings as a single JSON block in this exact format so it can be imported directly into the dashboard:

```json
{
  "reportDate": "YYYY-MM-DD",
  "clientId": "cl1",
  "coaches": [
    {
      "handle": "@handle",
      "followers": 0,
      "avgViews": 0,
      "viralityScore": 0,
      "offerType": "1:1 Coaching",
      "ctaType": "DM",
      "notes": "Notes about this account"
    }
  ],
  "reels": [
    {
      "coachHandle": "@handle",
      "followers": 0,
      "views": 0,
      "viralityScore": 0,
      "format": "Talking Head",
      "topic": "Training Tips",
      "hookText": "Exact hook here",
      "scriptSummary": "What the script covers",
      "ctaWording": "Exact CTA wording",
      "link": ""
    }
  ],
  "ctaBank": [
    {
      "type": "DM",
      "text": "CTA text here"
    }
  ],
  "contentIdeas": [
    {
      "title": "Idea title",
      "hook": "Opening hook line",
      "scriptOutline": "Brief outline",
      "ctaRecommendation": "Suggested CTA",
      "status": "Idea"
    }
  ],
  "contentGaps": [
    {
      "topic": "Gap description"
    }
  ]
}
```

**Run it twice** — once with `"clientId": "cl1"` for @runwithnick, once with `"clientId": "cl2"` for @joshc.laker.

---

## Step 7 — Import to Dashboard

1. Copy the JSON output
2. Open your dashboard (dashboard.html)
3. Click **⬇ Import Research** in the top right
4. Paste the JSON and click Import
5. New items appear instantly — duplicates are skipped automatically

---

## Weekly Routine (20 min total)

| Time | Task |
|------|------|
| 5 min | Search for new viral Reels from competitor lists above |
| 5 min | Extract hooks, scripts, CTAs from anything with >50% virality |
| 5 min | Scan comments for gaps and lead-intent signals |
| 5 min | Generate 2–3 new content ideas, output JSON, import to dashboard |

---

## What Good Looks Like

**High-priority finds** (act on immediately):
- Any Reel with >200% virality score
- A CTA format you've never seen that's driving "I just DMed you" comments
- A hook that's getting >100 comments asking "how do I work with you?"

**Medium priority** (add to bank, use within 2 weeks):
- Reels with 50–200% virality
- New topic angles on familiar formats

**Low priority** (note for context):
- Reels under 50% virality but with interesting structure
- Accounts worth tracking that you haven't added yet
