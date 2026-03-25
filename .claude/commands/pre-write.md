# Pre-Write Command

Analyze a research brief, determine content type, map content to Sanity components, and scaffold a JSON data file before writing. This command runs **before** `/write`.

## Usage
`/pre-write [research brief filename or topic]`

## What This Command Does
1. Reads the research brief from `research/`
2. Determines the content type from the canonical taxonomy
3. Maps every visual/structural element to existing Sanity block types
4. Flags any elements that may need a new component (with reuse justification)
5. Generates `.excalidraw` JSON files for any diagrams needed
6. Outputs a component mapping table for review
7. Scaffolds a JSON data file for the refactored content pipeline

## Process

### Step 1: Load the Research Brief
- Find the matching brief in `research/` (by filename or topic match)
- If no brief found, ask the user which brief to use

### Step 2: Determine Content Type

Reference the canonical Content Type Taxonomy (from `spyglass/docs/CONTENT_GENERATION_REFACTORING_GUIDE.md`). Every page created via SEO Machine falls into one of these types:

| Content Type | Sanity Type | URL Pattern | When to Use |
|---|---|---|---|
| **Topic Page** | `topicPage` | `/{examBoard}/{code}/{paper}/{topic}` | Educational revision content (differentiation, integration, vectors) |
| **Blog Post** | `post` | `/blog/category/{category}/{slug}` | Articles, guides, study tips |
| **Alternative Page** | `alternativePage` | `/alternatives/{competitor}/` or `/vs/{competitor}/` | Competitor comparisons (Save My Exams, PMT) |
| **Best-of List** | `bestOfPage` | `/best/{category}/` or `/tools/{tool-name}/` | Resource roundups, free tool pages |
| **Hub Page** | `hubPage` | `/{examBoard}/{code}/` | Pillar pages (Cambridge 9709, Pure 1) |
| **Feature Page** | `featurePage` | `/{feature-name}` | Product features (Exam Readiness Index, Smart Review) |
| **Audience Segment Page** | `audienceSegmentPage` | `/for/{segment}/` | Segment landing pages (resitters, tutors, international students) |
| **Location Page** | `locationPage` | `/countries/{country}/` | Geographic/country pages (UAE, Pakistan, Malaysia) |
| **Past Papers Hub** | `pastPapersHub` | `/past-papers/` | Past paper resources |
| **Landing Page** | `landingPage` | `/` or `/{page}` | Marketing/product pages |

**State the determined content type explicitly** and confirm with the user before proceeding.

### Step 3: Load Available Components

The current Sanity block types available for portable text content:

#### Portable Text Block Types
| Block Type | Sanity Schema | Frontend Component | Purpose |
|---|---|---|---|
| `mathBlock` | `objects/mathBlock.ts` | `MathBlock.tsx` | LaTeX math (inline/block), displayMode, caption |
| `calloutBlock` | `objects/calloutBlock.ts` | `CalloutBlock.tsx` | 5 variants: exam-tip, common-mistake, examiner-says, remember, key-formula |
| `workedSolution` | `objects/workedSolution.ts` | `WorkedSolution.tsx` | Multi-step with question, difficulty, marks, steps (math + annotation), examiner note |
| `comparisonTable` | `objects/comparisonTable.ts` | `ComparisonTable.tsx` | Dynamic headers/rows, row highlighting, LaTeX in cells |
| `codeBlock` | (in blockContent) | `CodeBlock.tsx` | Syntax highlighting with language/filename labels |
| `faq` | `objects/faq.ts` | `FaqSection.tsx` | Accordion Q&A with FAQPage JSON-LD schema |
| `ctaBlock` | `objects/ctaBlock.ts` | (CTA rendering) | Call-to-action blocks |
| Image blocks | (in blockContent) | `SanityImage.tsx` | With alt text (required) and captions |

#### Standard Marks/Annotations
- Bold, italic, underline, strikethrough, code
- External links (with target control)
- Internal references (post, examBoardHub, topicPage, pastPaperPage, comparisonPage)

#### Supporting Components (frontend only, not Sanity blocks)
- `MathText.tsx` — Inline LaTeX parser with memoization cache
- `BlogJsonLd.tsx` — Structured data (BlogPosting, FAQPage, BreadcrumbList)
- `TableOfContents.tsx` — Auto-generated from H2/H3 headings
- `AuthorCard.tsx`, `RelatedPosts.tsx`, `ShareButtons.tsx`, `NewsletterCTA.tsx`

### Step 4: Map Brief Elements to Components

For each section in the brief's **Recommended Article Outline** and **Visual Suggestions**:

1. **Identify the content type** — Is it a formula, a worked example, an exam tip, a comparison, a diagram, a FAQ, etc.?
2. **Map to existing block** — Which Sanity block type handles this?
3. **Flag gaps** — If no existing block fits, flag it with:
   - What the element is
   - Whether there's a reuse case (will this appear in future articles?)
   - Suggested approach (new component vs. workaround with existing blocks)

### Step 5: Generate Visual Assets

For any visual element mapped as a diagram/graph/illustration, choose the right tool:

#### Decision: Matplotlib vs Excalidraw

| Use **Matplotlib** (`diagram_generator.py`) | Use **Excalidraw** (`.excalidraw` JSON) |
|---|---|
| Mathematical curves (functions, trig, polynomials) | Flowcharts, decision trees, process flows |
| Graphs with axes, gridlines, plotted points | Box-and-arrow layouts (input → process → output) |
| Side-by-side function comparisons | Conceptual diagrams (no mathematical curves) |
| Shaded regions (integration, area under curves) | Text-heavy grids or tables with annotations |
| Stationary points, tangent lines, asymptotes | Hierarchical/tree structures |
| Transformations showing before/after curves | Venn diagrams, set diagrams |
| Any diagram requiring mathematical accuracy | Mind maps, relationship diagrams |

**When borderline, default to Matplotlib.** The output is higher quality, mathematically precise, and brand-consistent via `DiagramGenerator`.

#### Matplotlib workflow
1. Add a generation call to the `if __name__ == '__main__'` block of `data_sources/modules/diagram_generator.py` (or create a topic-specific script that imports `DiagramGenerator`)
2. Run: `python data_sources/modules/diagram_generator.py drafts/assets`
3. SVGs are generated directly — no manual conversion step needed
4. Available methods on `DiagramGenerator`:
   - `inverse_function_reflection()` — f and f⁻¹ with y=x mirror
   - `horizontal_shift_explanation()` — why f(x+a) shifts opposite
   - `one_one_vs_many_one()` — side-by-side horizontal line test
   - `function_transformation()` — single original vs transformed curve
   - `transformation_grid()` — 2x2 or 2x3 grid of transformations
   - `curve_with_annotations()` — generic curves with text/arrow annotations
   - `shaded_area()` — area between two curves (integration)
   - `stationary_points_diagram()` — curve with classified max/min/inflection
5. If no existing method fits, add a new reusable method to the class (not a one-off script)

#### Excalidraw workflow
1. Generate a `.excalidraw` JSON file with the diagram content
2. Save to `drafts/assets/` with a descriptive filename
3. User converts to SVG manually (open in Excalidraw → export)

#### Mapping notation
- Matplotlib assets: `[IMAGE: description (matplotlib → filename.svg)]`
- Excalidraw assets: `[IMAGE: description (excalidraw → filename.excalidraw)]`

### Step 6: Output Component Mapping Report

Output a structured mapping table (human-readable):

```
## Component Mapping: [Article Title]

### Content Type: [type from taxonomy]
### Sanity Type: [sanityType]
### Slug: [just the topic/page name]
### URL: [full URL path]

### Block Usage Summary
| Block Type | Count | Sections Used In |
|---|---|---|

### Detailed Mapping

#### [Section from outline]
- **Content type**: [formula / worked example / callout / etc.]
- **Sanity block**: [mathBlock / workedSolution / calloutBlock / etc.]
- **Target field** (topicPage only): [keyFormulas / examTips / workedExamples / body]
- **Notes**: [Any specifics — variant, difficulty level, etc.]

### Visual Assets
| # | Description | Tool | File | Notes |
|---|---|---|---|---|
| 1 | [description] | Matplotlib | `filename.svg` | [method used or "new method needed"] |
| 2 | [description] | Excalidraw | `filename.excalidraw` | [user converts to SVG] |

### New Component Proposals (if any)
| Element | Reuse Case | Recommendation |
|---|---|---|
| [element] | [where else it would be used] | [build / skip / workaround] |
```

### Step 7: Scaffold JSON Data File

Generate a JSON data file following the refactored content pipeline structure. Save to `spyglass/scripts/content/{type-folder}/{slug}.json`.

**File paths by content type:**
- Topic pages: `scripts/content/topics/{hub-slug}/{topic-slug}.json`
- Blog posts: `scripts/content/blog/{category}/{slug}.json`
- Alternative pages: `scripts/content/alternatives/{competitor}.json`
- Best-of pages: `scripts/content/best-of/{slug}.json`
- Hub pages: `scripts/content/hubs/{slug}.json`
- Feature pages: `scripts/content/features/{slug}.json`
- Audience segment pages: `scripts/content/audience-segments/{segment}.json`
- Location pages: `scripts/content/countries/{country}.json`

**The JSON file should contain:**
- `type`: Content type from taxonomy
- `metadata`: title, slug, seo (metaTitle, metaDescription), topicName, definition, practiceCtaText, parentHub slug
- `assets`: Array of SVG files needed with file, label, alt, caption
- `commonMistakes`: Array of {mistake, correction} (for topicPage)
- `faqs`: Array of {question, answer}
- Content field arrays: `keyFormulas`, `examTips`, `workedExamples`, `body` (for topicPage structured format)

**At this stage, content field arrays should be scaffolded with placeholder sections** that indicate what content goes where. The actual text, formulas, and worked solutions get populated during `/write`.

#### JSON Block Type Reference

Every block in `keyFormulas`, `examTips`, `workedExamples`, and `body` arrays MUST use one of these types. **Never use plain `paragraph` blocks for content that should be a callout, worked solution, comparison table, or image.** The visual quality of the published page depends entirely on using the right block types.

```json
// Paragraph — plain text only. Use sparingly for transitions/context.
{ "type": "paragraph", "text": "Plain text paragraph." }

// Heading — H2, H3, H4 section headers
{ "type": "heading", "level": 3, "text": "Section Title" }

// Math Block — LaTeX formulas (the core visual element for maths content)
{ "type": "mathBlock", "latex": "\\int x^n \\, dx = \\frac{x^{n+1}}{n+1} + C", "displayMode": true, "caption": "The power rule" }

// Callout — 5 variants: exam-tip, common-mistake, examiner-says, remember, key-formula
{ "type": "callout", "variant": "exam-tip", "title": "Optional title", "body": ["First paragraph of callout text.", "Second paragraph if needed."] }
{ "type": "callout", "variant": "common-mistake", "title": "Sign errors", "body": ["Description of the mistake and how to avoid it."] }
{ "type": "callout", "variant": "examiner-says", "title": "Examiner insight", "body": ["Direct quote or paraphrase from examiner report."] }
{ "type": "callout", "variant": "remember", "title": "Key point", "body": ["Important concept to remember."] }
{ "type": "callout", "variant": "key-formula", "title": "Mark Breakdown", "body": ["Paper 1 = 75 marks. Integration = 15-20 marks (20-27%)."] }

// Worked Solution — step-by-step with math + annotations (the signature visual element)
{ "type": "workedSolution", "question": "Find \\( \\int 3x^2 dx \\)", "difficulty": "easy", "marks": 3,
  "steps": [
    { "math": "\\int 3x^2 \\, dx", "annotation": "Apply the power rule to each term" },
    { "math": "= \\frac{3x^3}{3} + C = x^3 + C", "annotation": "Add 1 to power, divide by new power, add +C" }
  ],
  "examinerNote": "Optional examiner insight about this question type"
}

// Comparison Table — with headers, rows, and optional row highlighting
{ "type": "comparisonTable", "caption": "Integration techniques", "headers": ["Type", "Method", "Example"],
  "rows": [
    { "cells": ["Powers of x", "Power rule", "∫ 3x² dx"] },
    { "cells": ["(ax+b)^n", "Reverse chain rule", "∫ (2x+1)³ dx"], "highlight": true }
  ]
}

// Image — references an asset by filename (must be in the assets array)
{ "type": "image", "file": "flowchart.svg", "alt": "Descriptive alt text for accessibility", "caption": "Caption shown below image" }

// List — bulleted or numbered. Items can be plain strings or arrays of spans with marks.
{ "type": "list", "style": "numbered", "items": ["Step 1 text", "Step 2 text", "Step 3 text"] }
{ "type": "list", "style": "bulleted", "items": ["Plain item", "Another item"] }

// List with bold marks (e.g., syllabus codes) — use span arrays:
{ "type": "list", "style": "bulleted", "items": [
  [{ "text": "1.8.1", "marks": ["strong"] }, " — Integration as the reverse of differentiation"],
  [{ "text": "1.8.2", "marks": ["strong"] }, " — Integration of (ax + b)ⁿ for any rational n"],
  [{ "text": "1.8.3", "marks": ["strong"] }, " — Evaluating definite integrals"]
] }

// Paragraph with links — for internal/external links within text
{ "type": "paragraphWithLinks", "segments": [
  "This guide maps to Topics 1.8.1–1.8.5 of the ",
  { "text": "Cambridge 9709 syllabus", "href": "https://www.cambridgeinternational.org", "blank": true },
  ". If you've already covered ",
  { "text": "differentiation", "href": "/cambridge/9709/pure-1/differentiation/" },
  ", you have a head start."
] }

// Blockquote — for introductory callouts or citations
{ "type": "blockquote", "text": "This guide is part of our Complete Cambridge 9709 Pure 1 Revision Guide." }
```

#### Content Distribution Rules (topicPage)

Each article section maps to a specific structured field. **Do not put everything in `body`.**

| Article Section | topicPage Field | Expected Block Types |
|---|---|---|
| Formulas and rules | `keyFormulas` | `heading` → `mathBlock` → `paragraph` (explanation). Include `image` for visual derivations. |
| Decision frameworks, revision strategy, exam tips, flowcharts | `examTips` | `heading` → `paragraph`/`comparisonTable`/`image` → `callout(exam-tip)` → `workedSolution` (verification examples). This is the richest section visually. |
| Common mistakes from examiner reports | `commonMistakes` | Array of `{mistake, correction}` objects (NOT portable text blocks) |
| Worked solutions and practice questions | `workedExamples` | `heading` → `workedSolution` → `image` (diagrams). Place images AFTER the worked solution they illustrate. |
| Intro, syllabus scope, connections, CTA | `body` | `blockquote` (hub link) → `paragraph` → `heading` → `list` → `callout(key-formula)` → `image` → `paragraph` (CTA with links). |
| FAQ section | `faqs` | Array of `{question, answer}` objects (NOT portable text blocks) |

#### Visual Quality Checklist

Before finalising a JSON file, verify:
- [ ] Every formula uses `mathBlock` (not inline LaTeX in a paragraph)
- [ ] Every exam tip/insight uses a `callout` block (not a bold paragraph)
- [ ] Every worked example uses `workedSolution` with step-by-step `math` + `annotation`
- [ ] Every method comparison uses `comparisonTable` (not a markdown-style table in text)
- [ ] Every SVG asset is referenced as an `image` block in the section where it belongs
- [ ] Images are placed contextually (after the content they illustrate, not just listed in `assets`)
- [ ] `examTips` contains the richest mix of block types (tables, callouts, images, worked solutions)
- [ ] `body` contains the intro blockquote, syllabus scope, area diagrams, and CTA — not the teaching content

#### Example: Fully Populated examTips Section

This shows the visual density expected — mixing headings, paragraphs, images, tables, callouts, and worked solutions:

```json
"examTips": [
  { "type": "heading", "level": 3, "text": "Which method should you use?" },
  { "type": "paragraph", "text": "For 9709 Pure 1, there are only three paths:" },
  { "type": "image", "file": "method-flowchart.svg", "alt": "Decision flowchart for choosing integration method", "caption": "Which method to use in 9709 Pure 1" },
  { "type": "comparisonTable", "caption": "Integration techniques", "headers": ["Type", "Method", "Key Step"],
    "rows": [
      { "cells": ["Powers of x", "Power rule", "Add 1 to power, divide by new power"] },
      { "cells": ["(ax+b)^n", "Reverse chain rule", "Also divide by coefficient of x"], "highlight": true }
    ]
  },
  { "type": "callout", "variant": "exam-tip", "body": ["Differentiate your answer to check. If you get back the original expression, your integration is correct."] },
  { "type": "heading", "level": 3, "text": "The 30-second answer check" },
  { "type": "workedSolution", "question": "You got (2x+3)^5/10 + C. Verify.", "difficulty": "easy",
    "steps": [
      { "math": "\\frac{d}{dx}\\Big[\\frac{(2x+3)^5}{10}\\Big] = \\frac{5(2x+3)^4 \\times 2}{10}", "annotation": "Differentiate using chain rule" },
      { "math": "= (2x+3)^4", "annotation": "Matches the original. Integration is correct." }
    ]
  },
  { "type": "heading", "level": 3, "text": "Revision strategy" },
  { "type": "paragraph", "text": "Stage 1 — Learn the rules (Days 1-3). Focus on power rule and reverse chain rule." },
  { "type": "paragraph", "text": "Stage 2 — Practice by sub-topic (Days 4-10)." },
  { "type": "paragraph", "text": "Stage 3 — Exam simulation (Days 11+). Use past papers under timed conditions." }
]
```

Example scaffold for a topic page:
```json
{
  "type": "topicPage",
  "metadata": {
    "title": "...",
    "slug": "differentiation",
    "topicName": "Differentiation",
    "definition": "...",
    "practiceCtaText": "Practice differentiation with AI-powered questions calibrated to your level",
    "parentHub": "pure-1",
    "seo": {
      "metaTitle": "...",
      "metaDescription": "..."
    }
  },
  "assets": [
    { "file": "decision-flowchart.svg", "label": "...", "alt": "...", "caption": "..." }
  ],
  "keyFormulas": [
    { "type": "heading", "level": 3, "text": "Power Rule" },
    { "type": "mathBlock", "latex": "PLACEHOLDER", "displayMode": true, "caption": "..." },
    { "type": "paragraph", "text": "PLACEHOLDER — explanation of the rule" }
  ],
  "examTips": [
    { "type": "heading", "level": 3, "text": "PLACEHOLDER — decision framework" },
    { "type": "image", "file": "decision-flowchart.svg", "alt": "PLACEHOLDER", "caption": "PLACEHOLDER" },
    { "type": "comparisonTable", "caption": "PLACEHOLDER", "headers": ["PLACEHOLDER"], "rows": [] },
    { "type": "callout", "variant": "exam-tip", "body": ["PLACEHOLDER"] },
    { "type": "workedSolution", "question": "PLACEHOLDER", "difficulty": "easy", "steps": [] }
  ],
  "commonMistakes": [
    { "mistake": "PLACEHOLDER", "correction": "PLACEHOLDER" }
  ],
  "workedExamples": [
    { "type": "heading", "level": 3, "text": "PLACEHOLDER — sub-topic" },
    { "type": "workedSolution", "question": "PLACEHOLDER", "difficulty": "easy", "marks": 3, "steps": [] }
  ],
  "body": [
    { "type": "blockquote", "text": "This guide is part of our Complete Cambridge 9709 Pure 1 Revision Guide." },
    { "type": "heading", "level": 2, "text": "PLACEHOLDER — syllabus scope" },
    { "type": "paragraph", "text": "PLACEHOLDER" },
    { "type": "callout", "variant": "key-formula", "title": "Mark Breakdown", "body": ["PLACEHOLDER"] },
    { "type": "heading", "level": 2, "text": "PLACEHOLDER — connections to other topics" },
    { "type": "paragraph", "text": "PLACEHOLDER" },
    { "type": "heading", "level": 2, "text": "Summary" },
    { "type": "paragraph", "text": "PLACEHOLDER" }
  ],
  "faqs": [
    { "question": "PLACEHOLDER", "answer": "PLACEHOLDER" }
  ]
}
```

### Step 8: Topic Page Anti-Regression Checklist

Before generating the JSON, verify these are scaffolded. Reference `integration.json` as the gold standard.

**Body section:**
- [ ] Introductory hook paragraph (emotional, connects with student — not a dry factual opening)
- [ ] H3 "What's in scope for Paper 1" with bullet list using **bold syllabus codes** (1.8.1, 1.8.2, etc.) — NEVER flatten to semicolon-separated paragraph
- [ ] Mark breakdown callout (`variant: "key-formula"`, title: "Mark breakdown")
- [ ] Inline callouts placed where contextually relevant (common-mistake, remember) — not only in examTips
- [ ] Dedicated visual H3 section ("Understanding areas visually" or equivalent) grouping diagrams + explanatory callouts — never dump multiple images back-to-back without heading/text
- [ ] Internal links via `paragraphWithLinks` to related topics, hub, and past papers
- [ ] "What to Do Next" closing H2 with: revision advice, ExamPilot CTA paragraph, past papers link, next-topic link

**examTips section:**
- [ ] Decision flowchart IMAGE and comparison TABLE both present (they serve different purposes)
- [ ] Verification worked solution as proper `workedSolution` block with math steps (not just prose)
- [ ] At least one `callout variant="remember"` for the most critical trap

**workedExamples section:**
- [ ] H3 title heading BEFORE every workedSolution block (e.g., "Basic integration", "Reverse chain rule")
- [ ] Full technique coverage: basic power rule, rewriting (roots/fractions), reverse chain rule, definite integral, negative power, area between curves, area below x-axis (7+ examples minimum)

**commonMistakes:**
- [ ] Examiner report quotes embedded in correction text with year attribution — e.g., `As the examiner report notes: "..." (2024)`

**Assets:**
- [ ] ALL visual assets from the original draft included (flowcharts, area diagrams, negative-area-trap, area-between-curves) — never drop a diagram just because a table covers similar content

**Anti-patterns (never do these):**
- Never flatten a bullet list into a semicolon-separated paragraph
- Never drop callouts from body just because they appear in examTips
- Never replace a flowchart image with only a table
- Never omit worked example titles (H3 headings before each workedSolution)
- Never compress body into generic summary paragraphs
- Never drop the introductory hook

### Step 9: Readiness Checklist

```
### Ready for /write?
- [ ] Content type determined and confirmed
- [ ] All content mapped to existing blocks
- [ ] All visual assets generated (matplotlib SVGs + Excalidraw files)
- [ ] No unresolved component gaps (or gaps discussed and resolved)
- [ ] JSON data file scaffolded at correct path
- [ ] Slug follows correct pattern for this content type
- [ ] Parent hub / category exists
- [ ] Anti-regression checklist (Step 8) passed
```

## After Approval
Once the user confirms the mapping, they can run `/write [topic]` and the writer will:
1. Follow the component mapping for block placement
2. Populate the JSON data file with actual content
3. Generate the markdown draft (for human review)

## Sanity Publishing Checklist

Before creating the Sanity document, verify:

### Slug Pattern (by content type)
- **Topic pages**: slug is JUST the topic name (e.g., `differentiation`, `integration`, `vectors`). Hub provides the URL prefix.
- **Blog posts**: slug is the article slug (e.g., `best-way-to-revise-a-level-maths`)
- **Alternative pages**: slug is the competitor name (e.g., `save-my-exams`)
- **Hub pages**: slug is the hub identifier (e.g., `pure-1`, `cambridge-9709`)
- Do NOT use full path slugs

### Parent Relationships
- **Topic pages** -> parent hub (Cambridge 9709 Pure 1 hub slug: `pure-1`)
- **Blog posts** -> category reference
- **Hub pages** -> parent hub (for child hubs)
- Find existing parents, don't create duplicates

### Content Distribution (topicPage only)
Map article sections to the correct structured field:

| Article Section | topicPage Field |
|---|---|
| Formulas and rules | `keyFormulas` |
| Decision frameworks, revision strategy, exam tips, flowcharts | `examTips` |
| Common mistakes from examiner reports | `commonMistakes` (array of {mistake, correction}) |
| Worked solutions and practice questions | `workedExamples` |
| Intro, syllabus scope, mark breakdown, connections, CTA | `body` |
| FAQ section | `faqs` (array of {question, answer}) |

### Script to Use
- **Current (until refactoring is complete)**: Create a per-topic `.mjs` script in `spyglass/scripts/` following `create-integration-topicpage.mjs` pattern
- **After refactoring**: `node scripts/create-content.mjs scripts/content/{type}/{slug}.json`

## Updating This Process
This command should be updated when:
- New Sanity block types are added to `studio-spyglass/schemaTypes/`
- New portable text components are added to `exampilot/components/blog/portable-text/`
- Block types are deprecated or renamed
- New content types are added to the taxonomy
- The refactored content pipeline (`create-content.mjs`) is built

The canonical content type taxonomy lives in `spyglass/docs/CONTENT_GENERATION_REFACTORING_GUIDE.md`.
