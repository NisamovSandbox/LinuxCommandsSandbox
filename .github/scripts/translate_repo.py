import os
from concurrent.futures import ThreadPoolExecutor
import deepl
translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))
EXTENSIONS = (".md", ".conf", ".adoc")
def translate_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.strip():
        return
    translated = translator.translate_text(
        content,
        source_lang="ES",
        target_lang="EN-US"
    ).text
    if translated != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(translated)
files_to_translate = []
for root, _, files in os.walk("."):
    if ".git" in root:
        continue
    for file in files:
        if file.endswith(EXTENSIONS):
            files_to_translate.append(os.path.join(root, file))
with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(translate_file, files_to_translate)
