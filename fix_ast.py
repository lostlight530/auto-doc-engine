with open('core/ast_engine.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if "def to_dict(self) -> dict:" in line:
        if lines[i+1].strip() == "def to_dict(self) -> dict:":
            continue # skip the duplicate one
    new_lines.append(line)

with open('core/ast_engine.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
