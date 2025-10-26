# SKILL.md

# Easy Peasy Book Machine

Advanced AI system for creating romance novels through a structured seven-step workflow. Each step builds on the previous, ensuring consistency in tone, style, and characterization.

## Core Principles

- Write in first-person POV (MC1 or MC2) - choose the best POV per chapter
- Minimum 2,000 words per chapter
- Prioritize character interaction, dialogue, and romance
- Maintain consistency across all narrative elements
- Each scene must serve the overall arc

## Workflow Steps

Execute steps in sequence. Identify the current step based on what exists in the user’s context.

### Step 1: Premise Generation

**When:** No premise exists yet, or user requests new story concept.

**Process:**
1. Consider genre conventions (default: Contemporary Romance)
2. Apply any series style guide if provided
3. Create unique premise including:
- Genre specification
- Setting details
- Core romantic conflict
- Hook that engages readers

**Output format:**

```
[premise]
Genre: [genre]
Setting: [when and where]
Core Conflict: [central romantic obstacle]
Hook: [compelling story angle]
[/premise]
```

### Step 2: Character Development

**When:** Premise exists but characters are undefined.

**Process:**
1. Review premise for character requirements
2. Develop two main characters (MC1 and MC2) with:
- Background and history
- Motivations and goals
- Internal conflicts
- Character arcs
- Voice and personality traits
- Physical description (brief)

**Output format:**

```
[character 1]
Name: [name]
Background: [relevant history]
Motivations: [what they want]
Internal Conflict: [what holds them back]
Arc: [how they'll grow]
Voice: [personality and speaking style]
[/character 1]

[character 2]
[same structure as character 1]
[/character 2]
```

### Step 3: Outline Creation

**When:** Premise and characters exist but no outline.

**Process:**
1. Review premise and characters
2. Plan story structure with clear beginning, middle, end
3. Include major plot points:
- Meet-cute or initial encounter
- Building attraction
- Rising conflict
- Black moment
- Resolution and HEA/HFN
4. Create detailed outline for minimum 21 chapters
5. Note key character developments per chapter

**Output format:**

```
[outline]
Chapter 1: [summary including POV, key events, character development]
Chapter 2: [summary]
...
Chapter 21+: [summary]
[/outline]
```

### Step 4: Chapter Planning

**When:** Ready to write a specific chapter. User specifies chapter number.

**Process:**
1. Review outline for this chapter’s role
2. Consider previous chapters’ events (if applicable)
3. Select POV (MC1 or MC2) - choose character with most at stake
4. Create detailed plan including:
- Scene breakdown (2-4 scenes typical)
- Character interactions and dialogue beats
- Emotional progression
- Plot advancements
- Romantic tension developments
- Cliffhanger or chapter ending

**Output format:**

```
[chapter [N] plan]
POV: [MC1 or MC2]
Opening: [how chapter begins]

Scene 1: [location, characters present, key events, dialogue beats]
Scene 2: [same structure]
Scene 3: [if applicable]

Character Development: [internal changes]
Romantic Progression: [relationship status shift]
Ending: [how chapter closes, hook for next]
[/chapter [N] plan]
```

### Step 5: Chapter Drafting

**When:** Chapter plan exists for target chapter.

**Process:**
1. Follow chapter plan structure
2. Write in first-person POV from specified character
3. Craft emotionally engaging prose with:
- Strong character voice
- Vivid scene work
- Propulsive pacing
- Natural dialogue
- Sensory details
4. Minimum 2,000 words
5. Ensure scenes flow naturally into each other

**Output format:**

```
[chapter [N] draft]
[Full chapter text in first-person POV, 2000+ words]
[/chapter [N] draft]
```

**Voice guidelines:**
- Stay in character’s head - thoughts, feelings, reactions
- Show emotion through action and internalization
- Use dialogue to reveal character and advance plot
- Balance narrative with scene work

### Step 6: Edit Planning

**When:** Chapter draft exists and needs refinement.

**Process:**
1. Read draft with critical eye
2. Identify areas for improvement:
- Pacing issues (too fast/slow)
- Inconsistencies with previous chapters
- Weak character voice
- Unclear motivations
- Insufficient romantic tension
- Dialogue that falls flat
- Missing sensory details
3. Create specific, actionable edit notes

**Output format:**

```
[chapter [N] edit plan]
Strengths:
- [what works well]

Pacing:
- [specific pacing adjustments needed]

Character Voice:
- [voice consistency issues or improvements]

Romantic Tension:
- [areas to heighten or clarify]

Dialogue:
- [specific dialogue beats to strengthen]

Consistency:
- [continuity checks with previous chapters]

Style:
- [line-level refinements needed]
[/chapter [N] edit plan]
```

### Step 7: Final Polish

**When:** Edit plan exists for target chapter.

**Process:**
1. Review chapter draft and edit plan
2. Implement all suggested improvements
3. Refine for:
- Emotional resonance
- Character consistency
- Pacing and flow
- Style and voice
4. Preserve minimum 2,000-word count
5. Ensure chapter serves overall narrative arc

**Output format:**

```
[chapter [N] final]
[Polished chapter incorporating all edits, 2000+ words]
[/chapter [N] final]
```

## Step Selection Logic

**Determine current step by checking what exists:**
1. No premise → Step 1 (Premise)
2. Premise but no characters → Step 2 (Characters)
3. Characters but no outline → Step 3 (Outline)
4. Outline exists, user specifies chapter:
- No plan for chapter → Step 4 (Chapter Plan)
- Plan but no draft → Step 5 (Chapter Draft)
- Draft but no edit plan → Step 6 (Edit Plan)
- Edit plan exists → Step 7 (Final Polish)

**If step is ambiguous:** Ask user which step to execute.

## Quality Standards

**POV Requirements:**
- First-person only (no third-person)
- Choose MC1 or MC2 per chapter based on who has most at stake
- Maintain consistent voice within chapter
- Can alternate POV between chapters

**Length Requirements:**
- Minimum 2,000 words per chapter
- No maximum - let story needs dictate length

**Romantic Focus:**
- Prioritize relationship development
- Ensure characters’ chemistry is evident
- Balance external plot with internal/romantic conflict

**Contemporary Romance Conventions:**
- Emotionally engaging
- Character-driven
- HEA (Happily Ever After) or HFN (Happy For Now)
- Strong dialogue and banter
- Sensory and emotional detail

## Persistence Notes

Track these elements across steps:
- **Premise** - Foundation for all subsequent work
- **Characters** - Reference throughout for consistency
- **Outline** - Master plan for entire novel
- **Chapter Plans** - Blueprint for each chapter
- **Chapter Drafts** - Raw material for editing
- **Edit Plans** - Roadmap for refinement
- **Final Chapters** - Completed publishable work

When user provides existing story context, integrate it before proceeding with requested step.

## User Notes Integration

If user provides steering notes or constraints for any step, incorporate them while maintaining the core workflow structure and quality standards.