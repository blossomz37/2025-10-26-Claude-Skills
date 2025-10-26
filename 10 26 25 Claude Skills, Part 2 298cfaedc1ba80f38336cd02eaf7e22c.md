# 10/26/25 Claude Skills, Part 2

**Last Week’s Experiments:** [10/19/25 Claude Skills, Part 1](https://www.notion.so/10-19-25-Claude-Skills-Part-1-291cfaedc1ba8034a742f5801de070b5?pvs=21) 

<aside>

Also check out [**Friday’s YT live demo**](https://www.youtube.com/live/Qv56_D-cVyE) with EAW & Ekello. Claude Skills starts at 1hr 46 minutes. EAW does first-look → writing a chapter that meets specified word count in about 25 minutes.

</aside>

---

### **Start:**

- Quick rundown of Claude Skills
    
    [to do in group]
    

---

### Experiment 1: brand-guidelines

Push the `brand-guidelines` skill to 

- analyze a website
- identify the existing styles
- formalize the brand guidelines
- improve the existing style **without** using its template/guide unless it’s for structural reference
- generate an artifact so we can compare before and after

[https://github.com/anthropics/skills/tree/main/brand-guidelines](https://github.com/anthropics/skills/tree/main/brand-guidelines)

---

### Experiment 2: EPBM

[https://support.claude.com/en/articles/12512198-how-to-create-custom-skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

**File requirements - A “SKILL” is**

- ZIP file that includes **exactly one** `SKILL.md` file at the root level
- `SKILL.md` contains a skill name and description formatted in YAML
- Can also have a .skill extension. Example: `make-amazing-stuff.skill`

---

### OG Version Revisited

Source:  ‣ 

- **Chat**
    - Ran this in incognito mode, so there’s no shareable link
    - It took Claude much longer to generate, but it wrote a complex is skill in 3 prompts.
    
    **PROMPT 1:** (Copy of Original EPBM Prompt)
    
    ```bash
    write me the steps for an ai to be an automatic book machine. It will have to make characters and outline and the premise and then write at least 10 chapters. It also needs to make a plan before it writes each chapter. Task responses should always be tagged using square brackets [ ] like this [chapter 1 plan] [/chapter 1 plan] for example. Also, after a chapter is drafted, the AI must understand it now goes into edit mode and make a plan to edit the chapter, labeled appropriately and then write a final draft.
    Write this very detailed prompt for me step by step for an AI. You must write it as PROMPT. So explain all the goals and the step by step modes and loops it will go through
    ```
    
    ---
    
    [Response (new EPBM Prompt)](10%2026%2025%20Claude%20Skills,%20Part%202%20298cfaedc1ba80f38336cd02eaf7e22c/Response%20(new%20EPBM%20Prompt)%20298cfaedc1ba8014a69afb1941841e4e.md)
    
    ---
    
    **PROMPT 2:** Do you have access to `skill-creator` guide that provides instructions for building Claude Skills. It's located at `/mnt/skills/examples/skill-creator/SKILL.md`.
    
    ---
    
    Yes, I have access to the skill-creator guide. I'll now create your automatic book machine as a proper Claude skill following the established patterns.
    
    Let me start by initializing the skill structure:
    
    Skill created with structured workflow:
    
    - PHASE 1: Foundation (premise, characters, outline)
    - PHASE 2: Chapter loop (plan → draft → edit plan → final)
    - Square bracket tagging enforced
    - Sequential execution with no gaps
    - Adult fiction standards (25-45 audience)
    
    Upload the .skill file to activate in new conversations.
    
    [SKILL.md](10%2026%2025%20Claude%20Skills,%20Part%202%20298cfaedc1ba80f38336cd02eaf7e22c/SKILL%20md%20298cfaedc1ba8093860afa97588178a9.md)
    
    [automatic-book-machine.zip](10%2026%2025%20Claude%20Skills,%20Part%202%20298cfaedc1ba80f38336cd02eaf7e22c/automatic-book-machine.zip)
    
    ---
    
    **PROMPT 3:** I noticed you did not use a decision tree, scripting, variables from the user, or additional files in a subdirectory. The only file in the skills zip was the md file. Is nothing else needed?
    
    ---
    
    **CLAUDE:** You're absolutely right. I created a minimal skill when a more robust design would serve you better. Let me redesign it with:
    
    1. **Decision tree** - To gather preferences and guide the workflow
    2. **Reference files** - For genre patterns, story structures, prose guidelines
    3. **User variables** - Genre, themes, heat level, chapter count, etc.
    4. **Scripts** - For word count tracking, continuity checking
    
    Let me rebuild it:
    
    [Skill Overview](10%2026%2025%20Claude%20Skills,%20Part%202%20298cfaedc1ba80f38336cd02eaf7e22c/Skill%20Overview%20298cfaedc1ba806ba7fbee9c2d95f49a.md)
    
    [SKILL-OVERVIEW.md](10%2026%2025%20Claude%20Skills,%20Part%202%20298cfaedc1ba80f38336cd02eaf7e22c/SKILL-OVERVIEW.md)
    
    [automatic-book-machine.zip](10%2026%2025%20Claude%20Skills,%20Part%202%20298cfaedc1ba80f38336cd02eaf7e22c/automatic-book-machine%201.zip)
    
    [automatic-book-machine.skill](10%2026%2025%20Claude%20Skills,%20Part%202%20298cfaedc1ba80f38336cd02eaf7e22c/automatic-book-machine.skill)
    

---

### POML Version

**EPBM Skills Chat:** [https://claude.ai/share/8fe363a2-a30c-46ba-ad18-0985c9003a86](https://claude.ai/share/8fe363a2-a30c-46ba-ad18-0985c9003a86)

> **TLDR;**
> 
> - Here’s the skill: [SKILL.md](10%2026%2025%20Claude%20Skills,%20Part%202%20298cfaedc1ba80f38336cd02eaf7e22c/SKILL%20md%20298cfaedc1ba817ca9d3c09434b74531.md) and the [Recommended Structure](10%2026%2025%20Claude%20Skills,%20Part%202%20298cfaedc1ba80f38336cd02eaf7e22c.md)
> - Customize it to your project, zip the files and save to **Claude > Settings > Capabilities > Skills**
> - Use in a Claude Project.

> **CHAT EXCERPT BELOW**
> 

**ME:** Do you know how to build a Skill for Claude Skills?

**CLAUDE:**

<aside>

```jsx
	Yes, I have access to a `skill-creator` guide that provides instructions for building Claude Skills. It's located at /mnt/skills/examples/skill-creator/SKILL.md.
Would you like me to read it and walk you through the process?
```

</aside>

**ME:** Here is a prompt that I think could be made into a skill. How would you structure it into  Skills format? Would you need a YAML header, decision tree, scripting, variables from the user, or additional files in a subdirectory?

[Example EPBM - POML format](10%2026%2025%20Claude%20Skills,%20Part%202%20298cfaedc1ba80f38336cd02eaf7e22c/Example%20EPBM%20-%20POML%20format%20298cfaedc1ba80f3b45ced4fd1577613.md)

<aside>

**CLAUDE:**

I'll read the skill-creator guide first to understand the proper format, then help you structure this into a Claude Skill.

Reading the skill-creator guide to understand how to properly structure Claude Skills

Based on the skill-creator guide, here's how I'd structure your Easy Peasy Book Machine as a Claude Skill:

## Recommended Structure

```
easy-peasy-book-machine/
├── SKILL.md
├── assets/
│   ├── character-template.md
│   ├── outline-template.md
│   └── chapter-plan-template.md
└── references/
    └── romance-craft.md  (optional)
```

## SKILL.md Structure

**YAML Frontmatter:**

```
---
name: easy-peasy-book-machine
description: Orchestrates romance novella creation from premise to final chapters with structured workflow. Use when user needs to create or continue a romance novel through systematic steps (premise, characters, outline, chapter planning, drafting, editing). Enforces first-person POV, 2000+ word chapters, and contemporary romance conventions.
---

Body sections:

1. Workflow Overview - Brief explanation of the 7-step process
2. Step Selection Logic - Decision tree for determining current step based on what exists
3. Step Procedures - Each step's specific instructions:
	* Premise Generation
	* Character Development
	* Outline Creation
	* Chapter Planning
	* Chapter Drafting
	* Edit Planning
	* Final Polish
4. Quality Standards - POV rules, word counts, tone requirements
5. Persistence Instructions - How to track progress across steps
```

## Key Adaptations from POML

**No explicit YAML variables** - Skills use natural language instructions, not programmatic inputs. Instead of `<input name="chapter_number">`, you'd write: "Identify the chapter number from user context or ask if unclear."

**Conversational flow** - Rather than enforcing single-step execution programmatically, SKILL.md would say: "Execute only the current step. Ask user which step to perform if unclear from context."

**Template references** - Instead of embedding output format instructions, point to templates: "Use the template in `assets/chapter-plan-template.md` for structure."

**No scripting needed** - This workflow is high-freedom (multiple valid approaches), so text-based instructions work better than deterministic scripts.

Would you like me to write the complete SKILL.md with this structure?

</aside>

**ME:** Yes, please.

<aside>

**CLAUDE:**  

I'll create the complete SKILL.md file for you:

Creating the SKILL.md file for the Easy Peasy Book Machine skill

Copying the SKILL.md file to the outputs directory for user access

```bash
cp /home/claude/SKILL.md /mnt/user-data/outputs/SKILL.md

```

The skill follows Claude Skills format with:

- Proper YAML frontmatter (name + description)
- Seven-step workflow (premise → characters → outline → chapter plan → draft → edit plan → final)
- Step selection logic to determine current position
- Quality standards (first-person POV, 2000+ words, romance focus)
- Output format specifications for each step

No additional files needed - this workflow is high-freedom text-based guidance, so SKILL.md alone is sufficient. To package it as a .skill file, create the directory structure and run the packaging script referenced in the skill-creator guide.

</aside>

[SKILL.md](10%2026%2025%20Claude%20Skills,%20Part%202%20298cfaedc1ba80f38336cd02eaf7e22c/SKILL%20md%20298cfaedc1ba817ca9d3c09434b74531.md)

---