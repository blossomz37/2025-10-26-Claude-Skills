#!/usr/bin/env python3
"""
Tag Validator for Automatic Book Machine
Ensures all square bracket tags are properly opened and closed.
"""

import re
import sys
from pathlib import Path
from collections import defaultdict


def validate_tags(content):
    """Validate that all tags are properly opened and closed."""
    errors = []
    warnings = []
    
    # Find all opening and closing tags
    opening_tags = re.findall(r'\[([^\]/]+)\]', content)
    closing_tags = re.findall(r'\[/([^\]]+)\]', content)
    
    # Track tag pairs
    tag_stack = []
    tag_positions = []
    
    # Parse through content to match tags
    for match in re.finditer(r'\[/?([^\]]+)\]', content):
        full_tag = match.group(0)
        tag_name = match.group(1)
        position = match.start()
        
        if full_tag.startswith('[/'):
            # Closing tag
            if not tag_stack:
                errors.append(f"Closing tag without opening: {full_tag} at position {position}")
            elif tag_stack[-1][1] == tag_name:
                tag_stack.pop()
            else:
                errors.append(f"Mismatched closing tag: expected [/{tag_stack[-1][1]}] but found {full_tag} at position {position}")
        else:
            # Opening tag
            tag_stack.append((position, tag_name, full_tag))
    
    # Check for unclosed tags
    for position, tag_name, full_tag in tag_stack:
        errors.append(f"Unclosed tag: {full_tag} at position {position}")
    
    # Count occurrences of each tag type
    tag_counts = defaultdict(int)
    for tag in opening_tags:
        tag_counts[tag] += 1
    
    return errors, warnings, tag_counts


def main():
    if len(sys.argv) < 2:
        print("Usage: python tag_validator.py <manuscript_file>")
        sys.exit(1)
    
    filepath = Path(sys.argv[1])
    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    
    content = filepath.read_text(encoding='utf-8')
    errors, warnings, tag_counts = validate_tags(content)
    
    print("=" * 60)
    print("AUTOMATIC BOOK MACHINE - TAG VALIDATION REPORT")
    print("=" * 60)
    
    if errors:
        print("\nERRORS:")
        for error in errors:
            print(f"  ✗ {error}")
    else:
        print("\n✓ All tags are properly formatted and closed")
    
    if warnings:
        print("\nWARNINGS:")
        for warning in warnings:
            print(f"  ⚠ {warning}")
    
    print("\nTAG SUMMARY:")
    for tag_name, count in sorted(tag_counts.items()):
        print(f"  {tag_name}: {count}")
    
    print("=" * 60)
    
    # Exit with error code if there are errors
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
