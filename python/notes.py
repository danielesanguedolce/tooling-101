#!/usr/bin/env python3
import sys
from pathlib import Path

DB = Path("notes.txt")

def add(note: str):
    with DB.open("a", encoding="utf-8") as f:
        f.write(note.strip() + "\n")

def list_notes():
    if not DB.exists():
        print("(nessuna nota)"); return
    for i, line in enumerate(DB.read_text(encoding="utf-8").splitlines(), 1):
        print(f"{i}. {line}")

def delete(idx: int):
    if not DB.exists():
        print("Nessuna nota da cancellare"); return
    lines = DB.read_text(encoding="utf-8").splitlines()
    if 1 <= idx <= len(lines):
        del lines[idx-1]
        DB.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
        print(f"Nota {idx} eliminata")
    else:
        print("Indice non valido")

def search(pat: str):
    if not DB.exists():
        print("(nessuna nota)"); return
    pat = pat.lower()
    found = False
    for i, line in enumerate(DB.read_text(encoding="utf-8").splitlines(), 1):
        if pat in line.lower():
            print(f"{i}. {line}")
            found = True
    if not found:
        print("(nessun risultato)")

def help():
    print("Uso:")
    print('  notes.py add "testo"')
    print("  notes.py list")
    print("  notes.py del <indice>")
    print("  notes.py search <pattern>")

if __name__ == "__main__":
    if len(sys.argv) < 2: help(); sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "add":
        if len(sys.argv) < 3: help(); sys.exit(1)
        add(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_notes()
    elif cmd == "del":
        if len(sys.argv) != 3 or not sys.argv[2].isdigit(): help(); sys.exit(1)
        delete(int(sys.argv[2]))
    elif cmd == "search":
        if len(sys.argv) != 3: help(); sys.exit(1)
        search(sys.argv[2])
    else:
        help()
