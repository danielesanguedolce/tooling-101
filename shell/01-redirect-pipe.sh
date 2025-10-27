#!/usr/bin/env bash
set -euo pipefail
seq 1 100 | gshuf | head -n 20 > numbers.log
echo "hello" > out.txt
echo "world" >> out.txt
