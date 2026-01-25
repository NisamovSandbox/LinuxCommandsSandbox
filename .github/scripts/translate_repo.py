#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from transformers import MarianMTModel, MarianTokenizer

# Modelo español a inglés de Hugging Face
MODEL_NAME = "Helsinki-NLP/opus-mt-es-en"
tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
model = MarianMTModel.from_pretrained(MODEL_NAME)

def translate_text(text: str) -> str:
    batch = tokenizer([text], return_tensors="pt", truncation=True, padding=True)
    generated = model.generate(**batch)
    return tokenizer.decode(generated[0], skip_special_tokens=True)

def extract_code_blocks(text: str) -> (str, dict):
    """
    Sustituye bloques de código por placeholders para protegerlos.
    Devuelve el texto modificado y un diccionario {placeholder: contenido}.
    """
    code_blocks = {}

    pattern_md = r"```.*?```"
    for i, match in enumerate(re.findall(pattern_md, text, flags=re.DOTALL)):
        placeholder = f"__CODE_BLOCK_MD_{i}__"
        code_blocks[placeholder] = match
        text = text.replace(match, placeholder)
    
    pattern_tex = r"\\begin\{.*?\}.*?\\end\{.*?\}"
    for i, match in enumerate(re.findall(pattern_tex, text, flags=re.DOTALL)):
        placeholder = f"__CODE_BLOCK_TEX_{i}__"
        code_blocks[placeholder] = match
        text = text.replace(match, placeholder)
    
    pattern_adoc = r"(\[source.*?\]\n----.*?----)"
    for i, match in enumerate(re.findall(pattern_adoc, text, flags=re.DOTALL)):
        placeholder = f"__CODE_BLOCK_ADOC_{i}__"
        code_blocks[placeholder] = match
        text = text.replace(match, placeholder)
    
    return text, code_blocks

def restore_code_blocks(text: str, code_blocks: dict) -> str:
    for placeholder, code in code_blocks.items():
        text = text.replace(placeholder, code)
    return text

def translate_preserving_indent(text: str) -> str:
    lines = text.split("\n")
    translated_lines = []
    for line in lines:
        if not line.strip():
            translated_lines.append(line)
            continue
        leading_spaces = len(line) - len(line.lstrip(' '))
        translated = translate_text(line.strip())
        translated_lines.append(' ' * leading_spaces + translated)
    return "\n".join(translated_lines)

def translate_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    content, code_blocks = extract_code_blocks(content)
    translated = translate_preserving_indent(content)
    translated = restore_code_blocks(translated, code_blocks)

    with open(path, "w", encoding="utf-8") as f:
        f.write(translated)
    print(f"[OK] Traducido {path}")

def main():
    extensions = (".md", ".tex", ".adoc")
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(extensions):
                translate_file(os.path.join(root, file))

if __name__ == "__main__":
    main()