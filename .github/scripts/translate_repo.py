import os
from concurrent.futures import ThreadPoolExecutor
import deepl
translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))
EXTENSIONS = (".md", ".conf", ".adoc")
def translate_file(input_path):
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()
    translated_text = translator.translate_text(content, target_lang="EN-US").text
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(translated_text)
file_paths = []
for root, _, files in os.walk("."):
    if ".git" in root:
        continue
    for file in files:
        if file.endswith(EXTENSIONS):
            file_paths.append(os.path.join(root, file))
with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(translate_file, file_paths)
