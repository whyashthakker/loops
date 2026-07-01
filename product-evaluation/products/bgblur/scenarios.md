# BGBlur — Real-Use Evaluation Scenarios

Production-like scenarios for the Product Evaluation Loop. Each scenario maps to a persona and capability from `product.md`.

---

## Scenario 1: Vlogger background blur

**Persona:** Content creator (YouTube vlogger)  
**Capability:** Background blur  
**Flow:**
1. Upload a 3-minute MP4 vlog (under free tier limits)
2. Apply background blur with motion tracking
3. Export MP4 and verify subject stays sharp, background softened
4. Confirm processing completes in browser without desktop app

**Pass criteria:** Background blur applies frame-accurately; export is HD; no server-side permanent storage claim violated.

---

## Scenario 2: Dashcam license plate anonymization

**Persona:** Fleet operator / compliance editor  
**Capability:** License plate blur + motion tracking  
**Flow:**
1. Upload dashcam footage with moving vehicles
2. Apply license plate blur
3. Verify plates stay blurred as vehicles move through frame
4. Export for legal/compliance review

**Pass criteria:** Plates detected and tracked across frames; blur remains locked on moving plates.

---

## Scenario 3: Social clip face anonymization

**Persona:** Social media manager  
**Capability:** Face anonymization  
**Flow:**
1. Upload a 30-second vertical clip for TikTok/Instagram
2. Apply face anonymization to all visible faces
3. Export WebM or MP4 suitable for platform upload
4. Confirm identities are not recoverable from export

**Pass criteria:** All faces anonymized; export format supported; clip meets platform length limits.

---

## Scenario 4: Bulk photo background blur

**Persona:** Agency / marketing team  
**Capability:** Bulk background blur  
**Flow:**
1. Upload a batch of 50 product photos
2. Apply uniform background blur across batch
3. Download all results with consistent blur strength

**Pass criteria:** Batch completes without manual per-image masking; results are uniform.

---

## Scenario 5: Enterprise CCTV redaction

**Persona:** Enterprise security team  
**Capability:** Face blur + license plate blur + batch processing  
**Flow:**
1. Process high-volume CCTV clips through enterprise pipeline
2. Redact faces and plates in bulk
3. Audit trail available for compliance review

**Pass criteria:** High-volume processing supported; enterprise tier documented; privacy claims hold at scale.

---

## Scenario 6: Mobile browser blur

**Persona:** Field educator  
**Capability:** Face blur on mobile  
**Flow:**
1. Open bgblur.com on iPhone or Android browser
2. Upload a short campus tour clip
3. Blur student faces and export

**Pass criteria:** Mobile-responsive UI; upload and blur work on mobile browser; export succeeds.

---

## Scenario 7: Developer API embed

**Persona:** Developer  
**Capability:** BGBlur API & SDK  
**Flow:**
1. Integrate blur via REST API or SDK
2. Send video programmatically and receive blurred output
3. Document rate limits and auth requirements

**Pass criteria:** API/SDK documented; integration path clear; limits specified.

---

## Scenario 8: Custom object blur (Blur Anything)

**Persona:** Freelance video editor  
**Capability:** Blur anything (prompt-based)  
**Flow:**
1. Upload interview footage with branded signage in background
2. Prompt "blur logo on wall" or comma-separated object list
3. Verify only targeted objects are blurred

**Pass criteria:** Prompt-based object detection works; multiple objects supported via comma separation.

---

## Scenario 9: Short-form GIF blur

**Persona:** Social media manager  
**Capability:** GIF blur  
**Flow:**
1. Upload an animated GIF containing a visible face or plate
2. Apply blur across all frames of the GIF
3. Export as GIF and confirm blur persists through the loop

**Pass criteria:** Blur is applied consistently across all GIF frames; exported GIF loops correctly with blur intact.

---

## Scenario Coverage Matrix

| Capability | Scenarios |
|---|---|
| Background blur | 1, 4 |
| License plate blur | 2, 5 |
| Face blur | 6 |
| Face anonymization | 3 |
| Blur anything | 8 |
| Motion tracking | 1, 2, 5 |
| Bulk / batch | 4, 5 |
| Mobile | 6 |
| API & SDK | 7 |
| GIF blur | 9 |

**Minimum for loop exit:** Every capability in `product.md` must map to at least one scenario, and every scenario must have documented pass criteria.
