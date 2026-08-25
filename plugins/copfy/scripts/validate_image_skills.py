#!/usr/bin/env python3
"""Validate the generated image-command inventory without third-party packages."""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
GENERATOR = Path(__file__).with_name("generate_image_skills.py")


def load_generator():
    spec = importlib.util.spec_from_file_location("copfy_image_skill_generator", GENERATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError("Não foi possível carregar o gerador de skills.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    generator = load_generator()
    commands = generator.parse_commands()
    expected = {command["name"] for command in commands}
    errors: list[str] = []

    generated: set[str] = set()
    descriptions: dict[str, str] = {}
    for skill_file in sorted((PLUGIN_ROOT / "skills").glob("*/SKILL.md")):
        content = skill_file.read_text(encoding="utf-8")
        if generator.GENERATED_MARKER not in content:
            continue
        name = skill_file.parent.name
        generated.add(name)
        match = re.search(r"^name:\s*([a-z0-9-]+)\s*$", content, re.MULTILINE)
        if match is None or match.group(1) != name:
            errors.append(f"Nome inválido no frontmatter: {skill_file}")
        description_match = re.search(r'^description:\s*"(.+)"\s*$', content, re.MULTILINE)
        if description_match is None:
            errors.append(f"Descrição ausente no frontmatter: {skill_file}")
        else:
            descriptions[name] = description_match.group(1)
        example_url = (
            "https://raw.githubusercontent.com/copfybr/copfy-plugin/main/"
            f"plugins/copfy/assets/examples/{name}.jpg"
        )
        if example_url not in content:
            errors.append(f"Exemplo visual não referenciado pela skill: {skill_file}")
        if "grátis, sem autenticação Copfy" not in content:
            errors.append(f"Disponibilidade free tier ausente: {skill_file}")

    missing = sorted(expected - generated)
    extra = sorted(generated - expected)
    if missing:
        errors.append(f"Skills ausentes: {', '.join(missing)}")
    if extra:
        errors.append(f"Skills geradas fora do catálogo: {', '.join(extra)}")
    if len(set(descriptions.values())) != len(expected):
        errors.append("As 148 skills devem ter descrições próprias e não duplicadas.")

    for relative_path, label in (
        ("IMAGE_COMMANDS.md", "catálogo"),
        ("tests/IMAGE_TEST_MATRIX.md", "matriz de testes"),
    ):
        content = (PLUGIN_ROOT / relative_path).read_text(encoding="utf-8")
        rows = len(re.findall(r"^\| `/[a-z0-9-]+` \|", content, re.MULTILINE))
        if rows != len(expected):
            errors.append(f"{label}: esperadas {len(expected)} linhas; encontradas {rows}")

    gallery = (PLUGIN_ROOT / "EXAMPLES.md").read_text(encoding="utf-8")
    gallery_names = set(re.findall(r'alt="Exemplo /([a-z0-9-]+)"', gallery))
    if gallery_names != expected:
        errors.append("A galeria não contém exatamente os 148 comandos esperados.")

    examples_root = PLUGIN_ROOT / "assets" / "examples"
    example_names = {
        path.stem
        for path in examples_root.glob("*.jpg")
        if path.stat().st_size >= 10_000 and path.read_bytes()[:3] == b"\xff\xd8\xff"
    }
    if example_names != expected:
        missing_examples = sorted(expected - example_names)
        extra_examples = sorted(example_names - expected)
        if missing_examples:
            errors.append(f"Exemplos ausentes ou inválidos: {', '.join(missing_examples)}")
        if extra_examples:
            errors.append(f"Exemplos fora do catálogo: {', '.join(extra_examples)}")

    router = (PLUGIN_ROOT / "skills" / "image-commands" / "SKILL.md").read_text(encoding="utf-8")
    for required in (
        "Recomendação automática",
        "compatibilidade física ou conceitual",
        "raw.githubusercontent.com/copfybr/copfy-plugin/main",
        "não recomende engrenagens",
    ):
        if required not in router:
            errors.append(f"Roteador sem regra obrigatória: {required}")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Inventário validado: {len(expected)} comandos, catálogo e matriz de QA.")


if __name__ == "__main__":
    main()
