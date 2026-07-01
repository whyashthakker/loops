# Evaluation Findings

Structured log for each Product Evaluation Loop iteration.

---

## Iteration 0 — Baseline

**Date:** 2026-07-01

### Environment
- Branch: main
- Command: `cd product-evaluation && python -m pytest`

### Baseline results
- Pytest: 5 passed, 7 failed
- Criteria passed: 5/12

### Weaknesses identified
1. `free_tier` in `bgblur_spec.py` was 200 MB / 10 min, inconsistent with the canonical 500 MB / 5 min in `product.md`.
2. `export_formats` in spec omitted `webm`, though `product.md` advertises MP4/MOV/WebM export.
3. `scenarios` dict in spec had no entries for dashcam license-plate blur, mobile browser use, enterprise CCTV redaction, or GIF blur — `all_capabilities_have_scenarios()` failed because `motion_tracking` and `gif_blur` capabilities had zero scenario coverage.
4. `product_lines` in spec omitted `api_sdk`, though `product.md` lists "BGBlur API & SDK" as a product line.
5. `personas` in spec omitted `enterprise` and `developer`, though both are listed personas in `product.md` and both have dedicated scenarios in `scenarios.md`.
6. `scenarios.md` had no scenario documenting the GIF blur capability (Scenario Coverage Matrix showed no row for it).
7. `product.md` carried a stale note flagging a 200 MB / 10 min vs 500 MB / 5 min inconsistency without resolution.

### Fixes applied
- `src/bgblur_spec.py`: set `free_tier = {"max_mb": 500, "max_minutes": 5}`; added `"webm"` to `export_formats`; added `"api_sdk"` to `product_lines`; added `"enterprise"` and `"developer"` to `personas`; added `dashcam_license_plate` → `license_plate_blur`, `mobile_browser_blur` → `face_blur`, `enterprise_cctv_redaction` → `motion_tracking`, and `gif_shortform_blur` → `gif_blur` to `scenarios`, giving full coverage of all 8 capabilities.
- `products/bgblur/scenarios.md`: added Scenario 9 (Short-form GIF blur) and updated the Scenario Coverage Matrix to include Motion tracking scenario 5 and the new GIF blur row.
- `products/bgblur/product.md`: resolved the stale 200 MB/500 MB limits note, pointing to the now-matching spec value.

### Re-evaluation results
- Pytest: 12 passed, 0 failed
- Criteria passed: 12/12 — all evaluation criteria in `evaluation-criteria.md` are satisfied:
  - Core blur capabilities (background, plate, face/anonymization, blur-anything): documented and tested — pass.
  - Privacy claims consistent (browser-local, no permanent storage) — pass.
  - Free tier limits consistent (500 MB / 5 min) — pass.
  - Export formats complete (MP4, MOV, WebM) — pass.
  - Dashcam and mobile scenarios exist — pass.
  - All capabilities mapped to at least one scenario — pass.
  - API & SDK product line documented — pass.
  - Enterprise persona and CCTV scenario covered — pass.
  - All tests in `tests/` pass — pass.
  - Findings documented (this file) — pass.

---

## Product Evaluation — BGBlur — Iteration 1
──────────────────────────────────────────
✅ Background blur documented
✅ License plate blur documented
✅ Face blur & anonymization documented
✅ Blur anything documented
✅ Privacy claims consistent
✅ Free tier limits consistent
✅ Export formats complete
✅ Dashcam scenario exists
✅ Mobile scenario exists
✅ All capabilities mapped
✅ API & SDK product line documented
✅ Enterprise persona covered
✅ Evaluations pass
✅ Findings documented
──────────────────────────────────────────
Pytest: 12 passed, 0 failed
Status: COMPLETE (all passed)
Next action: none — exit condition met

---

## Product Evaluation — BGBlur — Iteration 2 (re-check)
──────────────────────────────────────────
Re-ran `python -m pytest` to confirm the loop's completed state still holds; no changes to
`product.md`, `scenarios.md`, or `bgblur_spec.py` since Iteration 1.
──────────────────────────────────────────
Pytest: 12 passed, 0 failed
Status: COMPLETE (all passed)
Next action: none — exit condition still met, loop stopped

---

<!-- Copy the Iteration 0 block above for each new loop run -->
