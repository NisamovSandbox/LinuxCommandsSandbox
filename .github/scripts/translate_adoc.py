#!/usr/bin/env python3
from pathlib import Path
from deep_translator import GoogleTranslator
import sys
import time
import re

if len(sys.argv) != 4:
    print("Uso: translate_adoc.py <SRC_DIR> <DST_DIR> <TARGET_LANG>")
    sys.exit(1)

SRC_ROOT = Path(sys.argv[1])
DST_ROOT = Path(sys.argv[2])
TARGET_LANG = sys.argv[3]
DST_ROOT.mkdir(parents=True, exist_ok=True)
translator = GoogleTranslator(source="es", target=TARGET_LANG)
TECH_PATTERN = re.compile(r"[{}\[\]_*:`<>]")
def should_translate(line: str, target_lang: str) -> bool:
    stripped = line.lstrip()

    if stripped.strip() == "":
        return False

    if stripped.startswith((
        "=", ":", "include::",
        "[", "* ", "- ", "+ ",
        "//", "ifdef::", "ifndef::", "ifeval::"
    )):
        return False

    if stripped.startswith("[") and "]" in stripped:
        return False
    if any(x in stripped for x in (
        "::", "xref:", "link:", "image::", "footnote:"
    )):
        return False
    if any(x in stripped for x in (
        "unordered", "ordered", "disc", "circle", "square"
    )):
        return False
    if TECH_PATTERN.search(stripped):
        return False
    if target_lang.startswith("zh") and len(stripped) < 40:
        return False
    return True

def translate_adoc(text: str) -> str:
    output = []
    in_code_block = False
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        if stripped.startswith("----"):
            in_code_block = not in_code_block
            output.append(line)
            continue
        if in_code_block:
            output.append(line)
            continue
        if should_translate(line, TARGET_LANG):
            try:
                translated = translator.translate(line.rstrip("\n"))
                output.append(translated + "\n")
                time.sleep(0.05)
            except Exception:
                output.append(line)
        else:
            output.append(line)
    return "".join(output)
for src_file in SRC_ROOT.rglob("*.adoc"):
    relative_path = src_file.relative_to(SRC_ROOT)
    dst_file = DST_ROOT / relative_path
    dst_file.parent.mkdir(parents=True, exist_ok=True)

    text = src_file.read_text(encoding="utf-8")
    translated_text = translate_adoc(text)
    dst_file.write_text(translated_text, encoding="utf-8")

    print(f"Traducido ({TARGET_LANG}): {src_file} -> {dst_file}")