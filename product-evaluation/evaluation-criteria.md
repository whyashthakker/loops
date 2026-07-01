# Product Evaluation Criteria

Evaluate the **TaskManager** product in `src/task_manager.py` against each capability below. Run tests in a production-like environment: `cd product-evaluation && python -m pytest`.

**Exit condition:** Evaluation complete when **all** criteria are ✅.

---

## Create capability

- [ ] **Valid input accepted** — Creating a task with a non-empty title returns a task with a unique id and `done=False`
- [ ] **Invalid input rejected** — Empty or whitespace-only titles raise `ValueError`

## List capability

- [ ] **Snapshot returned** — `list_tasks()` returns a copy; callers cannot mutate internal state
- [ ] **Completed tasks filterable** — `list_tasks(include_completed=False)` excludes completed tasks

## Complete capability

- [ ] **Known task completes** — Completing an existing task sets `done=True` and returns the updated task
- [ ] **Unknown task rejected** — Completing a non-existent id raises `ValueError`

## Quality standards

- [ ] **Real-use scenarios covered** — All tests in `tests/` pass (`python -m pytest` exits 0)
- [ ] **Findings documented** — `findings.md` records baseline, weaknesses, fixes, and re-evaluation results for each iteration

---

## Guardrails

- Do not skip any evaluation step
- Do not change these criteria mid-loop
- Do not add capabilities outside Create / List / Complete unless a fix requires it
- Base evaluations on real-use scenarios in `tests/`, not hypothetical edge cases

---

## Evaluation Output Format

After each iteration, respond with:

```
Product Evaluation — Iteration N
────────────────────────────────
✅/❌ Criterion name — reason
...
────────────────────────────────
Pytest: X passed, Y failed
Status: INCOMPLETE (A/B passed) | COMPLETE (all passed)
Next action: <highest-priority fix>
```

Only report **COMPLETE** when every criterion above is ✅ and pytest is green.
