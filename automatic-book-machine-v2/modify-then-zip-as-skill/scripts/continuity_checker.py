#!/usr/bin/env python3
"""
Continuity Checker for Automatic Book Machine
Tracks character names and identifies potential inconsistencies across chapters.
"""

import re
import sys
from pathlib import Path
from collections import defaultdict


def extract_character_names(content):
    """Extract character names from character profiles section."""
    characters = []
    
    # Find character profiles section
    profile_match = re.search(r'\[character profiles\](.*?)\[/character profiles\]', 
                             content, re.DOTALL | re.IGNORECASE)
    
    if profile_match:
        profiles = profile_match.group(1)
        # Extract character names (look for "CHARACTER N: Name" pattern)
        for match in re.finditer(r'CHARACTER \d+:\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', profiles):
            characters.append(match.group(1))
    
    return characters


def find_character_mentions(content, character_name):
    """Find all mentions of a character across chapters."""
    mentions = defaultdict(list)
    
    # Check each chapter
    for chapter_match in re.finditer(r'\[chapter (\d+) (?:draft|final)\](.*?)\[/chapter \1 (?:draft|final)\]', 
                                     content, re.DOTALL | re.IGNORECASE):
        chapter_num = int(chapter_match.group(1))
        chapter_text = chapter_match.group(2)
        
        # Count mentions in this chapter
        pattern = r'\b' + re.escape(character_name) + r'\b'
        found = re.findall(pattern, chapter_text, re.IGNORECASE)
        if found:
            mentions[chapter_num] = len(found)
    
    return mentions


def check_name_variants(content, character_names):
    """Check for potential misspellings or name variants."""
    issues = []
    
    # Look for similar names that might be typos
    for character in character_names:
        # Create pattern for close matches (one letter different)
        base_name = character.split()[0]  # First name only
        
        # Find potential variants in text
        all_text = re.sub(r'\[character profiles\].*?\[/character profiles\]', '', content, flags=re.DOTALL)
        
        # Look for capitalized words similar to character name
        words = re.findall(r'\b[A-Z][a-z]+\b', all_text)
        
        for word in set(words):
            if word != base_name and len(word) == len(base_name):
                # Check if it's one letter different
                differences = sum(1 for a, b in zip(word, base_name) if a != b)
                if differences == 1:
                    issues.append(f"Potential misspelling: '{word}' might be '{base_name}'")
    
    return issues


def main():
    if len(sys.argv) < 2:
        print("Usage: python continuity_checker.py <manuscript_file>")
        sys.exit(1)
    
    filepath = Path(sys.argv[1])
    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    
    content = filepath.read_text(encoding='utf-8')
    
    print("=" * 60)
    print("AUTOMATIC BOOK MACHINE - CONTINUITY CHECK REPORT")
    print("=" * 60)
    
    # Extract character names
    characters = extract_character_names(content)
    
    if not characters:
        print("\n⚠ No character profiles found")
        sys.exit(0)
    
    print(f"\nCHARACTERS IDENTIFIED: {len(characters)}")
    for char in characters:
        print(f"  • {char}")
    
    # Track mentions per chapter
    print("\nCHARACTER APPEARANCES BY CHAPTER:")
    for character in characters:
        mentions = find_character_mentions(content, character)
        if mentions:
            chapters = sorted(mentions.keys())
            print(f"\n  {character}:")
            for chapter_num in chapters:
                print(f"    Chapter {chapter_num}: {mentions[chapter_num]} mentions")
        else:
            print(f"\n  {character}: ⚠ No appearances found in chapters")
    
    # Check for potential name issues
    print("\nNAME CONSISTENCY CHECK:")
    issues = check_name_variants(content, characters)
    if issues:
        for issue in issues:
            print(f"  ⚠ {issue}")
    else:
        print("  ✓ No obvious name inconsistencies detected")
    
    print("=" * 60)


if __name__ == "__main__":
    main()
