---
adapter: generic
max_iters: 2
score_threshold: 0.85
no_improvement_for: 3
---

# Primes up to N

Write a Python module `primes.py` that exposes:

- `primes_below(n: int) -> list[int]` — return all primes strictly less
  than `n`, in ascending order. Use the Sieve of Eratosthenes for `n` up
  to 1,000,000 in well under a second.
- `is_prime(n: int) -> bool` — return whether `n` is prime. Handles
  edge cases (`n < 2` is not prime).

Acceptance:
- `primes_below(20) == [2, 3, 5, 7, 11, 13, 17, 19]`
- `primes_below(2) == []`
- `is_prime(1) is False` and `is_prime(2) is True`
- No external dependencies; standard library only.

Also drop a tiny `test_primes.py` with at least three assertion-based
tests covering the cases above. End your turn with a one-line summary of
what you delivered.

## Iteration history
- iter 0: Initial spec generation → Provide scaffolding for primes module and tests.