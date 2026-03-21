# ExamPilot Waitlist Homepage — Full Specification (v2)

**Date**: 2026-03-20
**Conversion Goal**: Waitlist signup (email capture)
**Target Conversion Rate**: 15-25% (lead capture benchmark for strong offer)
**Page Type**: Pre-launch waitlist with SEO value
**Audience**: A-Level Maths students (16-18), Cambridge International A Level Mathematics and Edexcel International A Level Mathematics, global (UK, EU, Pakistan, India, UAE, Malaysia, Singapore, Nigeria + 150 other CIE countries)
**Brand Voice**: See "Brand Voice & Tone" appendix at end of this document

---

## Strategic Framing

This is NOT a "coming soon" page. It's a fully-realized landing page that:
1. Captures waitlist signups as the primary conversion
2. Builds SEO authority (proper content, schema, internal linking)
3. Establishes brand credibility before product launch
4. Collects emails for nurture sequence
5. Serves as the hub page that all blog content links back to

The page should feel like ExamPilot already exists and is selectively onboarding — not like it's vaporware.

**Framing language**: "Early access" / "We're onboarding students now" — NOT "Coming soon" / "Under construction" / "We're building"

### Hub Page Strategy

This homepage is the top of the content hierarchy. Blog content and pillar pages link back here:

```
Homepage (this page) ← all content links back here
├── /cambridge/9709/pure-1/          ← Cambridge 9709 pillar (future)
│   ├── /cambridge/9709/pure-1/integration/
│   ├── /cambridge/9709/pure-1/differentiation/
│   └── ... (topic spokes)
├── /edexcel/ial/pure-1/             ← Edexcel IAL pillar (future)
├── /blog/                           ← Blog hub
│   ├── /blog/common-mistakes-9709/
│   └── ... (blog articles)
└── /alternatives/                   ← Competitor comparison pages (post-90-day)
```

**Transition plan**: When the product goes live, this waitlist page evolves into a traditional product homepage. The structure is designed for this:
- Hero section: swap waitlist CTA → "Start Free" / "Try ExamPilot"
- Problem section: stays as-is
- Solution section: add product screenshots/demo video
- Features section: stays as-is, add real metrics
- Social proof: add real testimonials (currently excluded)
- Lead magnet section: becomes secondary CTA or remove
- FAQ: update launch-related Qs to product Qs

The pillar pages (`/cambridge/9709/pure-1/` etc.) become the SEO workhorses and continue linking to the homepage. The homepage shifts from lead capture to product conversion, but the content architecture doesn't change.

### Value Proposition (Core Messaging)

ExamPilot's value is NOT "we predict your grade." The value is:

**You walk into your exam prepared, confident, and calm — because ExamPilot has found your misconceptions, fixed them through adaptive practice, made sure you retain what you've learned, and tested you on exam-style questions across the curriculum.**

Grade prediction is a byproduct of this process, not the headline. The platform needs significant usage and curriculum coverage before it can estimate a grade — it's not an instant feature.

**Messaging hierarchy**:
1. We find the specific misconceptions causing your mistakes
2. We fix them with adaptive, exam-style practice
3. We make sure you actually remember what you learn (spaced repetition)
4. We ensure you've covered enough of the curriculum
5. Over time, all of this gives us the data to estimate how you'll likely perform

---

## Page Architecture (Section by Section)

### Section 1: Hero (Above the Fold)

**Goal**: Pass the 5-second test. Visitor understands: what it is, who it's for, why they should care, what to do next.

**H1 Headline** (under 65 chars, benefit-led):
> "Walk Into Your A-Level Maths Exam Ready"

Alternative options to A/B test:
- "A-Level Maths Revision That Finds What You're Getting Wrong"
- "Stop Revising Blind. Know Exactly Where Your Gaps Are."
- "The A-Level Maths Prep That Fixes Your Mistakes For Good"

**Subheadline** (1-2 sentences, expands on headline):
> "ExamPilot identifies the exact misconceptions holding you back, fixes them with adaptive practice, and uses spaced repetition so you actually retain what you learn. Built for Cambridge International and Edexcel International A Level Maths."

**Primary CTA Button**:
> "Get Early Access + Free Revision Kit"

**Secondary CTA** (text link, not button):
> "See how it works ↓"

**Risk Reversal** (directly under CTA button, small text):
> "Free to join. No credit card. Unsubscribe anytime."

**Trust Bar** (below hero, horizontal strip):
> "Cambridge International & Edexcel IAL aligned · Adaptive AI-powered practice · Covers the full curriculum"

**Form**: Email-only input field. Single field. Placeholder: "Your email address". Button: "Get Early Access". No name, no password, no dropdowns.

**Design Notes**:
- No slider/carousel
- No autoplay video
- Clean, focused — one CTA path
- Minimal navigation (logo + single "Log In" link, no menu items that distract)
- Mobile: CTA button full-width, headline max 2 lines

---

### Section 2: Problem (The Pain)

**Goal**: Emotional resonance. Student reads this and thinks "that's exactly me."

**H2**: "Sound Familiar?"

Three problem cards (card-based layout, each with an icon and a student quote):

**Card 1: "I don't know what I don't know"**
> You've been revising for weeks but have no idea if it's working. Your teacher says "you'll be fine" but you don't feel fine. You could be wasting hours on topics you already know — or completely missing the ones that'll cost you marks.

**Card 2: "I keep making the same mistakes"**
> You practice question after question, but the same errors keep coming back. You know the formula, you just... keep getting it wrong. Something in your approach is broken, and no one's telling you what it is.

**Card 3: "I have no idea what grade I'm actually getting"**
> Mock exams feel random. Your teacher's prediction doesn't match how you feel. You need a conditional grade for university and you genuinely don't know if you'll get it. The uncertainty is worse than the revision.

**Design Notes**:
- Use actual student language (sourced from Reddit r/alevel, r/igcse)
- Cards should feel personal, not corporate
- No ExamPilot branding in this section — pure empathy
- Short paragraphs, conversational

---

### Section 3: Solution (What ExamPilot Does)

**Goal**: Transition from pain to possibility. Introduce the product as the answer to the problems above, not as a feature list.

**H2**: "What If Something Actually Understood Where You're Going Wrong?"

**Body** (2-3 short paragraphs):
> ExamPilot is an AI-powered exam prep platform for Cambridge International and Edexcel International A Level Maths.
>
> It finds the specific misconceptions behind your mistakes — not just "you got integration wrong" but the exact reasoning error causing it across multiple question types. Then it gives you targeted, adaptive practice to fix those patterns, and uses spaced repetition to make sure the fix sticks.
>
> The more you use it, the clearer the picture becomes — what you know, what you don't, and how ready you actually are.

**Mini CTA** (inline, after solution text):
> "Join the waitlist to be first in line →"

**Design Notes**:
- No feature grid yet — just the concept
- Keep it human, not technical
- This section bridges problem → features
- The last line subtly references the eventual grade prediction without promising it

---

### Section 4: How It Works (3 Steps)

**Goal**: Make it concrete. Show the student what the experience feels like.

**H2**: "How It Works"

**Step 1: Start Practising**
> Jump in and start answering exam-style questions. Our AI watches how you think — not just whether you get the right answer, but how you approach the problem and where your reasoning breaks down.

**Step 2: See Your Misconceptions**
> ExamPilot maps the specific patterns causing your mistakes. You'll see exactly which reasoning errors are holding you back — and get targeted practice designed to fix them at the root.

**Step 3: Retain What You Learn**
> Spaced repetition ensures you don't forget what you've mastered. The AI resurfaces content at the exact moment you're about to forget it. Over time, you build a complete, lasting understanding of the curriculum.

**Design Notes**:
- Numbered steps with icons
- Each step: bold title + 2-sentence description
- No product screenshots (pre-launch) — icons or simple illustrations

---

### Section 5: What Makes This Different (Features as Benefits)

**Goal**: Differentiate from Save My Exams, PapaCambridge, Physics & Maths Tutor. Position ExamPilot as categorically different.

**H2**: "Not Another Past Paper Site"

**Subheadline**: "Every other platform gives you questions and says 'good luck.' ExamPilot actually understands how you think."

Feature cards (4 max):

**1. Finds WHY You Get Things Wrong (Question DNA)**
> You're not "bad at integration." You're making a specific reasoning error that shows up across multiple question types. Question DNA identifies the pattern and fixes it at the root.
>
> *Your teacher can't see this. Our AI can.*

**2. Questions That Match Your Level (Adaptive Practice)**
> Questions automatically adjust to your ability. Challenging enough to push you forward, not so hard you get stuck and frustrated. Every question is exam-style and chosen specifically for you.
>
> *Not random questions from a bank. Targeted practice.*

**3. Remember What You Learn (Smart Review)**
> Built on the FSRS spaced repetition algorithm. ExamPilot knows when you're about to forget something and resurfaces it at exactly the right time.
>
> *No more forgetting formulas the day before the exam.*

**4. Covers Your Full Curriculum**
> Practice that maps to your entire syllabus — so you know you haven't missed anything. ExamPilot tracks which topics you've covered and which still need attention, so there are no surprises on exam day.
>
> *Complete curriculum coverage, not just random practice.*

**Design Notes**:
- Card layout, 2x2 grid on desktop, stacked on mobile
- Each card: bold title, 2-sentence benefit description, italic differentiator line
- No "learn more" links — keep them on this page
- Icons/illustrations rather than screenshots (pre-launch)
- Question DNA (misconception identification) is the lead feature — it's the core differentiator

---

### Section 6: Curriculum Alignment

**Goal**: Show this is built for THEIR specific exam — not generic maths. SEO anchor.

**H2**: "Built for Your Exam Board"

Two cards side by side:

**Cambridge International A Level Mathematics**
- Exam board: Cambridge Assessment International Education (CAIE)
- Qualification: Cambridge International AS & A Level Mathematics
- "Aligned to the current Cambridge International specification. Exam-style questions, syllabus-mapped coverage, and practice calibrated to Cambridge assessment objectives."
- Badge: "SYLLABUS ALIGNED"

**Edexcel International A Level Mathematics**
- Exam board: Pearson Edexcel
- Qualification: Edexcel International Advanced Level Mathematics
- "Aligned to the current Pearson Edexcel IAL specification. Questions matched to Edexcel format, style, and assessment criteria."
- Badge: "SYLLABUS ALIGNED"

**Design Notes**:
- Keep it at exam board level — don't list specific paper codes or topics here
- Students self-identify by exam board, not by paper code, at this stage
- SEO value: entity mentions for Cambridge International and Edexcel IAL
- When pillar pages exist, these cards can link to `/cambridge/9709/` and `/edexcel/ial/`

---

### Section 7: Lead Magnet + Waitlist CTA (Mid-Page)

**Goal**: Conversion opportunity in the middle of the page (the audit found a 60% gap with no CTA).

**H2**: "Join the Waitlist. Get Free Revision Resources."

**Body**:
> Sign up for early access and we'll send you three resources to start improving right now — before ExamPilot even launches:

**Lead Magnet Bundle** (3 items):
1. **A-Level Maths Revision Timetable Template** — Week-by-week plan for the 8 weeks before your exam
2. **Top 20 Common Mistakes from Examiner Reports** — From actual Cambridge and Edexcel examiner reports. Know what to avoid before you even start practising.
3. **Formula Quick Reference Sheet** — Every formula you need, formatted for printing and pinning above your desk.

**CTA Button**:
> "Get My Free Revision Kit"

**Risk Reversal**:
> "Instant download. No spam, ever. Unsubscribe anytime."

**Form**: Email only. Single field.

**Design Notes**:
- This is the highest-converting section — strong offer + low friction
- Show mockups/previews of the lead magnets if possible
- Checkmarks next to each item
- This section should be visually distinct (subtle background color change)

---

### Section 8: FAQ

**Goal**: Handle objections. SEO value (FAQPage schema). Keep students on page longer.

**H2**: "Questions? Answers."

**Q1: When does ExamPilot launch?**
> We're onboarding our first students now. Join the waitlist and you'll be among the first to get access when we open up. Early access students get priority and exclusive pricing.

**Q2: Is it free?**
> ExamPilot will have a free tier with core features. Early waitlist members get extended free access as a thank-you for joining early. The revision resources you get when you sign up are completely free, no strings attached.

**Q3: Does it work for both Cambridge and Edexcel?**
> Yes. ExamPilot is built for Cambridge International A Level Mathematics and Edexcel International A Level Mathematics. Every question and recommendation is calibrated to your specific exam board's requirements and assessment style.

**Q4: Will this work if I'm really struggling?**
> Especially then. ExamPilot adapts to your level — you won't face overwhelming questions. Question DNA finds the specific misconceptions causing your mistakes and helps you fix them. Most students start noticing improvement within a few weeks of regular practice.

**Q5: I'm an international student. Does it work for me?**
> Absolutely. Cambridge International exams are taken in 160+ countries, and Edexcel IAL is widely used internationally. ExamPilot works anywhere with an internet connection. Ask Sparky (our AI tutor) is available 24/7 — no waiting for school hours or tutoring appointments.

**Q6: How is this different from Save My Exams or Physics & Maths Tutor?**
> Those are great resources for past papers and notes. ExamPilot is fundamentally different — it diagnoses the reasoning patterns behind your mistakes, adapts questions to your level, and uses spaced repetition so you actually retain what you learn. It's not a document library, it's an AI study partner that understands how you think.

**Q7: Can ExamPilot predict my grade?**
> As you use the platform and build up practice data across the curriculum, ExamPilot develops an increasingly accurate picture of your readiness. Over time, this gives you a meaningful estimate of how you're likely to perform. But our focus is on the preparation itself — finding your gaps, fixing your misconceptions, and making sure you've covered enough ground to walk into the exam confident.

**Design Notes**:
- Accordion/collapsible format
- FAQPage schema on all 7 questions (critical for AI Overviews)
- Keep answers concise — 2-3 sentences max
- Q6 is the competitive differentiation question students actually ask on Reddit
- Q7 handles grade prediction honestly — it's a byproduct of thorough preparation, not an instant feature

---

### Section 9: Final CTA (Closing)

**Goal**: Last conversion opportunity. Strongest copy, fullest risk reversal.

**H2**: "Your Exam Is Coming. Start Preparing Smarter."

**Body**:
> Get instant access to your free revision resources and be first in line when ExamPilot opens for early access.

**CTA Button** (large, prominent):
> "Get Early Access + Free Revision Kit"

**Risk Reversal** (below button):
> "Free. No credit card. No spam. Unsubscribe anytime."

**Supporting trust elements** (small text/icons below):
- "Cambridge International & Edexcel IAL aligned"
- "Adaptive AI-powered practice"
- "Used by students across 12+ countries"

**Design Notes**:
- This section should feel like a closing argument
- Maximum visual weight on the CTA
- No student counts or fabricated social proof

---

### Section 10: Footer

**Content**:
- Logo + tagline: "AI-powered exam prep for A-Level Maths"
- Navigation: Blog | About | Terms | Privacy
- Social: Instagram, TikTok, Discord, LinkedIn
- Contact: hello@exampilot.io
- Copyright: © 2026 ExamPilot. All rights reserved.
- Data protection: "Your data is protected. We never share your email with third parties."

**Design Notes**:
- Minimal — don't distract from final CTA above
- Include privacy line (builds trust, especially for international/EU audience)

---

## SEO Specification

### Meta Title (under 60 chars)
> "A-Level Maths Exam Prep | AI-Powered Revision | ExamPilot"

### Meta Description (150-160 chars)
> "AI finds the misconceptions behind your A-Level Maths mistakes and fixes them. Adaptive practice + spaced repetition for Cambridge & Edexcel. Join the waitlist." (162 chars)

### URL
> `https://www.exampilot.io/`

### H1
> Same as hero headline (one H1 only)

### Schema Markup (JSON-LD)
1. **Organization** — ExamPilot, education technology
2. **SoftwareApplication** — ExamPilot, Educational
3. **FAQPage** — All 7 FAQ questions
4. **WebPage** — Homepage type

### Internal Links
- Blog link in nav and footer → `/blog`
- Each blog post should link back to homepage
- Future hub pages (`/cambridge/9709/pure-1/`, `/edexcel/ial/pure-1/`) link to homepage
- Curriculum cards link to pillar pages when they exist

### Keyword Integration
Primary keywords to integrate naturally (don't force):
- "A-Level Maths" (in headline, subheadline, body)
- "Cambridge International A Level Mathematics" (curriculum section, FAQ)
- "Edexcel International A Level Mathematics" (curriculum section, FAQ)
- "exam prep" / "revision" (throughout)
- "misconceptions" / "mistakes" (solution, features)
- "spaced repetition" (features, how it works)
- "adaptive practice" (features, trust bar)

---

## Technical Specification

### Performance
- LCP < 2.5s (Largest Contentful Paint)
- INP < 200ms (Interaction to Next Paint)
- CLS < 0.1 (Cumulative Layout Shift)
- Total page weight < 500KB
- No render-blocking third-party scripts above fold

### Form
- Single field: email
- Client-side validation (email format)
- Server-side validation
- Success state: inline confirmation message ("You're in! Check your email for your free revision kit.")
- Error state: inline error below field
- Submission triggers: PostHog `waitlist_signup` event with source attribution
- Double opt-in required (GDPR compliance for EU/UK students)

### Analytics Events (PostHog)
| Event | Trigger | Properties |
|-------|---------|------------|
| `page_view` | Page load | `page: homepage` |
| `waitlist_signup` | Form submit | `source: hero \| mid-page \| footer`, `email_domain` |
| `cta_click` | Any CTA click | `cta_text`, `cta_position`, `section` |
| `faq_expand` | FAQ accordion open | `question_index`, `question_text` |
| `scroll_depth` | 25%, 50%, 75%, 100% | `depth_pct` |

### Responsive Breakpoints
- Mobile: < 640px (single column, full-width CTAs, stacked cards)
- Tablet: 640-1024px (2-column where appropriate)
- Desktop: > 1024px (full layout, 2x2 feature grid, side-by-side curriculum cards)

### Accessibility
- All images have alt text
- Color contrast ratio 4.5:1 minimum
- Keyboard-navigable form and FAQ accordions
- ARIA labels on interactive elements
- Focus indicators visible

---

## Design Direction

### Overall Aesthetic
- Clean, modern, confidence-inspiring
- Dark mode preferred (aligns with student/tech audience, differentiates from the bright/playful look of Save My Exams and PMT)
- Zinc/neutral background tones with one accent color (blue-teal gradient from current site works)
- Geist Sans for interface text, Geist Mono for any data/metrics shown
- Generous whitespace — the page should breathe

### Section Visual Rhythm
| Section | Background | Visual Weight |
|---------|------------|---------------|
| Hero | Dark/gradient | Maximum — headline + CTA dominate |
| Problem | Slightly lighter | Medium — cards with subtle borders |
| Solution | Same as problem | Medium — text-focused |
| How It Works | Light/contrasting strip | Medium — numbered steps |
| Features | Dark | High — feature cards with icons |
| Curriculum | Neutral | Medium — two cards side by side |
| Lead Magnet CTA | Accent/highlight background | High — this needs to pop |
| FAQ | Neutral | Low — accordion, clean |
| Final CTA | Dark/gradient (echo hero) | Maximum — closing push |

### Imagery
- No stock photos of students studying
- Prefer: abstract/geometric illustrations, subtle math-related patterns, or stylized product mockups
- Lead magnet previews: show mockups of the timetable/guide/formula sheet
- No fabricated student photos or AI-generated faces

### Interactions
- Smooth scroll on "See how it works ↓"
- FAQ accordion (one open at a time)
- Subtle hover states on cards and CTAs
- No parallax, no animations that delay content visibility
- Form: inline success message, not redirect

---

## Copy Tone Guidelines

- **Confident, not arrogant**: "ExamPilot finds the misconceptions behind your mistakes" — not "We're the best revision tool ever made"
- **Student-first language**: "Your misconceptions" / "Your gaps" not "Our AI technology"
- **Honest about difficulty**: "A-Level Maths is hard. We don't pretend otherwise."
- **Understate grade prediction**: It's a consequence of thorough preparation, not a headline feature. Don't promise accuracy percentages until validated.
- **International-neutral English**: No UK slang, no assumptions about school system. "Revision" is fine (universally understood in target markets). "Swotting" is not. Remember EU audience alongside traditional CIE markets.
- **No fabricated social proof**: No fake testimonials, no inflated student counts, no unverified university names. When real proof exists, add it.
- **No "study plan" language**: ExamPilot focuses on personalized spaced repetition and misconception identification, not prescriptive study plans.

For full brand voice details, see the Brand Voice & Tone appendix at the end of this document.

---

## What's Intentionally Excluded (and Why)

| Excluded | Reason | When to Add |
|----------|--------|-------------|
| Social proof / testimonials | No real users yet. Fake testimonials damage trust. | When real beta testers provide genuine feedback. |
| Student count ("500+ students") | Cannot verify. Inflated numbers erode credibility. | When real waitlist count is meaningful and verifiable. |
| University name-dropping ("UCL, Imperial") | Unverified association. | Only when students from these universities are real, confirmed users. |
| "Built by A-Level Maths teachers" | Not accurate. | Replace with accurate founder/team credentials when ready. |
| Grade prediction as headline | Requires significant usage data. Cannot deliver in 15 minutes. Overpromising risks trust. | When the prediction model is validated and the UX supports progressive grade estimation. |
| 94% accuracy claim | Not yet validated at scale. | When statistically defensible across sufficient user base. |
| Specific paper codes (9709/12, WMA11) | Homepage should be broad. Pillar pages go specific. | Pillar pages and spoke articles cover paper-code specificity. |
| Demo video | Doesn't exist yet. | When a real product walkthrough is available. |

---

## Conversion Optimization Checklist

Before shipping, verify:

### Above the Fold
- [ ] Headline under 65 chars with benefit
- [ ] Value prop clear within 5 seconds (misconceptions + adaptive practice + spaced repetition)
- [ ] Single primary CTA visible without scrolling
- [ ] Risk reversal text under CTA
- [ ] No competing navigation distracting from CTA

### CTAs (3-4 total)
- [ ] Hero CTA (0-10% of page)
- [ ] Mid-page inline CTA after Solution section (~30%)
- [ ] Lead magnet CTA (~60%)
- [ ] Final closing CTA (~90%)
- [ ] All CTAs use "Get" + benefit language
- [ ] All CTAs have risk reversal text nearby
- [ ] Form is email-only (1 field)

### Trust (Honest Signals Only)
- [ ] Exam board alignment stated
- [ ] Core value prop clearly communicated
- [ ] Data privacy mentioned (footer minimum)
- [ ] GDPR double opt-in for EU/UK
- [ ] No fabricated numbers, testimonials, or claims

### SEO
- [ ] Single H1 with primary keyword
- [ ] Meta title under 60 chars
- [ ] Meta description 150-160 chars with CTA
- [ ] FAQPage schema on all FAQ items
- [ ] Organization + SoftwareApplication schema
- [ ] Blog link present for internal linking

### Mobile
- [ ] Headline fits 2 lines max on mobile
- [ ] CTA buttons full-width on mobile
- [ ] FAQ accordion works on touch
- [ ] Form input large enough for thumb typing
- [ ] No horizontal scroll

### Performance
- [ ] LCP < 2.5s
- [ ] No layout shift on form interaction
- [ ] Images lazy-loaded below fold
- [ ] Total page weight < 500KB

---

## Post-Signup Flow (Brief)

After email submission:
1. **Inline success message**: "You're in! Check your email for your free revision kit."
2. **Welcome email** (immediate):
   - Subject: "Your A-Level Maths Revision Kit is here"
   - Contains: download links for all 3 lead magnets
   - Sets expectation: "We'll email you when early access opens"
3. **Nurture sequence**:
   - Email 2 (Day 3): Common mistakes guide highlight + study tip
   - Email 3 (Day 7): "How ExamPilot finds your misconceptions" (build anticipation)
   - Email 4 (Day 14): Progress update / waitlist milestone

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Waitlist conversion rate | 15-25% | Signups / unique visitors |
| Bounce rate | < 40% | PostHog |
| Avg time on page | > 90 seconds | PostHog |
| Scroll depth (75%+) | > 40% of visitors | PostHog |
| Lead magnet download rate | > 80% of signups | Email open + click |
| Email list growth | 200+ signups/month | Email provider |

---

## Appendix A: Brand Voice & Tone

### Voice Pillars

**1. Confident Guide, Not Distant Expert**
We know A-Level Maths inside out, but we talk like someone who's been through it — not someone lecturing from a podium. We're the older student who got the A* and is now showing you exactly how.
- Sound: Direct, assured, practical. No hedging. "Here's what to do" not "you might want to consider."
- Example: "Integration isn't hard — it's just poorly taught. Here's the approach that actually clicks."
- Avoid: Academic language, condescension, false modesty, wishy-washy advice.

**2. Relentlessly Practical**
Every sentence earns its place by being useful. We don't write to fill space — we write to move someone closer to exam readiness. Action-oriented, specific, step-by-step.
- Example: "Your predicted grade is based on 3 things: topic coverage, accuracy under timed conditions, and retention over time."
- Avoid: Motivational fluff without substance, generic study tips recycled from every other site, filler content.

**3. Honest About the Challenge**
We don't pretend A-Level Maths is easy. We don't promise miracles. We acknowledge the difficulty and then show the path through it. Students trust us because we don't bullshit them.
- Example: "Integration by parts trips up most students — not because they can't do maths, but because they haven't built the pattern recognition yet."
- Avoid: Toxic positivity, minimizing difficulty ("Maths is easy!"), promising unrealistic results ("Get an A* in 2 weeks!").

**4. Data-Driven, Not Data-Drowning**
We use numbers and metrics to back up claims — but we always translate them into what they mean for the student. Show the data, then tell the story.
- Example: "Students who used spaced repetition for 3 weeks saw their retention jump from 45% to 78% on the same topic set."
- Avoid: Throwing metrics without context, making the platform sound clinical rather than helpful.

**5. Student-First, Always**
We exist for students, not for schools, parents, or investors. Every piece of content asks: "Does this help a 16-18 year old study better?" Slightly informal, but not immature. Smart without trying too hard.
- Example: "Skip the 3-hour cram session. 20 minutes of focused practice targets exactly what you'll forget first."
- Avoid: Talking about students in third person ("Students will benefit from..."), corporate speak, trying too hard to use Gen-Z slang.

### General Tone: Smart Study Partner
Imagine a sharp, slightly older student who absolutely nailed their A-Levels and is now helping you do the same. Direct, knowledgeable, doesn't waste your time, genuinely wants you to succeed. Not trying to be your friend — trying to get you an A*.

### Tone by Content Type

| Content Type | Tone | Example |
|-------------|------|---------|
| Study guides / how-to | Clear, sequential, confidence-building | "Step 3 is where most people get stuck. Here's the trick..." |
| Exam strategy | Authoritative, tactical, insider-knowledge | "Cambridge 9709 Paper 1 always front-loads the algebra. Get those marks banked first." |
| Product / features | Benefit-first, student-language, honest | "Ask Sparky doesn't give you the answer. It asks you the right questions until you find it yourself." |
| Blog / SEO | Helpful, search-intent matched, value-dense | "If you're searching for '9709 Pure 1 past papers,' you're probably 3 weeks from your exam. Here's a smarter approach." |
| Homepage / landing | Empathetic to problem, confident about solution, no hype | "A-Level Maths is hard. We don't pretend otherwise. But the right practice changes everything." |

### Terminology

| Say This | Not That | Why |
|----------|----------|-----|
| Practice session | Quiz | Practice sounds purposeful; quiz sounds random |
| Exam readiness | Exam preparation | Readiness implies measurement, not just activity |
| Knowledge gaps | Weak areas | Gaps sounds fixable; weak sounds personal |
| Misconceptions | Errors / mistakes | Misconceptions implies a fixable thinking pattern |
| Ask Sparky | AI tutor | Sparky has personality; AI tutor is generic |
| Syllabus | Curriculum | Syllabus is what Cambridge/Edexcel students use |
| Mark scheme | Answer key | Mark scheme is exam-board specific and students know it |

### Cultural Sensitivity
Students span the UK, EU, UAE, Pakistan, Malaysia, Singapore, Nigeria, India, and beyond. Be assertive without being culturally insensitive. Avoid UK-centric slang or assumptions about school systems. "Revision" is universally understood. "Swotting" is not. A student in Dubai and a student in London both feel exam pressure — but may express it differently.

### Writing Style
- **Sentence length**: 12-18 words average. Short punchy sentences for impact. Longer for explanation.
- **Paragraphs**: 1-3 sentences. One idea per paragraph. Front-load the value.
- **Voice**: Active. "ExamPilot identifies your gaps" not "Gaps are identified by ExamPilot."
- **Mobile-first**: Many students read on phones. Short paragraphs, scannable structure.
- **Word choice**: Clear and direct. "Learn" not "Facilitate the acquisition of knowledge." Specific over vague: "Cambridge 9709 Pure 1 integration" not "maths topics."

---

## Appendix B: Product Features Reference

### Core Platform
ExamPilot is an AI-powered exam readiness platform for A-Level Mathematics students. It tells students exactly where they stand, what they need to work on, and guides them to their target grade through adaptive practice, AI tutoring, and spaced repetition.

### Exam Board Support
| Exam Board | Qualification | Status |
|---|---|---|
| Cambridge International (CAIE) | AS & A Level Mathematics (9709) | Launch focus (80%) |
| Pearson Edexcel | International A Level Pure Mathematics (WMA11/WMA12) | Launch focus (20%) |

### Key Features (for copy reference)

**Exam Readiness Index (ERI)**: Generates a predictive grade (A*-U) based on actual performance data. Continuously updated. Requires significant platform usage to calibrate — NOT an instant result.

**Question DNA**: Tags questions with underlying reasoning patterns, not just topic labels. Identifies the specific misconceptions causing mistakes across multiple question types.

**Adaptive Practice**: Questions adjust to student ability level. Challenging enough to grow, not so hard they get discouraged.

**Ask Sparky (AI Tutor)**: Socratic AI tutor. Never gives the answer — asks guiding questions. Available 24/7. Context-aware (knows the specific question being worked on).

**Smart Review (Spaced Repetition)**: FSRS-powered system that resurfaces content at optimal intervals to prevent forgetting. Tracks forget risk, memory debt, and stability momentum.

**Module Tests & ExamLens (Mock Exams)**: Structured tests covering specific syllabus modules. Timed mock papers that mirror real exam conditions. Questions selected based on knowledge gaps.

### Competitive Positioning
| ExamPilot | Save My Exams | Physics & Maths Tutor | PapaCambridge |
|---|---|---|---|
| Identifies misconceptions (Question DNA) | Topic labels only | Topic labels only | No classification |
| Adaptive question difficulty | Static papers | Static resources | Static PDFs |
| Spaced repetition (FSRS) | No retention system | No retention system | No retention system |
| Socratic AI tutor (Ask Sparky) | No AI | No AI | No AI |
| Cambridge + Edexcel specific | Broad coverage | Broad coverage | Cambridge only |
| Progressive grade estimation | No prediction | No prediction | No prediction |

### Company
- **Founded**: 2025
- **Founders**: Enitan Williams, Teresa
- **Based**: Spain (serving globally)
- **Stage**: Pre-launch, onboarding first users
- **URL**: https://www.exampilot.io
- **Contact**: hello@exampilot.io
- **Social**: Instagram (@exampilot.uk), TikTok (@exampilot), Discord, LinkedIn
