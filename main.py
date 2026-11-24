"""One-Line Roast: The Gadget You Use Every Day.

One original roast, a single line of at most 200 characters, aimed at a
gadget used every day: a phone whose battery keeps office hours, dies
before dinner, and still finds the energy to ask for a rating.
"""

import os

LINE = (
    "My phone's battery has a union contract: 100% at nine, 3% by lunch, "
    "dead before dinner \u2014 yet it still has the nerve to ask me to "
    "rate it."
)

chars = len(LINE)
if chars < 1 or chars > 200:
    raise SystemExit(f"entry line is {chars} characters, outside the 1-200 gate")
if not LINE.strip():
    raise SystemExit("entry line is blank")
if "\n" in LINE or "\r" in LINE:
    raise SystemExit("entry line must be a single line")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
# The grader collects /output as another user, so the file must be
# world-readable: a default mkstemp-style 0600 mode fails "not readable".
os.chmod(path, 0o644)
print(LINE)
print(f"({chars} characters)")
