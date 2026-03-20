# ExamPilot Features & Benefits

## Product Overview

ExamPilot is an AI-powered exam readiness platform for A-Level Mathematics students. It tells students exactly where they stand, what they need to work on, and guides them to their target grade through adaptive practice, AI tutoring, and spaced repetition.

**Tagline**: Know exactly where you stand and what to do next to improve your predicted grade.

**URL**: https://www.exampilot.io

## Exam Board Support

| Exam Board | Qualification | Spec Code | Status |
|---|---|---|---|
| Cambridge International | A-Level Mathematics | 9709 | Launch focus (80%) |
| Pearson Edexcel | International A-Level Pure Mathematics | WMA11/WMA12 | Launch focus (20%) |

Future expansion: GCSE Maths, Additional Maths, Statistics, Mechanics, other A-Level subjects.

## Core Features

### Exam Readiness Index (ERI)
**What it does**: Generates a predictive grade (A*-U) based on your actual performance data — not a quiz score, but a statistically modelled prediction of your exam outcome.
**Why it matters**: Students stop guessing and start knowing. Conditional university offers require specific grades — ERI tells you if you're on track.
**Differentiator**: No other A-Level tool provides a continuously-updated predicted grade based on adaptive assessment.

### Question Bank
**What it does**: Browse and practice questions by topic, difficulty, and exam board. Every question mapped to the syllabus.
**Why it matters**: Targeted practice on exactly what you need — not random questions from a generic pool.
**Differentiator**: Questions tagged with Question DNA — the underlying reasoning patterns, not just topic labels.

### Module Tests
**What it does**: Structured tests covering specific syllabus modules (e.g., Pure 1, Pure 2).
**Why it matters**: Simulates real exam conditions for specific papers.
**Differentiator**: Adaptive difficulty based on your proficiency level.

### ExamLens (Mock Exams)
**What it does**: Generates predictive timed mock papers that mirror real A-Level exam conditions.
**Why it matters**: The closest thing to sitting the real exam. Timed, formatted correctly, difficulty-calibrated.
**Differentiator**: Questions selected based on your specific knowledge gaps — not random sampling.

### Ask Sparky (AI Tutor)
**What it does**: Socratic AI tutor available during practice sessions. Never gives the answer — asks guiding questions until you reach understanding.
**Why it matters**: 24/7 help for international students who can't access teachers outside school hours.
**Differentiator**: Socratic method (not answer-giving), context-aware (knows the specific question you're working on), costs 1 Sparx credit per use.

### Smart Review (Spaced Repetition)
**What it does**: FSRS-powered system that resurfaces content at optimal intervals to prevent forgetting.
**Why it matters**: Cramming doesn't work. Smart Review ensures long-term retention of concepts.
**Differentiator**: Integrated into the learning flow (not a separate flashcard app). Tracks forget risk, memory debt, and stability momentum.

### Dashboard
**What it does**: Personalised daily overview — streaks, progress, knowledge health, at-risk topics, study plan.
**Why it matters**: One screen that tells you what to do today.
**Differentiator**: Predicted score, topic accuracy breakdown, and knowledge state visualisation in one view.

### Progress Tracking
**What it does**: Track mastery across all topics over time. See improvement trajectories.
**Why it matters**: Motivation through visible progress. Identify persistent weak spots.

### Sparx (Virtual Currency)
**What it does**: Earn credits through study activity. Spend on premium features (Ask Sparky, advanced analysis).
**Why it matters**: Gamification that rewards consistent study behaviour.

### Settings & Personalisation
**What it does**: Set exam board, exam date, target grade, notification preferences, theme.
**Why it matters**: Tailored experience from day one.

## Key Differentiators (vs Competitors)

| ExamPilot | Save My Exams | Physics & Maths Tutor | Generic Apps |
|---|---|---|---|
| Predicted grade (ERI) | No prediction | No prediction | No prediction |
| Adaptive questions | Static papers | Static resources | Random difficulty |
| Socratic AI tutor | No AI | No AI | Answer-giving chatbots |
| Spaced repetition (FSRS) | No retention system | No retention system | Basic flashcards |
| Cambridge 9709 + Edexcel IAL specific | Broad coverage | Broad coverage | Generic maths |
| Question DNA (reasoning patterns) | Topic labels only | Topic labels only | No classification |

## Technology Stack (for technical content)

- Next.js 15 (App Router)
- FastAPI backend with 22+ AI agents
- Supabase (Auth + DB)
- Sanity CMS (marketing content)
- Claude 3.5 Haiku (Ask Sparky)
- FSRS (spaced repetition algorithm)
- Deployed on Vercel + Railway

## Company Information

- **Founded**: 2025
- **Founders**: Enitan Williams, Teresa
- **Based**: Spain (serving globally)
- **Mission**: Help every A-Level Maths student know exactly where they stand and what to do next
- **Stage**: Pre-launch, onboarding first 100 users
