# Product Evaluation Criteria — BGBlur

Evaluate **BGBlur** (https://bgblur.com) against each criterion below.

**Product data:** `products/bgblur/product.md`  
**Scenarios:** `products/bgblur/scenarios.md`  
**Machine spec:** `src/bgblur_spec.py`  
**Run evaluations:** `cd product-evaluation && python -m pytest`

**Exit condition:** Evaluation complete when **all** criteria are ✅.

---

## Core blur capabilities

- [ ] **Background blur documented** — Video and photo background blur defined with motion tracking notes
- [ ] **License plate blur documented** — Plate detection and motion-tracked blur for dashcam/street footage
- [ ] **Face blur & anonymization documented** — Distinct face blur vs face anonymization capabilities with compliance use cases
- [ ] **Blur anything documented** — Prompt-based custom object blur with multi-object support

## Privacy & limits

- [ ] **Privacy claims consistent** — Client-side processing and no permanent server storage reflected in spec
- [ ] **Free tier limits consistent** — Spec limits match canonical values in `product.md` (500 MB, 5 minutes)
- [ ] **Export formats complete** — All advertised export formats (MP4, MOV, WebM) present in spec

## Scenario coverage

- [ ] **Dashcam scenario exists** — Real-use scenario for license plate blur in moving vehicle footage
- [ ] **Mobile scenario exists** — Real-use scenario for iPhone/Android browser usage
- [ ] **All capabilities mapped** — Every capability in the spec has at least one scenario in `scenarios` dict

## Product lines & personas

- [ ] **API & SDK product line documented** — Developer embed path listed in product lines
- [ ] **Enterprise persona covered** — Enterprise/CCTV persona and scenario documented

## Quality standards

- [ ] **Evaluations pass** — All tests in `tests/` pass (`python -m pytest` exits 0)
- [ ] **Findings documented** — `findings.md` records baseline, weaknesses, fixes, and re-evaluation per iteration

---

## Guardrails

- Do not skip any evaluation step
- Do not change these criteria mid-loop
- Base evaluations on real-use scenarios in `products/bgblur/scenarios.md`
- Keep `product.md`, `bgblur_spec.py`, and scenarios in sync when applying fixes

---

## Evaluation Output Format

After each iteration, respond with:

```
Product Evaluation — BGBlur — Iteration N
──────────────────────────────────────────
✅/❌ Criterion name — reason
...
──────────────────────────────────────────
Pytest: X passed, Y failed
Status: INCOMPLETE (A/B passed) | COMPLETE (all passed)
Next action: <highest-priority fix>
```

Only report **COMPLETE** when every criterion above is ✅ and pytest is green.
