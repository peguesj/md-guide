import re
import sys
import os
from difflib import SequenceMatcher

# The list of available .md files in the directory
available_files = ['activity-diagram-beta.md', 'activity-diagram-issues.md', 'activity-diagram-legacy.md', 'ant-task.md', 'api.md', 'archimate-diagram.md', 'ascii-art.md', 'ascii-math.md', 'board-diagram.md', 'bpmn.md', 'brackex.md', 'changes.md', 'chronology-diagram.md', 'class-diagram-issues.md', 'class-diagram.md', 'code-groovy.md', 'code-javascript-asynchronous.md', 'code-javascript-synchronous.md', 'code-php.md', 'color.md', 'command-line.md', 'commons.md', 'component-diagram.md', 'creole.md', 'dark-mode.md', 'dedication.md', 'deployment-diagram-issues.md', 'deployment-diagram.md', 'developers.md', 'ditaa.md', 'doclet.md', 'docutils.md', 'donors.md', 'dot.md', 'doxygen.md', 'ebnf-discussion.md', 'ebnf.md', 'eclipse.md', 'elk.md', 'emacs.md', 'eps.md', 'er-diagram.md', 'external-links.md', 'faq-install.md', 'faq-licence-cheerpj.md', 'faq.md', 'files-diagram.md', 'flow-diagram.md', 'font.md', 'formatting.md', 'ftp.md', 'gantt-diagram.md', 'gfm-support.md', 'git-diagram.md', 'graphviz-dot.md', 'gui.md', 'handwritten.md', 'hcl.md', 'ie-diagram.md', 'index-full.md', 'index.md', 'issues.md', 'javadoc.md', 'jcckit.md', 'jquery.md', 'json-issues.md', 'json.md', 'latex.md', 'layout-engines.md', 'link.md', 'lua.md', 'menu.md', 'mindmap-diagram.md', 'nassi-diagram.md', 'newline.md', 'notes.md', 'nwdiag-issues.md', 'nwdiag.md', 'object-diagram.md', 'openiconic.md', 'oregon-trail.md', 'patreon-support.md', 'pdf.md', 'picoweb.md', 'plantuml-text-encoding.md', 'plantumlshell.md', 'pmwiki.md', 'poll-about-package-and-namespace.md', 'poll-about-wiki-syntax.md', 'preprocessing-gallery.md', 'preprocessing-json.md', 'preprocessing-v2.md', 'preprocessing.md', 'problem-diagram.md', 'professional.md', 'pte.md', 'regex-old.md', 'regex.md', 'salt.md', 'security.md', 'sequence-diagram.md', 'server.md', 'skinparam.md', 'smetana02.md', 'sources.md', 'spec-multiline.md', 'sprite.md', 'start.md', 'starting.md', 'state-diagram-issues.md', 'state-diagram.md', 'statistics-report.md', 'stdlib.md', 'steve.md', 'story-board.md', 'style-evolution-history.md', 'style-evolution.md', 'style.md', 'sub-diagram.md', 'sudoku.md', 'svek.md', 'svg.md', 'syntax-asciidoc.md', 'syntax-dokuwiki.md', 'syntax-markdown.md', 'teoz.md', 'text-encoding.md', 'theme-gallery.md', 'theme.md', 'timing-diagram-issues.md', 'timing-diagram.md', 'undocumented.md', 'unicode.md', 'url-authentication.md', 'url-basicauth.md', 'url-oauth.md', 'url-tokenauth.md', 'use-case-diagram.md', 'using-a-citation-manager.md', 'versioning-scheme.md', 'vizjs.md', 'wbs-diagram.md', 'what-is-a-software-modeling-tool.md', 'why-sequence-diagram.md', 'wire-diagram.md', 'word.md', 'xearth.md', 'xmi.md', 'yaml.md']

# Known top-level diagram types for mapping
diagram_mapping = {
    "Sequence Diagram": "sequence-diagram.md",
    "Use Case Diagram": "use-case-diagram.md",
    "Class Diagram": "class-diagram.md",
    "Object Diagram": "object-diagram.md",
    "Activity Diagram (legacy)": "activity-diagram-legacy.md",
    "Activity Diagram (New Syntax)": "activity-diagram-beta.md",
    "Component Diagram": "component-diagram.md",
    "Deployment Diagram": "deployment-diagram.md",
    "State Diagram": "state-diagram.md",
    "Timing Diagram": "timing-diagram.md",
    "Display JSON Data": "json.md",
    "Display YAML Data": "yaml.md",
    "Network Diagram with nwdiag": "nwdiag.md",
    "Salt (Wireframe)": "salt.md",
    "ArchiMate Diagram": "archimate-diagram.md",
    "Gantt Chart": "gantt-diagram.md",
    "MindMap": "mindmap-diagram.md",
    "Work Breakdown Structure (WBS)": "wbs-diagram.md",
    "Maths": "ascii-math.md",
    "Information Engineering Diagrams": "ie-diagram.md",
    "Common Commands in PlantUML": "commons.md",
    "Creole": "creole.md",
    "Defining and using sprites": "sprite.md",
    "Skinparam command": "skinparam.md",
    "Preprocessing": "preprocessing.md",
    "Unicode": "unicode.md",
    "PlantUML Standard Library": "stdlib.md"
}

def similarity(a, b):
    """Calculate text similarity between two strings."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def normalize_name(name):
    """Convert a title to a kebab-case filename."""
    # Remove special characters
    name = re.sub(r'[^\w\s]', '', name.lower())
    # Replace spaces with hyphens
    name = name.replace(' ', '-')
    return name + ".md"

def find_best_match(item_name, parent_file=None, outline_num=""):
    """Find the best matching file for a given item name."""
    
    # Skip purely numeric items (page numbers)
    if re.match(r'^\d+$', item_name.strip()):
        return None, 0
    
    # Check if item name is in our known mapping
    if item_name in diagram_mapping:
        return diagram_mapping[item_name], 1.0
    
    # Try normalized name
    normalized = normalize_name(item_name)
    if normalized in available_files:
        return normalized, 0.9
    
    # For sub-sections, usually use the parent file
    if parent_file and parent_file in available_files:
        return parent_file, 0.8
    
    # Try to find a close match based on text similarity
    best_match = None
    best_score = 0
    
    # Extract keywords from item name
    keywords = re.findall(r'\b\w{3,}\b', item_name.lower())
    
    for file in available_files:
        score = 0
        # Check for direct word matches in the filename
        for keyword in keywords:
            if keyword in file.lower():
                score += 0.2
        
        # Add similarity score
        score += similarity(item_name, file.replace('-', ' ').replace('.md', '')) * 0.5
        
        if score > best_score:
            best_score = score
            best_match = file
    
    return best_match, best_score

def escape_for_md_table(text):
    """Escape pipe characters and other special chars for markdown tables"""
    if not text:
        return ""
    # Escape pipe characters with backslash
    text = text.replace("|", "\\|")
    # Add other special character escaping as needed
    return text

def process_table(input_file, output_file):
    """Process the TOC table and update file mappings."""
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # First two lines are the header rows
    header_lines = lines[:2]
    content_lines = lines[2:]
    
    # Parse table to extract info
    items = []
    
    for line in content_lines:
        if '|' not in line:
            continue
            
        parts = line.split('|')
        if len(parts) < 6:
            continue
            
        outline_num = parts[1].strip()
        item_name = parts[2].strip()
        parent_outline = parts[3].strip()
        parent_name = parts[4].strip()
        current_doc = parts[5].strip()
        
        # Skip rows that are likely page footer artifacts
        if outline_num and not item_name and not parent_outline and not parent_name and not current_doc:
            if '.' not in outline_num:  # Just an integer
                try:
                    int(outline_num)
                    continue  # Skip this row
                except ValueError:
                    pass  # Not a page number, keep processing
        
        items.append({
            'outline_num': outline_num,
            'item_name': item_name,
            'parent_outline': parent_outline,
            'parent_name': parent_name,
            'current_doc': current_doc,
            'line': line
        })
    
    # Build parent-child relationships
    parent_map = {}
    for item in items:
        if item['parent_outline']:
            for parent in items:
                if parent['outline_num'] == item['parent_outline']:
                    parent_map[item['outline_num']] = parent
                    break
    
    # Track matched files and statistics
    matched_files = set()
    matched_items_count = 0
    unmatched_items_count = 0
    low_confidence_threshold = 0.3
    
    # First pass: Set mappings for top-level items
    for item in items:
        if not item['parent_outline']:  # Top-level item
            best_match, confidence = find_best_match(item['item_name'])
            item['new_doc'] = best_match
            item['confidence'] = confidence
            
            if best_match and confidence > low_confidence_threshold:
                matched_items_count += 1
                matched_files.add(best_match)
            else:
                unmatched_items_count += 1
                
            print(f"Top-level: {item['outline_num']} {item['item_name']} → {best_match} (confidence: {confidence:.2f})")
    
    # Second pass: Set mappings for child items based on their parents
    for item in items:
        if item['parent_outline']:
            parent = parent_map.get(item['outline_num'])
            parent_doc = parent['new_doc'] if parent else None
            best_match, confidence = find_best_match(item['item_name'], parent_doc, item['outline_num'])
            item['new_doc'] = best_match
            item['confidence'] = confidence
            
            if best_match and confidence > low_confidence_threshold:
                matched_items_count += 1
                matched_files.add(best_match)
            else:
                unmatched_items_count += 1
                
            parent_info = f" (parent: {parent['item_name']} → {parent_doc})" if parent else ""
            print(f"Child: {item['outline_num']} {item['item_name']} → {best_match} (confidence: {confidence:.2f}){parent_info}")
    
    # Generate updated table
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.writelines(header_lines)
        
        # Write updated content with proper escaping
        for item in items:
            parts = item['line'].split('|')
            if len(parts) < 6:
                f.write(item['line'])
                continue
                
            # Escape items if needed
            item_name = escape_for_md_table(item['item_name'])
            parent_name = escape_for_md_table(item['parent_name'])
            
            # Replace values in parts
            parts[2] = f" {item_name} "
            parts[4] = f" {parent_name} "
            parts[5] = f" {item['new_doc'] or ''} "
            f.write('|'.join(parts))
    
    # Calculate remaining unmatched files
    unmatched_files = set(available_files) - matched_files
    
    # Print statistics
    print(f"\nMatching Statistics:")
    print(f"- Matched items: {matched_items_count}")
    print(f"- Unmatched or low confidence items: {unmatched_items_count}")
    print(f"- Unique files matched: {len(matched_files)}")
    print(f"- Remaining unmatched files: {len(unmatched_files)}")

if __name__ == "__main__":
    input_file = "toc_table.md"
    output_file = "toc_table_updated.md"
    
    # Backup the original file
    if os.path.exists(input_file):
        process_table(input_file, output_file)
        print(f"\nUpdated TOC table written to {output_file}")
        print("Review the file and if satisfied, rename it to toc_table.md")
    else:
        print(f"Error: Input file {input_file} not found")
