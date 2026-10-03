"""Check post text against Adam's writing rules. Usage: python3 scripts/social/lint.py file.md [more files]
Exit code 1 if anything is found."""
import re, sys
BAN = ["shift", "bottleneck", "friction", "leverag", "delve", "seamless", "holistic", "certainly", "navigat", "landscape",
       "pivotal", "foster", "cultivat", "great question", "sovereign", "hits hard", "real talk", "game changer",
       "let's be honest", "here's the truth", "the truth?", "let that sink in", "cut through the noise", "here's the kicker",
       "most people get this wrong", "none of this is complicated", "in today's", "thanks for reading", "curious", "quietly",
       "habitat for humanity", "crafting a tapestry"]
bad = False
for p in sys.argv[1:]:
    s = open(p, encoding="utf-8").read(); low = s.lower(); hits = []
    for ch, name in [("—", "em dash"), ("–", "en dash")]:
        if ch in s: hits.append(f"{name} x{s.count(ch)}")
    hits += [f"spaced hyphen: {m.group(0)!r}" for m in re.finditer(r"\w+ - \w+", s)]
    hits += [f"banned: {w}" for w in BAN if w in low]
    hits += [f"'real' in: {s[max(0, m.start() - 30):m.end() + 20]!r}" for m in re.finditer(r"\breal\b(?! estate)", low)]
    hits += [f"italic markup: {m.group(0)!r}" for m in re.finditer(r"(?<![\*\w])\*[^\*\n]+\*(?!\*)|(?<![_\w])_[^_\n]+_(?![_\w])", s)]
    print(p, "->", hits or "clean"); bad = bad or bool(hits)
sys.exit(1 if bad else 0)
