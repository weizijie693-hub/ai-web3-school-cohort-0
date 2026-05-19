#!/usr/bin/env python3
"""
AI x Web3 Concept Explainer

Usage:
  python cli_concept_explainer.py list              # list all concepts
  python cli_concept_explainer.py explain <keyword>  # look up a concept
  python cli_concept_explainer.py random             # random concept
  python cli_concept_explainer.py quiz               # interactive quiz (5 questions)
  python cli_concept_explainer.py stats              # show learning stats
"""

import json
import random
import sys
from pathlib import Path

DATA_FILE = Path(__file__).parent / "concepts.json"


def load_concepts():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def print_header(text):
    print("\n" + "=" * 60)
    print("  " + text)
    print("=" * 60)


def print_concept(key, c):
    print()
    print("== {}  ({})".format(c["name"], c["name_en"]))
    print("  Category: " + c.get("cat", "general"))
    print("-" * 50)
    print("\n>> One-Line Summary")
    print("   {}".format(c["one_line"]))
    print("\n>> Example")
    print("   {}".format(c["example"]))
    print("\n>> Misconception")
    print("   {}".format(c["misconception"]))
    print()


def cmd_list():
    concepts = load_concepts()
    print_header("AI x Web3 Concept Library ({} concepts)".format(len(concepts)))
    cats = {"ai": "AI", "web3": "Web3", "bridge": "AI x Web3"}
    for cat_key, cat_label in cats.items():
        items = [(k, c) for k, c in concepts.items() if c.get("cat") == cat_key]
        if items:
            print("\n  [{}]".format(cat_label))
            for key, c in sorted(items):
                print("    {:<22s} {}".format(key, c["name"]))
    print("\n  Usage: python cli_concept_explainer.py explain <keyword>")


def cmd_explain(keywords):
    concepts = load_concepts()
    keyword = " ".join(keywords).lower()
    if keyword in concepts:
        print_concept(keyword, concepts[keyword])
        return
    matches = []
    for key, c in concepts.items():
        if keyword in key or keyword in c["name"] or keyword in c["name_en"].lower():
            matches.append((key, c))
    if not matches:
        print("\n[ERROR] Concept not found: '{}'".format(keyword))
        print("    Available: python cli_concept_explainer.py list")
        return
    if len(matches) == 1:
        print_concept(matches[0][0], matches[0][1])
    else:
        print("\n[INFO] Multiple matches:")
        for key, c in matches:
            print("  {:<22s} {}".format(key, c["name"]))
        print("\n    Use an exact keyword: python cli_concept_explainer.py explain <keyword>")


def cmd_random():
    concepts = load_concepts()
    key = random.choice(list(concepts.keys()))
    print("\n[RANDOM] {}".format(concepts[key]["name"]))
    print_concept(key, concepts[key])


def cmd_quiz():
    concepts = load_concepts()
    items = list(concepts.items())
    random.shuffle(items)

    score = 0
    total = min(5, len(items))

    print_header("AI x Web3 Quiz ({} questions)".format(total))
    print("See the concept name -> pick the matching description type:")
    print("  [1] One-Line Summary")
    print("  [2] Example")
    print("  [3] Misconception")
    print("  [0] Skip\n")

    for i, (key, c) in enumerate(items[:total], 1):
        q_type = random.choice(["one_line", "example", "misconception"])
        type_label = {"one_line": "One-Line Summary", "example": "Example", "misconception": "Misconception"}[q_type]
        text = c[q_type][:100] + "..."

        print("\n--- Q{} / {} ---".format(i, total))
        print("Concept: {}".format(c["name"]))
        print("Which is its '{}'?".format(type_label))
        print("  " + text)

        wrong = random.choice([x for x in items if x[0] != key])
        options = [("1", c[q_type], True), ("2", wrong[1][q_type], False)]
        random.shuffle(options)
        for opt_label, opt_text, _ in options:
            preview = (opt_text[:80] + "...") if len(opt_text) > 80 else opt_text
            print("  [{}] {}".format(opt_label, preview))

        answer = input("\nYour choice (1/2, or 0 to skip): ").strip()
        if answer == "0":
            print("  Correct answer: {}".format(c[q_type][:120]))
            continue
        if answer not in ("1", "2"):
            print("  Invalid. Correct answer: {}".format(c[q_type][:120]))
            continue
        selected = next((x for x in options if x[0] == answer), None)
        if selected and selected[2]:
            print("  CORRECT!")
            score += 1
        else:
            print("  WRONG. Correct answer:")
            print("  {}".format(c[q_type][:120]))

    print("\n{}".format("=" * 40))
    print("  Score: {}/{}".format(score, total))
    print("{}".format("=" * 40))


def cmd_stats():
    concepts = load_concepts()
    total = len(concepts)
    cats = {}
    for c in concepts.values():
        cat = c.get("cat", "general")
        cats[cat] = cats.get(cat, 0) + 1
    print_header("Learning Stats")
    print("  Total concepts: {}".format(total))
    for cat, count in sorted(cats.items()):
        print("    {}: {}".format(cat, count))
    print()


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        print("Commands: list, explain <keyword>, random, quiz, stats")
        return

    cmd = sys.argv[1]
    if cmd == "list":
        cmd_list()
    elif cmd == "explain" and len(sys.argv) > 2:
        cmd_explain(sys.argv[2:])
    elif cmd == "random":
        cmd_random()
    elif cmd == "quiz":
        cmd_quiz()
    elif cmd == "stats":
        cmd_stats()
    else:
        print("Unknown command: {}".format(cmd))
        print(__doc__)


if __name__ == "__main__":
    main()
