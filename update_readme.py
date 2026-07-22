import os
import re

easy_dir = "easy"
problems_dir = "Problems"

# Count solved problems
solved_count = len([f for f in os.listdir(easy_dir) if f.endswith(".py")])

# Build list from Problems folder, sorted alphabetically
files = sorted(os.listdir(problems_dir))
lines = []
for i, f in enumerate(files, start=1):
    name = f.replace(".md", "").split("-", 1)[-1].replace("-", " ")
    lines.append(f"{i}. [{name}](Problems/{f})")

problem_list = "\n".join(lines)

with open("README.md", "r") as file:
    content = file.read()

content = re.sub(r"- ✅ Solved: \d+ / 75", f"- ✅ Solved: {solved_count} / 75", content)

with open("README.md", "w") as file:
    file.write(content)