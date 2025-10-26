# Automatic Book Machine - Usage Guide

## What's Included

### Main Skill File
- **SKILL.md** - Complete workflow orchestration with decision tree and parameter collection

### Reference Files (Loaded as needed)
- **romance.md** - Romance genre conventions, pacing, heat levels, tropes, dialogue patterns
- **thriller.md** - Thriller conventions, tension building, antagonist patterns, pacing techniques
- **story-structures.md** - Multiple story frameworks (Three-Act, Hero's Journey, Save the Cat, etc.)
- **dialogue.md** - Dialogue best practices, voice differentiation, subtext, formatting

### Validation Scripts
- **word_counter.py** - Tracks word counts per chapter and total manuscript
- **tag_validator.py** - Ensures all square bracket tags are properly opened and closed
- **continuity_checker.py** - Tracks character names and identifies inconsistencies

---

## How to Use

### 1. Install the Skill
Upload `automatic-book-machine.skill` to Claude via the Skills interface.

### 2. Invoke the Skill
Simply say: "Write a book" or "Generate a novel using the automatic book machine"

### 3. Provide Parameters
The skill will request these parameters:

**Required:**
- Genre (Romance, Thriller, Fantasy, Sci-Fi, Literary, Mystery, Horror, etc.)
- Target word count (50k-120k words)
- Chapter count (minimum 10)

**Optional:**
- POV (First person, Third person limited, etc.)
- Content rating (for intimate scenes)
- Story structure preference (Three-Act, Hero's Journey, etc.)

### 4. Autonomous Execution
Once parameters are confirmed, the book machine will:
- Create premise and characters
- Generate detailed chapter outline
- Write each chapter with plan → draft → edit → final workflow
- Perform continuity review
- Generate completion summary

### 5. Validation
After completion, the skill will suggest running validation scripts to check:
- Word counts meet requirements
- All tags are properly formatted
- Character name consistency

---

## Customization Options

### Genre-Specific Generation
When you select Romance or Thriller, the skill automatically loads detailed genre-specific guidance including:
- Pacing requirements
- Scene distribution
- Genre conventions
- Reader expectations

### Story Structure Selection
Choose from multiple proven story frameworks:
- Three-Act Structure (default, universal)
- Hero's Journey (adventure, transformation arcs)
- Save the Cat (commercial fiction)
- Seven-Point Structure (mystery, thriller)
- Five-Act Structure (literary, classical)
- Kishotenketsu (non-conflict narratives)

### Content Rating (Romance)
Control intimacy levels:
- **Sweet/Closed Door**: Fade to black
- **Medium Heat**: Sensual but not explicit
- **High Heat**: Detailed intimate scenes (25+ characters only)

---

## Output Format

All outputs use square bracket tags for easy parsing:

```
[premise]
Content here...
[/premise]

[character profiles]
Content here...
[/character profiles]

[story outline]
Content here...
[/story outline]

[chapter 1 plan]
Content here...
[/chapter 1 plan]

[chapter 1 draft]
Content here...
[/chapter 1 draft]

[chapter 1 edit plan]
Content here...
[/chapter 1 edit plan]

[chapter 1 final]
Content here...
[/chapter 1 final]

[... repeat for all chapters ...]

[continuity check]
Content here...
[/continuity check]

[manuscript complete]
Content here...
[/manuscript complete]
```

---

## Progressive Disclosure Design

The skill uses efficient context management:

1. **Metadata** - Always loaded (skill name and description)
2. **SKILL.md** - Loaded when skill is invoked
3. **Reference files** - Loaded only when needed based on genre/parameters
4. **Scripts** - Executed when validation requested (not loaded into context)

This ensures optimal token usage while providing comprehensive guidance.

---

## Quality Control

### Built-in Quality Gates
- Character profiles must be complete before outlining
- Outlines must meet minimum chapter count
- Every chapter must go through edit loop (no skipping)
- Edit plans must identify 5+ specific issues
- Final drafts must address all edit issues
- Continuity review must verify all arcs resolve

### Edit Loop Enforcement
Unlike simple generation, this skill mandates:
1. **Planning** before each chapter
2. **Drafting** the complete chapter
3. **Critical analysis** with specific, actionable feedback
4. **Revision** addressing all identified issues

This ensures publishable quality, not just first-draft content.

---

## Example Invocation

**You:** "Use the automatic book machine to write a romance novel"

**Claude:** "I'll use the automatic book machine to generate a complete romance novel. First, I need to collect some parameters..."

[Collects genre, word count, chapter count, POV, heat level, structure]

[Loads romance.md, story-structures.md, dialogue.md]

[Executes Phase 1: Foundation]
- Generates premise
- Creates 3-5 character profiles
- Outlines all chapters

[Executes Phase 2: Chapter Loop for each chapter]
- Plans chapter
- Drafts chapter
- Critiques draft with specific issues
- Revises into final version

[Executes Phase 3: Completion]
- Reviews continuity
- Generates summary

[Suggests validation scripts]

---

## Tips for Best Results

### Be Specific with Parameters
- Choose target word count based on genre expectations
- Romance: 50k-90k
- Thriller: 70k-100k
- Fantasy: 90k-120k+

### Let It Run Autonomously
- The skill is designed to execute without interruption
- Each chapter automatically proceeds to the next
- Intervention only needed for parameter changes

### Use Validation Scripts
- After completion, run the validation scripts
- They catch formatting issues and inconsistencies
- Help ensure manuscript quality

### Leverage Genre References
- Romance and Thriller have detailed genre-specific guidance
- Other genres use universal principles
- Consider adding custom genre references for your specific needs

---

## Advanced: Adding Custom References

To add genre references for Fantasy, Sci-Fi, Mystery, etc.:

1. Create new reference file (e.g., `references/fantasy.md`)
2. Follow the pattern in romance.md and thriller.md
3. Include: core requirements, pacing guidelines, genre conventions
4. Update SKILL.md decision tree to load your new reference

---

## Support & Iteration

This skill follows skill-creator best practices:
- Use on real tasks to identify improvements
- Notice struggles or inefficiencies
- Update SKILL.md or references as needed
- Test changes with validation scripts

The skill improves through iteration based on actual book generation experience.
