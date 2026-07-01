# Checklist Review

Evaluate the **current pull request** against each item below. Report status as ✅ (pass) or ❌ (fail) with a one-line reason.

**Exit condition:** Checklist complete when **all** items are ✅.

---

## Code Quality

- [ ] **No debug artifacts** — No `print`/`console.log`/`debugger`/`TODO: remove` left in changed files
- [ ] **Input validation** — Public functions validate inputs and raise/return clear errors for invalid input
- [ ] **Docstrings** — New public functions have docstrings explaining args, return value, and raised errors

## Testing

- [ ] **Happy-path test** — At least one test covers the main success case
- [ ] **Edge-case test** — At least one test covers invalid or boundary input

## PR Hygiene

- [ ] **PR description** — PR body explains *what* changed and *why* (not just "add feature")
- [ ] **Focused diff** — Changes are limited to the feature; no unrelated formatting or drive-by edits
- [ ] **Tests pass** — `cd self-improvement && python -m pytest` exits 0

---

## Review Output Format

After reviewing, respond with:

```
Checklist Review — Iteration N
──────────────────────────────
✅/❌ Item name — reason
...
──────────────────────────────
Status: INCOMPLETE (X/Y passed) | COMPLETE (all passed)
Next action: <what to fix if incomplete>
```

Only report **COMPLETE** when every item above is ✅.
