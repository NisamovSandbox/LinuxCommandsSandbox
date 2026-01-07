#!/usr/bin/env python3
import re
from pathlib import Path
EXCLUDED_DIRS={'.git','.github','__pycache__'}
EXCLUDED_FILES={'README.md','CONTRIBUTING.md','INFO.md','KEYWORD.md','LICENSE'}
ROOT=Path('.')
def write_readme(path:Path,lines):
    readme=path/'README.md'
    start='<!-- AUTO-GENERATED-INDEX:START -->'
    end='<!-- AUTO-GENERATED-INDEX:END -->'
    tree_md='\n'.join(lines)
    new_block=f"{start}\n{tree_md}\n{end}"
    if readme.exists():
        content=readme.read_text(encoding='utf-8')
        if start in content and end in content:
            pattern=re.compile(re.escape(start)+'.*?'+re.escape(end),re.DOTALL)
            updated=pattern.sub(new_block,content)
        else:
            updated=content.rstrip()+"\n\n"+new_block
    else:
        updated=f"# {path.name}\n\n{new_block}"
    readme.write_text(updated,encoding='utf-8')
def generate_root_readme(root:Path):
    lines=[
        f"- [{d.name}](/{d.as_posix()})"
        for d in sorted(root.iterdir())
        if d.is_dir() and d.name not in EXCLUDED_DIRS
    ]
    write_readme(root,lines)
def generate_section_readme(section:Path):
    lines=[]
    for d in sorted(section.iterdir()):
        if not d.is_dir() or d.name in EXCLUDED_DIRS:
            continue
        lines.append(f"- [{d.name}](/{d.as_posix()})")
        for f in sorted(d.rglob('*.md')):
            if f.name in EXCLUDED_FILES:
                continue
            rel=f.relative_to(section).as_posix()
            lines.append(f"  - [{rel}](/{f.as_posix()})")
    write_readme(section,lines)
if __name__=='__main__':
    generate_root_readme(ROOT)
    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and d.name not in EXCLUDED_DIRS:
            generate_section_readme(d)
