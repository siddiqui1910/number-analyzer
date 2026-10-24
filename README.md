# Number Analyzer

Takes an integer and reports whether it is even/odd, positive/negative/zero,
divisible by 3 and 5, and whether it is a perfect square.

## How to run
python number-analyzer.py

## What I learned
- Nested conditionals for edge cases (negative numbers, zero)
- Guarding against complex roots: (-9) ** 0.5 returns a complex number
  in Python, so int() on it crashes. Fixed with `if x >= 0:`.
- Floating-point precision limits: `int(root) ** 2 == x` can fail
  for very large perfect squares. Would use math.isqrt() for production.

## Known limitations
- Input must be an integer. Typing `2.5` raises ValueError
  (will fix with try/except later).
