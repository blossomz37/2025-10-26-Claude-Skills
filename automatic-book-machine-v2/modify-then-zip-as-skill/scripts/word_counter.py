#!/usr/bin/env python3
"""
Word Counter for Automatic Book Machine
Counts words in tagged sections to track progress and verify minimum requirements.
"""

import re
import sys
from pathlib import Path


def count_words_in_text(text):
    """Count words in a text string."""
    words = re.findall(r'\b\w+\b', text)
    return len(words)


def extract_tagged_sections(content, tag_name):
    """Extract all content between [tag_name] and [/tag_name] markers."""
    pattern = rf'\[{re.escape(tag_name)}\](.*?)\[/{re.escape(tag_name)}\]'
    matches = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
    return matches


def count_chapter_words(content):
    """Count words in all chapter drafts and finals."""
    stats = {
        'drafts': {},
        'finals': {},
        'total_draft_words': 0,
        'total_final_words': 0
    }
    
    # Find all chapter drafts
    for match in re.finditer(r'\[chapter (\d+) draft\](.*?)\[/chapter \1 draft\]', 
                             content, re.DOTALL | re.IGNORECASE):
        chapter_num = int(match.group(1))
        chapter_text = match.group(2)
        word_count = count_words_in_text(chapter_text)
        stats['drafts'][chapter_num] = word_count
        stats['total_draft_words'] += word_count
    
    # Find all chapter finals
    for match in re.finditer(r'\[chapter (\d+) final\](.*?)\[/chapter \1 final\]', 
                             content, re.DOTALL | re.IGNORECASE):
        chapter_num = int(match.group(1))
        chapter_text = match.group(2)
        word_count = count_words_in_text(chapter_text)
        stats['finals'][chapter_num] = word_count
        stats['total_final_words'] += word_count
    
    return stats


def main():
    if len(sys.argv) < 2:
        print("Usage: python word_counter.py <manuscript_file>")
        sys.exit(1)
    
    filepath = Path(sys.argv[1])
    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    
    content = filepath.read_text(encoding='utf-8')
    stats = count_chapter_words(content)
    
    print("=" * 60)
    print("AUTOMATIC BOOK MACHINE - WORD COUNT REPORT")
    print("=" * 60)
    
    # Report on drafts
    if stats['drafts']:
        print("\nCHAPTER DRAFTS:")
        for chapter_num in sorted(stats['drafts'].keys()):
            word_count = stats['drafts'][chapter_num]
            status = "✓" if word_count >= 1500 else "✗ (below minimum)"
            print(f"  Chapter {chapter_num}: {word_count:,} words {status}")
        print(f"  Total: {stats['total_draft_words']:,} words")
    
    # Report on finals
    if stats['finals']:
        print("\nCHAPTER FINALS:")
        for chapter_num in sorted(stats['finals'].keys()):
            word_count = stats['finals'][chapter_num]
            status = "✓" if word_count >= 1500 else "✗ (below minimum)"
            print(f"  Chapter {chapter_num}: {word_count:,} words {status}")
        print(f"  Total: {stats['total_final_words']:,} words")
    
    # Overall statistics
    total_chapters = max(len(stats['drafts']), len(stats['finals']))
    print(f"\nOVERALL:")
    print(f"  Total chapters: {total_chapters}")
    print(f"  Manuscript word count: {stats['total_final_words']:,} words")
    
    print("=" * 60)


if __name__ == "__main__":
    main()
