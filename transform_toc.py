import re
import os
import datetime

# Change these filenames as needed.
input_file = "toc exc.md"
output_file = "toc_table.md"
# Remove the fixed document_name; now we assign per row using mapping below.

# New mapping dictionary (expand as needed)
md_mapping = {
    "Sequence Diagram": "sequence-diagram.md",
    "Declaring participant": "declaring-participant.md",
    "Basic Examples": "basic-examples.md",
    # ... add additional mappings as needed ...
}

# Dictionary to hold outline number -> item name for parent lookup.
outline_map = {}

# List to hold table rows.
rows = []

# Function to process a line and yield (outline, title) pairs.
def process_line(line):
    # Remove trailing page numbers (including multi-digit pages)
    cleaned = re.sub(r'\s+\d+\s*$', '', line)
    # Split the line on groups of one or more dots (with optional spaces) that occur at least twice consecutively.
    parts = re.split(r'\s+(?:\.+\s+){2,}', cleaned)
    if not parts:
        return []
    # Extract any outline numbers from the start (match tokens of the form digit(.digit)*)
    outlines = re.findall(r'\d+(?:\.\d+)*', parts[0])
    # Remove the outline numbers from the first part to get the first title segment.
    first_title = re.sub(r'^\s*(?:\d+(?:\.\d+)*\s+)+', '', parts[0]).strip()
    titles = [first_title] if first_title else []
    # Append the remaining parts as additional title segments.
    if len(parts) > 1:
        titles.extend([seg.strip() for seg in parts[1:]])
    # Map each outline with its corresponding title if available.
    pairs = []
    for i, num in enumerate(outlines):
        title = titles[i] if i < len(titles) else ""
        pairs.append( (num, title) )
    return pairs

# new helper function to get all .md files excluding those containing "toc"
def get_md_files(directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return []
    md_files = []
    for fname in os.listdir(directory):
        if fname.endswith(".md") and "toc" not in fname.lower():
            md_files.append(fname)
    return md_files

# Backup existing toc_table.md if it exists
if os.path.exists("toc_table.md"):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_name = f"toc_table.backup-{timestamp}.md"
    os.rename("toc_table.md", backup_name)
    print(f"Renamed toc_table.md to {backup_name}")

# Add a function to check if a string is just an integer
def is_just_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Updated function to check if a line is just a page footer artifact
def is_page_footer(outline_num, item_name, other_columns_empty=True):
    """Check if this is likely a page footer (just a number with empty columns)"""
    try:
        # Check if it's just an integer with no dots
        is_integer = '.' not in outline_num and int(outline_num)
        # Check if item name is empty or just a dot or other minimal punctuation
        minimal_content = not item_name.strip() or item_name.strip() in ['.', ',', '-']
        return is_integer and minimal_content and other_columns_empty
    except ValueError:
        return False

# Function to escape markdown table special characters
def escape_for_md_table(text):
    """Escape pipe characters and other special chars for markdown tables"""
    if not text:
        return ""
    # Escape pipe characters with backslash
    text = text.replace("|", "\\|")
    # Add other special character escaping as needed
    return text

# After importing and before processing lines, add:
assigned_docs = {}
current_dir = os.path.dirname(os.path.abspath(input_file))
available_md_files = get_md_files(current_dir)

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Skip any heading lines (like "Contents")
for line in lines:
    line = line.strip()
    # Only process lines beginning with a number
    if not re.match(r"^\d", line):
        continue
    pairs = process_line(line)
    for outline_num, item_name in pairs:
        # Skip page footer artifacts
        if is_page_footer(outline_num, item_name):
            continue
            
        # Check if item_name starts with the outline_num (with or without space)
        # This handles cases like "10.28 10.28Defining" or "10.28 10.28 Defining"
        outline_pattern = re.escape(outline_num)
        item_name = re.sub(r'^' + outline_pattern + r'\s*' + outline_pattern + r'?', '', item_name).strip()
        
        # Compute parent: if there is a dot, then parent's outline is all but last segment.
        parts = outline_num.split(".")
        if len(parts) == 1:
            parent_outline = ""
            parent_item = ""
        else:
            parent_outline = ".".join(parts[:-1])
            parent_item = outline_map.get(parent_outline, "")
        # Save this entry for later lookup.
        outline_map[outline_num] = item_name

        # Assign document based on top-level mapping and available md files.
        if not parent_outline:  # Top-level row.
            norm_title = item_name.replace(' ', '-').lower() + ".md"
            if norm_title in available_md_files:
                doc = norm_title
            elif item_name in md_mapping:
                doc = md_mapping[item_name]
            else:
                doc = norm_title
            assigned_docs[item_name] = doc
        else:
            # For sub-items, use parent's assigned document.
            doc = assigned_docs.get(parent_item, "")
        
        # Escape special characters for markdown table
        item_name = escape_for_md_table(item_name)
        
        rows.append({
            "OutlineNumber": outline_num,
            "ItemName": item_name,
            "ParentOutlineNumber": parent_outline,
            "ParentItemName": parent_item,
            "DocumentName": doc
        })

# Write the output Markdown table.
with open(output_file, "w", encoding="utf-8") as f:
    header = "| OutlineNumber | ItemName | ParentOutlineNumber | ParentItemName | DocumentName |\n"
    sep = "|---------------|----------|---------------------|----------------|--------------|\n"
    f.write(header)
    f.write(sep)
    for row in rows:
        line = f"| {row['OutlineNumber']} | {row['ItemName']} | {row['ParentOutlineNumber']} | {row['ParentItemName']} | {row['DocumentName']} |\n"
        f.write(line)

print(f"Markdown table output written to {output_file}")

# At the end, list all .md files in the current directory (excluding toc-related files)
current_dir = os.path.dirname(os.path.abspath(input_file))
md_files = get_md_files(current_dir)
print(md_files)
