#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

# Configuración
ROOT_DIR = Path(".")
OUTPUT_DIR = ROOT_DIR / "output"
EXCLUDE_DIRS = [ROOT_DIR / ".github"]
OUTPUT_DIR.mkdir(exist_ok=True)

# Comando base de Pandoc con LuaLaTeX
PANDOC_BASE_CMD = [
    "pandoc",
    "--pdf-engine=lualatex",
    "-V", "lang=es-ES",
    "-V", "mainfont=Noto Sans",
    "-V", "sansfont=Noto Sans",
    "-V", "monofont=Noto Sans Mono",
    "-V", "mainfontoptions=Renderer=Harfbuzz",
    "-V", "monofontoptions=Renderer=Harfbuzz",
    "-V", "geometry:margin=1.5cm",
    "-V", "fontsize=11pt",
    "-V", "colorlinks=true"
]

def gather_files(directory: Path):
    """Recoge los archivos en orden: README.md -> otros .md -> .yml/.yaml -> .conf"""
    readme = directory / "README.md"
    files = []

    # README.md primero
    if readme.exists():
        files.append(readme)

    exts_order = [".md", ".yml", ".yaml", ".conf"]
    for ext in exts_order:
        for f in sorted(directory.glob(f"*{ext}")):
            if f.name != "README.md":
                files.append(f)

    # Subdirectorios
    for subdir in sorted([d for d in directory.iterdir() if d.is_dir() and d not in EXCLUDE_DIRS]):
        files.extend(gather_files(subdir))

    return files

def generate_pdf(directory: Path):
    """Genera el PDF de un directorio, cada archivo en hoja nueva y sin nombres de archivo"""
    files = gather_files(directory)
    if not files:
        return

    output_file = OUTPUT_DIR / f"{directory.name.upper()}.pdf"

    # Crear archivo temporal concatenando Markdown
    temp_md = OUTPUT_DIR / f"{directory.name}_temp.md"
    with open(temp_md, "w", encoding="utf-8") as out_md:
        for i, f in enumerate(files):
            content = f.read_text(encoding="utf-8")

            # Mantener bloques de código para .yaml/.yml/.conf
            if f.suffix in [".yaml", ".yml", ".conf"]:
                out_md.write("```\n")
                out_md.write(content)
                out_md.write("\n```\n")
            else:
                out_md.write(content)
                out_md.write("\n\n")
            
            # Salto de página salvo que sea el último archivo
            if i < len(files) - 1:
                out_md.write("\n\\newpage\n")

    # Comprobar si es commands.md para orientación horizontal
    if any(f.name == "commands.md" for f in files):
        cmd = PANDOC_BASE_CMD + [
            str(temp_md),
            "-V", "documentclass=article",
            "-V", "classoption=landscape",
            "-o", str(OUTPUT_DIR / f"{directory.name.upper()}_COMMANDS.pdf")
        ]
        subprocess.run(cmd, check=True)

    # Generar PDF principal
    cmd = PANDOC_BASE_CMD + [
        str(temp_md),
        "-V", "documentclass=article",
        "-V", "classoption=portrait",
        "-o", str(output_file)
    ]
    subprocess.run(cmd, check=True)

    temp_md.unlink()

def main():
    for item in ROOT_DIR.iterdir():
        if item.is_dir() and item not in EXCLUDE_DIRS:
            generate_pdf(item)

if __name__ == "__main__":
    main()
