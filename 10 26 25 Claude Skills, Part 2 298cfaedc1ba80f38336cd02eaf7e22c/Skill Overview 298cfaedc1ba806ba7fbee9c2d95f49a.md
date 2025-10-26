# Skill Overview

# Automatic Book Machine - Skill Overview

## What's Included

### SKILL.md (Main Instructions)

- **Decision tree** for workflow initiation
- **User variable collection** (genre, heat level, themes, structure, etc.)
- **Configuration phase** with summary template
- **PHASE 1: Foundation** (premise, characters, outline)
- **PHASE 2: Chapter loop** (plan → draft → edit plan → final)
- **Validation instructions** for post-generation
- **Complete workflow** with all requirements

### Reference Files (Loaded as Needed)

**genre-patterns.md** (4,700 words)

- Romance (tropes, heat levels, story beats)
- Thriller/Suspense
- Science Fiction
- Fantasy
- Literary Fiction
- Mystery
- Horror
- Cross-genre advice

**story-structures.md** (3,200 words)

- Three-Act Structure
- Hero's Journey
- Save the Cat (15 beats)
- Seven-Point Story Structure
- Fichtean Curve
- Freytag's Pyramid
- Kishotenketsu
- In Medias Res
- Multiple POV structures
- Chapter distribution guides for each

**prose-quality.md** (3,800 words)

- Show don't tell
- Filter words to remove
- Active vs passive voice
- Clichés to avoid
- Dialogue best practices
- Sentence variety
- Pacing control
- POV consistency
- Description balance
- Avoiding purple prose
- Consistency checkers
- Chapter-level editing
- Line-level polish

**adult-fiction-standards.md** (4,000 words)

- Heat level spectrum (1-5)
- Consent and agency requirements
- Violence and intensity guidelines
- Mature themes handling
- Age-appropriate content (25-45)
- Genre-specific mature content
- Scene construction guidelines
- Language choices
- Quality standards
- Edit phase checklist

### Scripts (Executable Tools)

**chapter_validator.py**

- Validates all required tags present
- Checks tag balance (open/close pairs)
- Verifies foundation sections complete
- Confirms each chapter has all 4 sections
- Usage: `python scripts/chapter_validator.py <file>`

**continuity_tracker.py**

- Tracks characters (details, appearances)
- Tracks locations
- Manages plot threads (open/resolved)
- Timeline events
- Significant items (Chekhov's gun)
- Generates comprehensive reports
- Validates continuity issues
- Usage: `python scripts/continuity_tracker.py report <json>`

## How the Skill Works

### 1. Configuration Phase

AI collects user variables:

- Genre/subgenre
- Heat level (if applicable)
- Chapter count target
- Themes and tropes
- Story structure preference
- Tone and POV style

### 2. Reference Loading

Based on configuration, AI loads:

- `genre-patterns.md` for selected genre
- `story-structures.md` for outline planning
- `adult-fiction-standards.md` if heat level > 1
- `prose-quality.md` for editing phase

### 3. Foundation Phase

AI generates with proper tagging:

```
[premise development]
...content...
[/premise development]

[character creation]
...content...
[/character creation]

[story outline]
...content...
[/story outline]

```

### 4. Chapter Loop

For each chapter, AI executes:

```
[chapter X plan]
...detailed plan...
[/chapter X plan]

[chapter X draft]
...full chapter...
[/chapter X draft]

[chapter X edit plan]
...improvement analysis...
[/chapter X edit plan]

[chapter X final]
...polished chapter...
[/chapter X final]

```

### 5. Validation (Optional)

Run scripts to verify:

- Tag structure complete
- Continuity maintained
- Quality standards met

## Key Features

✅ **Decision-driven workflow** - Gathers preferences before starting
✅ **Genre-specific guidance** - Adapts to romance, thriller, fantasy, etc.
✅ **Heat level support** - Handles closed door to explicit content
✅ **Structure flexibility** - Multiple plotting frameworks available
✅ **Progressive disclosure** - Loads references only when needed
✅ **Quality enforcement** - Edit phase with detailed guidelines
✅ **Validation tools** - Scripts to check output structure
✅ **Continuity tracking** - Character and plot management system

## Token Efficiency

Main [SKILL.md](http://skill.md/): ~6,000 words

- Loaded every time skill is triggered
- Includes decision tree, workflow, instructions

References: ~16,000 words total

- Loaded selectively based on needs
- Only relevant references loaded per chapter
- Keeps context window lean

Scripts: Executable without loading

- Run for validation post-generation
- Don't consume context tokens
- Provide deterministic checking

## Usage Example

**User:** "Create an automatic book for me - a contemporary romance with medium heat, enemies to lovers trope, 12 chapters."

**AI Response:**

1. Confirms configuration with user
2. Loads genre-patterns.md (romance section)
3. Loads story-structures.md (Three-Act)
4. Loads adult-fiction-standards.md (heat level 2-3)
5. Executes [premise development]
6. Executes [character creation]
7. Executes [story outline]
8. Begins chapter loop
9. Loads prose-quality.md before first edit plan
10. Continues through all 12 chapters
11. Optionally validates with scripts

## Installation

1. Download automatic-book-machine.skill
2. Upload to Claude via Skills menu
3. Skill activates when user requests automatic book generation