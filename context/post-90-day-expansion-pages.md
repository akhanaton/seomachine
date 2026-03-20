# Post-90-Day Page Expansion Strategy

This document captures page types identified as gaps in the current 90-day SEO plan. These should be built AFTER the foundational 90-day content is in place, but are documented here so nothing is lost.

**Source:** Analysis of Mehrab (@mehrab_build) SaaS page type framework, March 2026.
**Context:** The 90-day plan covers Solution Pages, Comparison Pages, Syllabus/Curriculum Pages, Blog Content, and Programmatic Content. The following page types are NOT covered but are highly relevant to ExamPilot.

---

## 1. Alternative Pages (HIGH PRIORITY)

### What They Are
Pages targeting people who are already looking for a solution but are dissatisfied with or shopping beyond a specific competitor. Different from comparison pages ("ExamPilot vs X") — alternative pages target "Best X alternatives" keywords where the searcher has already decided they want something OTHER than X.

### Why They Matter for ExamPilot
- **Highest converting page type in SaaS** — the person is actively shopping
- Our competitors (Save My Exams, Physics & Maths Tutor, PapaCambridge) are well-known but have clear weaknesses we can exploit
- Students searching "save my exams alternative" are frustrated with paywalled content or static PDFs — they're primed for what ExamPilot offers

### Specific Pages to Build

| Page Title | Target Keyword | Why They're Searching |
|---|---|---|
| Best Save My Exams Alternatives for A-Level Maths | "save my exams alternative", "save my exams free alternative" | Paywall frustration, want better features |
| Best Physics & Maths Tutor Alternatives in 2026 | "physics maths tutor alternative", "PMT alternative" | Dated UI, ad-heavy, no progress tracking |
| Best PapaCambridge Alternatives for Cambridge 9709 | "papacambridge alternative" | Poor UX, static PDFs, no learning features |
| Best Free A-Level Maths Practice Tools | "free a level maths practice", "free a level maths app" | Shopping for tools, price-sensitive |
| Best A-Level Maths Revision Apps 2026 | "best a level maths app 2026", "best revision app a level maths" | General tool shopping, listicle format |
| Best Cambridge 9709 Revision Resources | "best cambridge 9709 resources" | Exam-board specific shopping |

### How to Write Them
- **Neutral, honest tone** — actually review the competitors. What's good about them. What's lacking. Don't trash them.
- **Feature comparison table** — side-by-side features, pricing, exam board coverage
- **ExamPilot as top recommendation** — but earned through the honest comparison, not forced
- **FAQ schema** — "Is [competitor] free?", "What's better than [competitor]?"
- **CTA**: "Try ExamPilot free" or "Check your exam readiness"

### URL Structure
```
/alternatives/save-my-exams/
/alternatives/physics-maths-tutor/
/alternatives/papacambridge/
/best/free-a-level-maths-practice-tools/
/best/a-level-maths-revision-apps/
/best/cambridge-9709-resources/
```

### Expected Impact
- High-intent traffic from students actively shopping for tools
- Strong conversion rates (they're ready to switch)
- Relatively low competition (competitors aren't targeting these keywords about themselves)

---

## 2. Audience Segment Pages (MEDIUM PRIORITY)

### What They Are
Pages targeting specific audience segments with tailored messaging. Unlike our syllabus pages (which organise by exam board), these organise by WHO the student is and WHERE they are in their journey.

### Why They Matter for ExamPilot
- A resitting student has completely different pain points from a first-timer
- A tutor uses ExamPilot differently from a self-studying student
- A parent searching for their child has different decision criteria
- International students have specific concerns (time zones, exam centre access, English as second language)

### Specific Pages to Build

| Page | URL | Target Audience | Key Messaging |
|---|---|---|---|
| ExamPilot for Resitting Students | /for/resitters/ | Students who didn't get the grade they needed | "Last time didn't go as planned. This time, you'll know exactly what to fix." Focus on diagnostic (find what went wrong), targeted practice (don't waste time on topics you know), faster improvement path |
| ExamPilot for International Students | /for/international-students/ | CIE students outside UK (UAE, Pakistan, Malaysia, Singapore, Nigeria, etc.) | "Cambridge 9709 prep that works wherever you are." Focus on 24/7 Ask Sparky access (no teacher outside school hours), Cambridge-specific content, understanding different exam windows |
| ExamPilot for A-Level Maths Tutors | /for/tutors/ | Private tutors and tutoring centres | "See exactly where each student is struggling." Focus on dashboard analytics, progress tracking across multiple students, time-saving on diagnostic work |
| ExamPilot for Parents | /for/parents/ | Parents of A-Level Maths students | "Your child's exam readiness, backed by data." Focus on Exam Readiness Index (concrete predicted grade), progress visibility, investment justification |
| ExamPilot for Self-Study Students | /for/self-study/ | Students studying without regular tutor support | "Your AI study partner for A-Level Maths." Focus on Ask Sparky, structured practice path, no teacher required |

### How to Write Them
- **Lead with the specific pain point** of that segment
- **Tailored value propositions** — same features, different emphasis
- **Social proof specific to that segment** (once available) — "87% of resitting students improved their grade"
- **Segment-specific FAQs** — "Can I use ExamPilot if I'm studying independently?", "Does ExamPilot work for Cambridge international exam centres?"
- **CTA matched to segment** — tutors get "Set up your student dashboard", parents get "See your child's readiness score"

### URL Structure
```
/for/resitters/
/for/international-students/
/for/tutors/
/for/parents/
/for/self-study/
```

### Expected Impact
- Captures long-tail "A-Level Maths for [segment]" searches
- Higher conversion than generic pages (messaging speaks directly to their situation)
- Useful for both organic search AND as landing pages for targeted social/ad campaigns later

---

## 3. Location/Country Pages (HIGH PRIORITY — pSEO Opportunity)

### What They Are
Pages targeting students in specific countries or regions where Cambridge International and Edexcel are used. This is a **programmatic SEO (pSEO)** opportunity — one template, many pages, each with location-specific context.

### Why They Matter for ExamPilot
- **Cambridge International exams are taken in 160+ countries.** Students in each country search with location context.
- **Nobody in our space is targeting geographic keywords.** Save My Exams, PMT, PapaCambridge are all UK-centric. Zero competition for "Cambridge 9709 revision UAE" or "A-Level Maths prep Pakistan."
- **Location changes buying intent.** A student in Dubai has different exam dates, different school holidays, different access to tutors than a student in London. Location-specific pages can address these differences.
- **LLM capture.** When someone asks ChatGPT "best A-Level Maths app for students in Malaysia", we need a page that captures that query.

### Countries/Regions to Target (Priority Order)

**Tier 1 — Largest Cambridge International markets:**
| Country | Why | Local Context to Include |
|---|---|---|
| UAE (Dubai, Abu Dhabi) | Huge CIE population, high spending power | International schools, May/June + Oct/Nov windows, competitive university applications |
| Pakistan | One of the largest CIE markets globally | British Council exam centres, high-stakes university entrance (LUMS, AKU, etc.), study resources scarce |
| Malaysia | Significant CIE presence | SPM vs Cambridge pathway, local tuition culture, bilingual study needs |
| Singapore | CIE and Edexcel both present | Highly competitive education system, tuition-heavy culture, A-Level as pathway to NUS/NTU |
| Nigeria | Growing CIE adoption | British Council centres, limited local digital resources, mobile-first audience |
| Bangladesh | Large CIE market | Dhaka/Chittagong exam centres, English as study language challenges |
| UK | Home market for Edexcel | School-based study, teacher access, UCAS context |
| India | Growing CIE presence | ISC vs CIE distinctions, competitive JEE/NEET-adjacent students |

**Tier 2 — Secondary markets:**
| Country | Notes |
|---|---|
| Egypt | CIE and Edexcel presence |
| Kenya | East African CIE hub |
| Sri Lanka | CIE market |
| Hong Kong | CIE and Edexcel |
| Oman | Gulf CIE market |
| Qatar | Gulf CIE market |
| Bahrain | Gulf CIE market |
| Kuwait | Gulf CIE market |
| Saudi Arabia | Growing international school sector |
| South Africa | CIE and local curriculum competition |
| Zimbabwe | Significant CIE market |
| Zambia | CIE presence |
| Trinidad & Tobago | Caribbean CIE market |
| Jamaica | Caribbean CIE market |

### Template Structure (One Template, Many Pages)

Each location page follows this template:

```
# A-Level Maths Revision for Students in [Country]

## Why [Country] Students Choose ExamPilot
[2-3 sentences about the local education context — exam boards used, exam windows, challenges]

## Cambridge 9709 in [Country]
- Exam centres: [list major cities/centres]
- Exam windows: May/June and October/November
- [Local-specific notes: British Council registration, school vs private candidate, etc.]

## Edexcel IAL in [Country]  (if applicable)
- [Same structure]

## How ExamPilot Helps Students in [Country]
- 24/7 AI tutor access (Ask Sparky) — no waiting for school hours
- Study on your schedule — works across all time zones
- Cambridge 9709 and Edexcel IAL specific — not generic maths
- Track your Exam Readiness Index — know exactly where you stand

## Features That Matter for [Country] Students
[Highlight features most relevant to this market — e.g., for Pakistan: AI tutor access outside school hours; for Singapore: detailed analytics for competitive positioning]

## Exam Dates for [Country]
[Specific Cambridge/Edexcel exam windows relevant to this location]

## FAQs for [Country] Students
- Can I use ExamPilot from [Country]?
- Does ExamPilot cover the [Country] Cambridge 9709 syllabus?
- What internet speed do I need?
- Is ExamPilot available in [local language]? (honest answer: English only currently)

## Start Preparing Now
[CTA: Join the waitlist / Try ExamPilot free]
```

### URL Structure
```
/countries/uae/
/countries/pakistan/
/countries/malaysia/
/countries/singapore/
/countries/nigeria/
/countries/uk/
etc.
```

Or alternatively, nested under exam board:
```
/cambridge/9709/uae/
/cambridge/9709/pakistan/
/edexcel/ial/uk/
```

### How to Build at Scale (pSEO)
1. Create the template once with variable fields ([Country], [Cities], [Exam Centres], [Local Context])
2. Research 2-3 unique local facts per country (exam centres, dates, local education notes)
3. Generate pages using the template — AI can draft, human reviews for accuracy
4. **Critical:** Each page must have SOME unique content (local context, local exam dates, local FAQs). Google penalises thin programmatic pages with no unique value.
5. Add FAQPage schema to every location page

### Expected Impact
- **Hundreds of pages** targeting zero-competition keywords
- Captures LLM queries with geographic context
- Builds topical authority across Cambridge International markets
- Students in these countries currently have NO dedicated resource — we'd be first movers
- Each page is a potential entry point for conversion

---

## 4. Free Tool Pages (MEDIUM-HIGH PRIORITY)

### What They Are
Standalone free tools that provide immediate value without requiring sign-up. They serve as link magnets (other sites link to useful tools), conversion funnels (use the free tool → see the value → sign up for full access), and LLM citation targets.

### Why They Matter for ExamPilot
- Free tools get organic backlinks (the #1 thing our plan struggles to generate cheaply)
- They demonstrate the product's value before commitment
- They create a natural upgrade path: free tool → "want more? sign up"
- They rank well for "free [X] tool" keywords

### Specific Tools to Build

| Tool | What It Does | Target Keyword | Conversion Path |
|---|---|---|---|
| **Predicted Grade Calculator** | Enter your recent test scores by topic, get an estimated A-Level grade | "a level maths predicted grade calculator", "predicted grade calculator" | "Want a more accurate prediction? ExamPilot tracks your progress over time." |
| **Exam Readiness Quiz** | 10 diagnostic questions → shows your strongest and weakest topics | "a level maths diagnostic test free", "am i ready for a level maths" | "See your full diagnostic? Sign up for ExamPilot." |
| **Study Plan Generator** | Enter exam date + current topics → generates week-by-week plan | "a level maths study plan", "revision timetable generator" | "Want a plan that adapts as you improve? Try ExamPilot." |
| **Topic Coverage Checker** | Paste your revision notes/list → see which syllabus topics you've covered vs missed | "cambridge 9709 syllabus checklist", "a level maths topic list" | "Found gaps? ExamPilot targets them automatically." |
| **Ask Sparky (Standalone)** | Free AI maths tutor — ask one question for free | "free a level maths tutor", "ai maths help" | "Loved Sparky? Get unlimited access with ExamPilot." |

### URL Structure
```
/tools/predicted-grade-calculator/
/tools/exam-readiness-quiz/
/tools/study-plan-generator/
/tools/topic-checker/
/tools/ask-sparky/
```

### How to Build
- Each tool needs its own landing page with:
  - Clear headline explaining what the tool does
  - The interactive tool itself
  - SEO content below the tool (500-1000 words explaining the methodology)
  - FAQ schema
  - CTA to sign up for full ExamPilot access
- Tools should work without sign-up (reduce friction)
- Optionally gate the detailed results behind email capture

### Expected Impact
- Organic backlinks from education resource pages
- High-volume top-of-funnel traffic
- Email list building (if gating detailed results)
- Product demonstration without commitment
- LLM citation ("Use ExamPilot's free predicted grade calculator at...")

---

## Implementation Priority

| Phase | Page Type | Number of Pages | Effort | Impact |
|---|---|---|---|---|
| **Post-90-Day Phase 1** | Alternative Pages | 6 pages | Low (content only) | High (conversion) |
| **Post-90-Day Phase 1** | Location Pages (Tier 1) | 8 pages | Medium (research per country) | High (untapped market) |
| **Post-90-Day Phase 2** | Free Tool Pages | 3-5 tools | High (engineering + content) | High (backlinks + conversion) |
| **Post-90-Day Phase 2** | Audience Segment Pages | 5 pages | Low (content only) | Medium (long-tail capture) |
| **Post-90-Day Phase 3** | Location Pages (Tier 2) | 14+ pages | Low (template exists) | Medium (pSEO scale) |

---

**Note:** This document is a reference for post-90-day planning. Do not start building these pages until the foundational 90-day content is in place. The 90-day plan builds the domain authority and content foundation that makes these expansion pages effective.
