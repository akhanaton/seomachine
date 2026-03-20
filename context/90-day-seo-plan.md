# Exampilot: 90-Day SEO & Organic Growth Strategy (2026 Edition)

## 1. Foundational Setup — Days 1–14

### Technical SEO Checklist

Your technical foundation determines whether everything else you build will rank. Get this right once, then leave it alone.

#### Site Architecture

* Use a flat architecture: no page should be more than 3 clicks from the homepage
* Canonical URL structure: exampilot.com/[subject]/[exam-board]/[topic] — e.g., /gcse/edexcel/maths and /a-level/cambridge/biology
* One domain, no subdomains for blog or app (use exampilot.com/blog/ not blog.exampilot.com) — subdomains split domain authority
* Implement HTTPS from day one; Google confirmed it as a ranking signal
* Separate your marketing site from the app login (app.exampilot.com for the SaaS product is fine, but all SEO-targeted content lives on the root domain)

#### Core Web Vitals

LCP (Largest Contentful Paint) must be under 2.5s, INP (Interaction to Next Paint) under 200ms, CLS (Cumulative Layout Shift) under 0.1. These are confirmed ranking factors in 2026 — sites with excellent CWV scores see up to 40% better search visibility. For a NextJS/Vercel stack, you're well-positioned: use Next Image for automatic image optimization, enable font optimization, and eliminate render-blocking third-party scripts at launch.

#### Mobile-First Indexing

Google indexes the mobile version of your site exclusively. Every page must render fully on mobile without content truncation. Use `<meta name="viewport" content="width=device-width, initial-scale=1">` and test every template in Google's Mobile-Friendly Test.

#### Schema Markup (Priority items for EdTech)

* EducationalOrganization schema on homepage and About page
* Course schema on all subject/exam prep landing pages
* FAQPage schema on all FAQ sections (critical for AI Overviews and featured snippets)
* Article schema with author, datePublished, dateModified on all blog content
* BreadcrumbList schema sitewide for crawl depth and SERP display
* HowTo schema on step-by-step study guides

#### Indexing Hygiene

* robots.txt: block /app/, /dashboard/, /admin/, all auth routes
* XML sitemap at exampilot.com/sitemap.xml, submitted to GSC within 48 hours of launch
* Set hreflang tags if you add any Spanish/European language variants later
* 301 redirect www to non-www (or vice versa) — pick one and enforce it sitewide

#### Domain & URL Structure

The cleanest URL architecture for your Cambridge 9709 & Edexcel IAL launch:

```
exampilot.com/                                    → Homepage (brand + CTA)
exampilot.com/cambridge/9709/                     → Cambridge 9709 Hub (pillar)
exampilot.com/cambridge/9709/pure-1/              → 9709 Pure 1 sub-pillar
exampilot.com/cambridge/9709/pure-1/integration/  → Topic page
exampilot.com/cambridge/9709/pure-3/              → 9709 Pure 3 sub-pillar (future)
exampilot.com/edexcel/ial/pure-1/                 → Edexcel IAL Pure 1 Hub
exampilot.com/edexcel/ial/pure-2/                 → Edexcel IAL Pure 2 Hub
exampilot.com/edexcel/ial/pure-1/differentiation/ → Topic page
exampilot.com/past-papers/9709/                   → Programmatic 9709 past papers
exampilot.com/past-papers/edexcel-ial/            → Programmatic Edexcel IAL papers
exampilot.com/blog/                               → Blog (topical authority content)
```

**Future expansion path:** When you add GCSE Maths, Statistics, Mechanics, or other A-Level subjects, they slot cleanly into this hierarchy:
- `exampilot.com/cambridge/igcse/maths/`
- `exampilot.com/edexcel/gcse/maths/`
- `exampilot.com/cambridge/9709/statistics-1/`

Keep URLs lowercase, hyphen-separated, no stop words, under 60 characters. Avoid including dates in URLs — exam prep content should appear evergreen.

### GSC & PostHog Setup

#### Google Search Console

* Verify via DNS TXT record (most reliable method)
* Submit XML sitemap immediately
* Set up email alerts for manual actions, crawl errors, and security issues
* Keep GSC data separate (PostHog doesn't have native GSC integration like GA4, but you can correlate data manually or via API)
* Enable the URL Inspection API for programmatic indexing checks later (Section 7)

#### PostHog

* Enable autocapture for automatic tracking of clicks, page views, and form submissions
* Create custom events: trial_signup, subject_selected, practice_test_started, question_answered
* Set up cohorts for user segmentation: visited_gcse_maths, started_trial, abandoned_signup
* Configure session recordings to watch how students interact with exam prep content (invaluable for UX optimization)
* Enable feature flags for A/B testing different CTAs and content formats
* Use PostHog's built-in event validation tools to verify event firing during setup

### Budget Tool Stack ($250/month)

| Tool | Monthly Cost | Role |
|------|--------------|------|
| Google Search Console | Free | Indexing, ranking data, crawl errors, Core Web Vitals monitoring |
| PostHog | Free (up to 1M events/month) | Product analytics, event tracking, session recordings, funnel analysis, feature flags, A/B testing |
| Mangools Suite (KWFinder + SERPWatcher + LinkMiner) | $29 | Keyword research, rank tracking (up to 200 keywords), competitor backlink analysis |
| Screaming Frog SEO Spider | Free (up to 500 URLs) | Technical site audit, crawl analysis, internal link mapping |
| RankMath Pro (if WordPress) or Schema Pro | $6–$8 | Schema markup automation, sitemap, robots.txt management |
| Ahrefs Webmaster Tools | Free | Backlink monitoring for your own domain, basic site audit |
| Surfer SEO | $89 (Content Editor) | On-page optimization scoring per article, NLP keyword density, competitor content benchmarking |
| Notion or Obsidian | Free | Content calendar, brief storage, keyword cluster maps |
| Featured.com (HARO replacement) | Free–$19 | Journalist source requests for link building |
| Claude Opus/Sonnet (already owned) | ~$20/month API costs | Content briefs, first-draft generation, cluster mapping, internal linking automation |
| Buffer or Metricool | Free tier | Social scheduling for wife's distribution work |

**Total:** ~$176–$198/month, leaving $52–$74 buffer for ad-hoc tools, domain renewals, or Surfer overage.

⚠️ If budget is tight: Drop Surfer SEO in Month 1. Use free tools (Google NLP API + Claude) to approximate content scoring. Add Surfer in Month 2 when you have content volume to justify it.

## 2. Keyword & Topical Authority Strategy

### Keyword Research for Exam Prep/EdTech

**Exampilot's Initial Focus:** Cambridge 9709 and Edexcel IAL Pure Maths.

This focused launch strategy is significantly stronger than broad GCSE coverage. Your primary competitors (PapaCambridge, Save My Exams, Physics & Maths Tutor) are static PDF repositories with no adaptive AI practice — exactly where Exampilot differentiates. The international A-Level audience (UAE, Pakistan, Malaysia, Singapore, Nigeria) is underserved by UK-centric tools.

#### Step 1 — Map the taxonomy (Cambridge 9709 & Edexcel IAL specific)

Build a spreadsheet focused on your launch scope:

**Cambridge 9709 cluster:**
- **Paper codes:** 9709/12, 9709/13 (Pure 1), 9709/32, 9709/33 (Pure 3)
- **Topics (Pure 1):** Functions, Quadratics, Coordinate Geometry, Circular Measure, Trigonometry, Vectors, Differentiation, Integration
- **Topics (Pure 3):** Algebra, Logarithms, Trigonometry, Differentiation, Integration, Numerical Methods, Vectors, Differential Equations, Complex Numbers
- **Modifiers:** past papers, worked solutions, topic questions, revision notes, exam tips, mark scheme, 9709 P1 2023, 9709/12 past papers

**Edexcel IAL cluster:**
- **Paper codes:** WMA11 (Pure 1), WMA12 (Pure 2)
- **Topics (Pure 1 & 2):** Algebra, Functions, Coordinate Geometry, Trigonometry, Exponentials/Logarithms, Differentiation, Integration, Vectors
- **Modifiers:** Edexcel IAL Pure 1 past papers, WMA11 topic questions, Edexcel International A Level worked examples

**Critical insight:** Students search by paper code (9709, WMA11, WMA12). These are zero-competition, high-intent keywords that only niche tools target. Example searches: "9709 P1 integration questions 2022", "WMA11 past papers by topic", "Cambridge 9709 Pure Maths worked solutions".

This focused taxonomy generates 200-300 highly-targeted seed keywords. Feed these into KWFinder.

#### Step 2 — Mine Reddit and student communities (International focus)

The subreddits r/alevel, r/Edexcel, and r/alevelmaths are gold mines for exact student language. International students frequently ask "where to find Edexcel IAL topic questions other than SME and PMT" or "best resource for Cambridge 9709 Pure 1". Use Google `site:reddit.com/r/alevel [keyword]` and `site:reddit.com/r/Edexcel [keyword]` to surface real questions.

**Key communities to monitor:**
- r/alevel (international + UK A-Level students, 9709 mentioned frequently)
- r/Edexcel (Edexcel IAL students specifically)
- r/alevelmaths (maths-specific, active exam question threads)
- Facebook Groups: "Cambridge A Level Mathematics 9709" (large South/SE Asian communities)
- YouTube comment sections on 9709 tutorial channels (many have 50K-200K subscribers)

#### Step 3 — Identify low-competition opportunities

For a brand-new domain, filter KWFinder results by:

- Keyword Difficulty (KD) ≤ 30 (Mangools scale)
- Monthly search volume ≥ 200 (meaningful, not too competitive)
- Informational intent (how-to, what is, tips, guide)

Avoid any keyword where the top 3 results are BBC Bitesize, Revision World, CGP Books, or Khan Academy — these have DR 70–90 and are near-impossible to displace within 90 days.

**Low-competition sweet spots for Exampilot (Cambridge 9709 & Edexcel IAL):**

- Paper code specific: "9709 P1 integration questions," "WMA11 past papers by topic," "Cambridge 9709 Pure 1 differentiation."
- Topic + paper: "Cambridge 9709 Pure 1 trigonometry revision", "Edexcel IAL Pure 2 vectors worked examples"
- AI-specific angles: "best AI tool for Cambridge 9709 revision", "adaptive practice for Edexcel IAL Pure Maths"
- Comparison: "Exampilot vs Save My Exams", "Exampilot vs PapaCambridge"
- Mistake-based: "common mistakes in 9709 P1 integration", "how to pass Cambridge 9709 Pure Maths"
- International student queries: "9709 Pure Maths resources for international students"

### Topic Cluster / Pillar Architecture

Build one pillar page per exam specification, supported by 8–12 spoke articles each. **Launch with Cambridge 9709 first** (your deepest content moat), then Edexcel IAL.

**Example: Cambridge 9709 Pure Mathematics 1 Cluster**

```
PILLAR: "Cambridge 9709 Pure Mathematics 1: Complete Revision Guide" (4,000+ words)
│
├── SPOKE: "9709 P1 Differentiation: Complete Topic Guide & Practice Questions"
├── SPOKE: "9709 P1 Integration: Exam Tips & Worked Solutions"
├── SPOKE: "Cambridge 9709 Functions & Graphs: Everything You Need to Know"
├── SPOKE: "9709 Pure 1 Trigonometry: Common Mistakes & How to Avoid Them"
├── SPOKE: "Cambridge 9709 Vectors: Complete Revision Notes"
├── SPOKE: "9709 P1 Coordinate Geometry: Past Paper Questions by Topic"
├── SPOKE: "How to Pass Cambridge 9709 Pure Mathematics 1"
└── SPOKE: "9709 Past Papers: Complete Paper Code Guide (9709/12, 9709/13)"
```

**Example: Edexcel IAL Pure 1 Cluster**

```
PILLAR: "Edexcel IAL Pure Mathematics 1: Complete WMA11 Revision Guide" (4,000+ words)
│
├── SPOKE: "Edexcel IAL Pure 1 Differentiation: WMA11 Topic Questions"
├── SPOKE: "Edexcel IAL Pure 1 Integration: Worked Examples & Practice"
├── SPOKE: "WMA11 Trigonometry: Complete Revision Notes"
├── SPOKE: "Edexcel IAL Pure 1 Algebra: Past Paper Questions by Topic"
├── SPOKE: "WMA11 vs WMA12: Key Differences Between Pure 1 & Pure 2"
├── SPOKE: "Edexcel International A Level Pure 1 Past Papers Guide"
├── SPOKE: "Common Mistakes in Edexcel IAL Pure 1 Exams"
└── SPOKE: "Best Resources for Edexcel IAL Pure Mathematics Revision"
```

Every spoke links back to the pillar. The pillar links out to all spokes. This architecture signals topical authority to Google — you're not just publishing random articles, you're owning the 9709 and Edexcel IAL Pure Maths niche.

### Keyword Prioritization Framework

**Month 1 — Target paper code + topic keywords (KD ≤ 20):**

These are near-zero competition, high-intent keywords. Examples: "9709 P1 integration questions," "WMA11 past papers by topic," "Cambridge 9709 Pure 1 differentiation." Your brand can rank for these within 2-4 weeks. Also target "AI + Cambridge 9709" and "AI + Edexcel IAL" keywords where you have genuine product differentiation.

**Month 2 — Target informational long-tail (KD ≤ 25):**

Question-type and mistake-based content specific to 9709 and Edexcel IAL. Examples: "common mistakes in 9709 P1 integration," "how to pass Cambridge 9709 Pure Maths," "Edexcel IAL Pure 1 exam tips." These rank faster because competition is thin blogs, not authority sites.

**Month 3 — Target pillar-level pages (KD 25–35):**

By Month 3 you'll have internal link equity and some backlinks. Launch the comprehensive pillar pages: "Cambridge 9709 Pure Mathematics 1: Complete Revision Guide" and "Edexcel IAL Pure 1: Complete WMA11 Guide." These compete directly with Save My Exams and Physics & Maths Tutor but with superior AI-enhanced, interactive content.

## 3. On-Page SEO

### Title Tags, Meta Descriptions & Headers

**Title tag formula:**

`[Primary Keyword] — [Benefit or Modifier] | Exampilot`

**Example:** Cambridge 9709 Pure 1 Revision: Complete Guide 2026 | Exampilot

- Keep under 60 characters
- Lead with the target keyword, not your brand name (brand goes last on non-homepage pages)
- Include year for time-sensitive content ("2026") — it improves CTR by approximately 5–15%

**Meta descriptions:**

- 120–155 characters
- Include a clear value proposition and a soft CTA
- **Example:** "Master Cambridge 9709 Pure Maths with AI-powered practice questions. Covers all P1 topics with instant feedback. Free to start."

**Header hierarchy:**

- One H1 per page (contains primary keyword naturally)
- H2s for major sections (include secondary keywords and question variations)
- H3s for sub-points
- Never use headers purely for visual styling — Google reads header hierarchy for content structure

### Internal Linking Strategy

This is the single highest-leverage on-page tactic for a new site with no backlinks — internal links distribute the authority you're building. Rules:

- Every new article must link to its parent pillar page and 2–3 topically related spokes
- Pillar pages must link to all their spokes
- Use descriptive anchor text (not "click here" — use "Cambridge 9709 Pure 1 revision guide")
- Limit to 5–8 internal links per 1,000 words — don't over-link
- Build an internal link map in Notion: a simple table of [page URL] → [links to] → [anchor text]
- Audit with Screaming Frog monthly to find orphan pages (pages with no internal links pointing to them)

### Content Depth & Format

For exam prep content, the winning format in 2026 is:

- **Word count:** 1,500–2,500 for spoke articles; 3,000–5,000 for pillars. Do not pad — Google's Helpful Content system actively demotes content that is long but low-value.
- **Structure non-negotiables:** Table of contents for any article over 1,500 words; FAQ section at the bottom of every page (minimum 3 questions in FAQPage schema); at least one comparison table where applicable; numbered lists for step-by-step content
- **Original elements:** Include one unique element per article that cannot be found elsewhere — a custom practice question, a study schedule template, a topic-specific checklist, or a brief analysis of past paper trends. This is your E-E-A-T differentiator.

### Page Experience Signals

Core Web Vitals targets: LCP < 2.5s, INP < 200ms, CLS < 0.1. On a NextJS/Vercel stack these are achievable by default if you:

- Never load fonts from Google Fonts without font-display: swap
- Lazy-load all images below the fold
- Avoid layout shifts from ads or embeds by pre-defining dimensions
- Use server-side rendering (SSR) or static generation (SSG) for content pages — not client-side rendering

CWV are not a primary ranking factor in isolation, but act as a tie-breaker in competitive queries and a multiplier on everything else.

## 4. AI-Assisted Content Creation Workflow

### Google's Official Policy on AI Content — Fact vs. Myth

**The fact:** Google does not penalize AI-generated content for being AI-generated. Google's official guidance since February 2023, reinforced through every subsequent update including the March 2025 Core Update, states clearly: "Our focus on the quality of content, rather than how content is produced, is a useful guide that has helped us deliver reliable, high quality results to users for years."

**The myth to kill:** That unedited AI output is safe if it "sounds human." It is not. The risk is not AI detection — it is that unedited AI output consistently fails Google's Helpful Content evaluation: it lacks first-hand experience signals, contains generic claims without evidence, and cannot demonstrate the E-E-A-T markers that human review adds.

**The safe zone in 2026:**

| Practice | Risk Level |
|----------|------------|
| Claude draft → human review → fact-check → personal insight added → publish | Low (treated as human content) |
| Claude draft → light edit → publish | Medium (Helpful Content demotion risk over time) |
| Bulk AI output → auto-publish at scale | High (Scaled Content Abuse policy, manual action risk) |

### Human-in-the-Loop Workflow with Claude

**Step 1 — Keyword Clustering (Claude Opus)**

Paste your 50–100 seed keywords into Claude with this prompt:

> "You are an SEO content strategist specializing in UK exam preparation (GCSE, A-Level). Group the following keywords into topic clusters. Each cluster should have one pillar page topic and 6–10 spoke article topics. Indicate the likely search intent (informational, navigational, transactional, commercial) for each. Keywords: [paste list]"

**Output:** a structured cluster map you paste into Notion.

**Step 2 — Content Brief Generation (Claude)**

For each article, run:

> "Create a detailed SEO content brief for the article: '[Target Title]'. Target keyword: '[keyword]'. Secondary keywords: [list]. Audience: UK secondary school students aged 14–18 studying [subject]. Include: recommended H2/H3 structure, key questions to answer, recommended word count, suggested original element (practice question, checklist, or table), internal link targets from this list: [existing pages], and a FAQ section with 4 questions students commonly ask."

**Step 3 — First Draft Generation (Claude)**

> "Write a [X]-word article based on this content brief. Write in a clear, encouraging, student-friendly tone. Do not use filler phrases like 'In this article...' or 'It's important to note that...'. Include concrete examples from real exam questions where possible. Flag any section where you are uncertain about factual accuracy with [VERIFY]."

**Step 4 — Human Quality Layer (Critical)**

This is your wife's content role or your own. For every article before publishing:

- ✅ Verify all factual claims (especially exam board-specific details — these change annually)
- ✅ Add one personal or original insight the AI couldn't generate (a common student mistake you've observed, a unique analogy, a real example)
- ✅ Replace any generic AI phrasing with specific, concrete language
- ✅ Add a visible author byline with credentials (e.g., "Reviewed by [Name], EdTech specialist with 5+ years in UK exam prep")
- ✅ Check all FAQPage schema is correctly implemented
- ✅ Confirm all internal links are live and pointing to published URLs

**Step 5 — Internal Link Automation (Claude Code)**

Maintain a JSON file of all published articles with their URLs and target keywords. Use Claude Code to:

> "Given this list of published articles and their primary keywords, generate internal link recommendations for the new article '[title]' targeting '[keyword]'. For each recommendation, provide the anchor text and the URL to link to."

### Publishing Cadence

For a 1–2 person team: 3 articles per week maximum. Quality over velocity is not a platitude in 2026 — it is the empirical reality of the Helpful Content system. Two solid, well-researched 2,000-word articles beat six generic 1,000-word posts every time.

**Recommended weekly rhythm:**

## 5. GEO — Generative Engine Optimization

### What GEO Is and Why It Matters for Exampilot

GEO is the practice of structuring your content so that AI-powered search engines (Google AI Overviews, ChatGPT, Perplexity) extract, cite, and surface your content in generated answers. Unlike traditional SEO where success = ranking #1, GEO success = being cited in a zero-click AI answer that is seen by hundreds of thousands of users who never click a blue link.

For Exampilot, this matters acutely. Students increasingly ask ChatGPT "what's the best app for GCSE revision?" or Perplexity "how do I revise A-level biology effectively?" — and the answer they receive is the discovery moment, not the Google SERP.

### On-Page Tactics for AI Citation

#### 1. Write definitive, extractable answers

AI systems prefer content that answers a question directly in the first 2–3 sentences of a section, then elaborates. Format your H2 sections so the first sentence after the heading is the complete answer:

##### H2: How long should you revise for Cambridge 9709 Pure 1?

"Most Cambridge 9709 Pure 1 students should revise for 60–90 minutes per session, 4–5 sessions per week in the 8–10 weeks before their exam. This equates to approximately 30–40 total hours of focused revision for P1."

This "answer-first" structure is extractable by AI without needing surrounding context.

#### 2. Structured data and semantic clarity

Implement FAQPage, HowTo, and DefinedTerm schema markup. AI systems crawl structured data directly. Every FAQ answer should be self-contained (answerable without the question context).

#### 3. Entity optimization

Mention the specific exam boards, subject names, and qualification names explicitly and consistently: "Cambridge 9709 Pure Mathematics 1," "Edexcel IAL Pure 1 WMA11," "Cambridge International A Level 9709." AI search engines use entity recognition; unambiguous entity mentions increase citation probability.

**For Cambridge 9709 and Edexcel IAL content:** Always include the paper code (9709, WMA11, WMA12) and explicitly state "aligned to Cambridge 9709 syllabus (2023–2025)" or "Edexcel IAL specification WMA11/WMA12" — these are the exact phrases Quality Raters and AI systems look for to verify authority.

#### 4. Cite your sources and data

Content that cites official sources (Ofqual, exam board websites, research papers) is treated as more authoritative by AI models. Include one cited statistic or external reference per major section.

#### 5. Brand mention seeding

Actively mention "Exampilot" in community discussions, forum posts, and guest articles so that AI training data and retrieval-augmented generation (RAG) systems begin associating your brand with exam prep queries. This is a long game but starts now.

#### 6. Conversational long-tail targeting

AI search queries are naturally conversational: "what's the difference between AS level and A level" rather than "AS level vs A level." Write FAQ content in the exact phrasing students would speak to an AI assistant. Use Answer The Public (free tier) to harvest question formats.

## 6. Link Building & Authority Building

### White Hat Strategies for a New Domain

Link building is the highest-friction, lowest-automatable part of your strategy. Expect 90 days of consistent effort to build 20–30 quality referring domains. That is realistic and sufficient to begin meaningfully competing for mid-difficulty keywords.

#### Tactic 1: Digital PR with Original Data (Highest ROI)

Create one original data piece per month — e.g., "Exampilot 2026 Student Revision Survey: How 1,000 GCSE Students Prepare for Exams." Distribute via Featured.com, Qwoted, and direct outreach to education journalists at The Guardian, TES (Times Educational Supplement), and Schools Week. A single placement in TES can yield a DR 70+ backlink.

How to create survey data without a large user base: use Google Forms + Reddit (offer a small incentive in r/GCSE), or partner with a school or tutoring center for data access.

#### Tactic 2: HARO/Journalist Outreach Alternatives

HARO is now owned by Cision and degraded in quality. Better alternatives for 2026:

* **Featured.com** (free tier available): curated journalist requests with better spam filtering
* **Qwoted:** higher-quality journalist network, vetted sources
* **#journorequests on Twitter/X:** real-time journalist source requests; monitor with a saved search for "exam," "education," "revision," "GCSE," "students"

Respond to 3–5 journalist queries per week. Your expertise angle: AI in education, exam preparation methods, student mental health around exams. These are evergreen press topics.

#### Tactic 3: Resource Page Link Building

Target pages titled "GCSE revision resources," "A-Level study tools," "best apps for students" on:

* University access/widening participation pages (high DR, education-relevant)
* School library resource pages
* Independent tutoring blogs
* Parent/student forum directories

Use KWFinder or Google `intitle:"resources" "GCSE revision" OR "A level revision"` to find candidates. Email template:

> "Hi [Name], I noticed you link to [existing resource] on your revision tools page. We've just launched Exampilot, an AI-powered adaptive exam prep tool specifically for GCSE/A-Level students. We'd love to be considered for inclusion — happy to share a free educator account for your review. [URL]"

#### Tactic 4: Strategic Guest Posting

Target education-adjacent blogs with DR 30–60: tutoring business blogs, edtech opinion sites, UK parent/student communities. Pitch one data-backed article per month. Topics that earn acceptance: "How AI is changing GCSE revision," "5 evidence-based revision techniques that actually work."

#### Tactic 5: Community-Based Links

Answer questions on r/GCSE, r/6thForm genuinely. Reddit no-follows links, but it drives referral traffic and earns brand mentions that feed AI retrieval systems. Occasionally link to a genuinely useful resource page when directly relevant — never spam.

### Realistic Link Velocity

* **Month 1:** 3–5 referring domains (mostly community mentions + Featured.com)
* **Month 2:** 8–15 referring domains (guest posts + resource pages)
* **Month 3:** 15–30 referring domains
* DR 15–25 in Ahrefs Webmaster Tools

Target DR 20–25 by day 90. This is achievable and sufficient to rank for KD 20–35 keywords.

### Explicitly Avoid These

## 7. Programmatic & Scalable Content

### Opportunities in Exam Prep (Cambridge 9709 & Edexcel IAL Focus)

Programmatic SEO is exceptionally well-suited to Cambridge 9709 and Edexcel IAL because the content taxonomy is precisely defined by the exam boards. This is your biggest single SEO opportunity.

#### Opportunity 1: Past Paper Landing Pages (Highest Priority)

**Cambridge 9709:**
* **URL pattern:** `/past-papers/9709/[paper-code]/[year]/`
* **Example:** `/past-papers/9709/12/2023/`, `/past-papers/9709/32/2022/`
* **Data source:** Link to official Cambridge exam board PDFs. Add unique value: AI-generated difficulty rating, topic breakdown, worked-solution walkthrough summary, and CTA to practice that exact paper type in Exampilot.
* **Scale:** ~30-45 pages per paper type (P1: 9709/12, 9709/13; P3: 9709/32, 9709/33) × 16 years = 120-180 pages

**Edexcel IAL:**
* **URL pattern:** `/past-papers/edexcel-ial/[paper-code]/[year]/`
* **Example:** `/past-papers/edexcel-ial/wma11/2023/`, `/past-papers/edexcel-ial/wma12/2022/`
* **Scale:** ~30-45 pages per paper code × 2 papers = 60-90 pages

**Critical advantage:** Students literally search "9709/12 past papers 2023" or "WMA11 2022 paper". These paper code keywords have near-zero competition and will index within 2-4 weeks.

#### Opportunity 2: Paper × Topic Landing Pages

* **URL pattern:** `/cambridge/9709/pure-1/[topic]/` or `/edexcel/ial/pure-1/[topic]/`
* **Example:** `/cambridge/9709/pure-1/integration/`, `/edexcel/ial/pure-1/differentiation/`
* **Template structure:** topic definition, key formulas, exam tips, common mistakes, 2-3 worked examples, practice question CTA
* **Scale:** 8 topics × 2 papers (9709 P1, Edexcel IAL P1) = 16 core pages, expandable to 30-40 as you add P3 and Pure 2

**Unique value per page:** An AI-generated difficulty rating, a worked-solution walkthrough summary, and a direct CTA to practice that exact topic in Exampilot's adaptive engine. This is differentiation that PapaCambridge and Physics & Maths Tutor cannot match.

#### Opportunity 3: "Compare Exam Prep Tools" Pages

* **URL pattern:** `/vs/[competitor]/`
* **Example:** `/vs/save-my-exams/`, `/vs/papacambridge/`, `/vs/physics-maths-tutor/`
* These capture high-intent commercial comparison searches from students actively evaluating tools. Thin competition for Cambridge 9709 and Edexcel IAL specific comparisons.

### Avoiding Thin Content Penalties

The critical rule: every programmatically generated page must have at least one element of unique, non-template value. The Google Helpful Content system evaluates pages individually and at site level — a large volume of near-duplicate thin pages can suppress your entire domain.

#### Safe implementation:

* Keep programmatic pages to a separate URL silo (`/past-papers/`, `/revision/`)
* Each page must have unique body content beyond the template (minimum 300 words of non-boilerplate text)
* noindex low-value thin pages initially; index only when you can add unique value
* Submit programmatic sitemaps separately to GSC for easier monitoring

### Claude Code Implementation

Build a Python script with Claude Code that:

1. Reads a CSV of [exam-board, level, subject, year, paper-number] combinations
2. Calls Claude API to generate a unique 300-word "paper overview" section per row
3. Outputs HTML-ready content files with all schema markup pre-populated
4. Generates a sitemap.xml batch for submission

#### Example Claude Code prompt:

> "Write a Python script that reads papers.csv with columns [exam_board, level, subject, year, paper_number] and for each row, calls the Anthropic API to generate a 300-word unique summary of that exam paper's key topics and revision focus areas. Output each as a JSON file with fields: title, meta_description, body_html, faq_schema."

## 8. Social Signals, Community & Distribution

### Platform Priority for Exampilot's Audience

| Platform | Audience | Priority | Use Case |
|----------|----------|----------|----------|
| r/alevel, r/Edexcel, r/alevelmaths | International A-Level students | #1 | Authentic Q&A, 9709 and Edexcel IAL questions frequent |
| Facebook Groups ("Cambridge A Level Mathematics 9709") | International students (South/SE Asia) | #2 | Large communities, resource sharing |
| YouTube (9709 tutorial channels) | Students 16–18 | #3 | Comment sections, collaborations with tutors (50K–200K subs) |
| WhatsApp/Telegram (regional student groups) | Pakistan, Malaysia, UAE, Nigeria students | #4 | High ROI if you can enter these communities |
| Quora | International students | #5 | Evergreen Q&A content that ranks in Google |
| r/teachingresources, r/TeachingUK | Teachers | #6 | Resource sharing, educator links |
| LinkedIn | Parents, educators, EdTech investors | #7 | Thought leadership, PR amplification |

### Community Engagement Rules

The cardinal rule: provide value 9 times before mentioning your product once. Reddit and Discord communities ban self-promotion instantly. Build a reputation as "that person who always gives great revision advice" before mentioning Exampilot. After 4–6 weeks of genuine contribution, a natural mention of "I actually built a tool for this" is welcomed, not penalized.

Quora is underrated in 2026 for EdTech: Quora answers rank in Google for long-tail questions. Write detailed, cited answers to questions like "What's the best way to revise for GCSE Biology?" — include Exampilot in context, not as a pitch.

### Wife's Weekly Marketing Tasks (Independent Ownership)

#### Daily (15 min):

* Monitor Reddit (r/alevel, r/Edexcel, r/alevelmaths) for relevant questions; post genuine answers

#### 3× per week (30 min each):

* Respond to Quora questions in exam prep niche
* Post one TikTok/Reel: revision tip, study technique, student Q&A format
* Schedule one LinkedIn post sharing a blog article with a personal angle

#### Weekly (1–2 hours):

* Research and respond to 3–5 journalist queries on Featured.com
* Engage with 5–10 education influencer/blogger posts (comments, shares — not spam)
* Update the content calendar with new keyword ideas sourced from Reddit threads

#### Monthly (2–3 hours):

* Pitch one guest post to an education blog
* Track all brand mentions using Google Alerts (free) — respond to each
* Pull the GSC impressions report and identify new keyword opportunities

## 9. 90-Day Execution Roadmap

### Sprint 1 — Days 1–30: Foundation & First Content

#### One-time setup tasks:

* Technical SEO audit and fix (schema, CWV, robots.txt, sitemap)
* GSC + PostHog configured and verified
* All tool accounts created (Mangools, Screaming Frog, Featured.com, Ahrefs Webmaster Tools, PostHog)
* **Keyword taxonomy spreadsheet built for Cambridge 9709 (P1, P3) and Edexcel IAL (Pure 1, Pure 2)**
* **Topic cluster map built: Cambridge 9709 Pure 1 cluster first (your deepest content moat)**
* Author bio pages created with mathematical credentials (E-E-A-T: qualified maths teacher, Cambridge/Edexcel examiner, or subject specialist)
* About page, Privacy Policy, Terms of Service published (trust signals)

#### Recurring weekly:

* **3 articles published: 4 Cambridge 9709 Pure 1 topic spokes (differentiation, integration, functions, trigonometry)**
* **5 Reddit answers posted on r/alevel, r/Edexcel, r/alevelmaths**
* 3 Featured.com journalist queries responded to

#### Sprint 1 KPIs:

* 12+ pages indexed in GSC
* First impressions appearing (even for brand name queries)
* 0–3 referring domains (community mentions, directory listings)
* CWV: all pages "Good" in GSC

### Sprint 2 — Days 31–60: Topical Authority & First Rankings

#### One-time setup tasks:

* **Programmatic 9709 past papers section built (20–30 pages for 9709/12, 9709/13)**
* **Cambridge 9709 Pure 1 pillar page published (4,000+ words): "Cambridge 9709 Pure Mathematics 1: Complete Revision Guide"**
* **Edexcel IAL Pure 1 hub and first 4 topic spokes published**
* Internal link audit with Screaming Frog — fix all orphan pages
* First outreach batch: 10 resource page targets identified and emailed (focus on international A-Level communities)

#### Recurring weekly:

* 3 articles published
* 1 guest post pitch sent
* Reddit/Quora engagement maintained
* Rank tracking reviewed in Mangools (look for pages entering top 50)

#### Sprint 2 KPIs:

* 40+ pages indexed
* First keyword in top 20 (likely a branded or very long-tail term)
* 5–10 referring domains
* First organic sessions from non-brand keywords in PostHog

### Sprint 3 — Days 61–90: Scale & Compound

#### One-time setup tasks:

* **Programmatic 9709 + Edexcel IAL section (60–90 pages total) reviewed, thin pages removed or improved, indexed batch submitted**
* **First original data asset created: "2026 International A-Level Student Survey: How Students Prepare for Cambridge 9709 and Edexcel IAL"**
* **Comparison pages published: /vs/save-my-exams/, /vs/papacambridge/, /vs/physics-maths-tutor/**
* Internal link map fully updated in Notion

#### Recurring weekly:

* 3 articles published
* Digital PR outreach (data asset distribution)
* Social distribution cadence maintained

#### Sprint 3 KPIs:

* 80–120 total pages indexed
* 3–8 keywords ranking in top 10
* 15–30 referring domains
* 200–1,000 organic sessions/month (realistic for new domain at day 90)
* DR 15–25 in Ahrefs Webmaster Tools

### 20% of Actions Driving 80% of Results

These are your non-negotiables — the highest-leverage moves in the entire plan:

1. **Technical foundation complete** (CWV, schema, GSC, sitemap) — everything else depends on this
2. **Cambridge 9709 Pure 1 cluster map complete** — 1 pillar + 8 spokes covering all P1 topics
3. **"Cambridge 9709 Pure Mathematics 1: Complete Revision Guide" pillar page published** (4,000+ words, all 8 P1 topics, FAQPage schema, internal links)
4. **FAQPage schema implemented on every page from day one** — single highest ROI schema for AI Overviews
5. **Featured.com and Qwoted accounts active**, with wife answering 3 journalist queries per week

The organic search results you'll see at day 90 — first rankings, first non-brand sessions, first referring domains — are the direct output of the decisions you make in days 1–14. The architecture choices you make now are extremely difficult to change later without losing whatever authority you've built. Prioritize structure over volume every time.

## 10. What NOT to Do

### Tactics That Are Hype or Actively Dangerous

**1. Bulk AI content production ("publish 50 articles in week one")**

This is the single most dangerous myth in 2026 SEO. Google's Scaled Content Abuse policy targets intent — using automation to produce content primarily to manipulate rankings. Even if each article is technically non-duplicate, a pattern of rapid low-quality AI publishing triggers Helpful Content demotion at the domain level. Recovery from a Helpful Content demotion takes 3–6 months minimum. Publish 3 high-quality articles per week and protect your domain's quality signal fiercely.

**2. Buying backlinks from "white hat" link marketplaces**

Sites like Loganix, Links Management, or Fiverr "niche edit" sellers present these as editorial. In 2026, Google's SpamBrain algorithm identifies paid link patterns via velocity, anchor text distribution, and linking site patterns. The risk is a manual action (discovered via GSC), not just algorithmic demotion — a manual action means zero organic traffic until manually reviewed by Google.

**3. Exact-match anchor text over-optimization**

If 40% of your backlinks say "GCSE revision app" pointing to your homepage, that is a clear spam signal. Keep branded anchors (your brand name) as the majority (~60%), generic anchors (~20%), and keyword-rich anchors (~20%).

**4. Targeting BBC Bitesize or Khan Academy head terms**

Head terms like "GCSE Maths revision" are dominated by DR 80+ authority sites. A new domain competing here in 90 days is wasted effort. Target the long tail they can't cover at scale.

**5. Hiding AI authorship**

Do not claim all content is "written by human experts" if it isn't. This is a trust signal that can backfire with sophisticated users (and Google Quality Raters who evaluate E-E-A-T). The honest position — "AI-assisted, human-reviewed content" — is fully defensible and increasingly respected.

**6. Social signal gaming (buying followers, fake engagement)**

Social signals are a negligible direct ranking factor. Fake engagement wastes budget and can get your social accounts banned. Focus social effort on genuine community building — the referral traffic and brand mentions have SEO value; the follower count does not.

**7. Thin "what is X" definition pages**

Publishing hundreds of pages like "What is the Krebs Cycle?" with 200 words each is exactly the programmatic thin content pattern that triggered the HCU devaluations of 2023–2025. Every page needs unique value above the definition: practice questions, exam-specific tips, a study technique for remembering the content.

---

## Final Priority Matrix

If you had to choose just five actions to execute in the first 30 days with limited bandwidth, they are, in order:

1. **Technical foundation complete** (CWV, schema, GSC, sitemap) — everything else depends on this
2. **Cambridge 9709 Pure 1 cluster map complete** — 1 pillar + 8 spokes covering all P1 topics
3. **"Cambridge 9709 Pure Mathematics 1: Complete Revision Guide" pillar page published** (4,000+ words, all 8 P1 topics, FAQPage schema, internal links)
4. **FAQPage schema implemented on every page from day one** — single highest ROI schema for AI Overviews
5. **Featured.com and Qwoted accounts active**, with wife answering 3 journalist queries per week

The organic search results you'll see at day 90 — first rankings, first non-brand sessions, first referring domains — are the direct output of the decisions you make in days 1–14. The architecture choices you make now are extremely difficult to change later without losing whatever authority you've built. Prioritize structure over volume every time.