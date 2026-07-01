# BGBlur — Product Data

**URL:** https://bgblur.com  
**Category:** Privacy-first AI blur & anonymization  
**Tagline:** Blur license plates & backgrounds. Anonymize or blur faces with AI.

## Overview

BGBlur is a browser-based video and photo privacy tool. Users upload media, apply AI-powered blur effects (background, faces, license plates, custom objects), and export privacy-safe content without desktop editing software like After Effects.

**Core value props:**
- Runs in the browser — no download required
- Motion-tracked blur for moving subjects
- Client-side processing — files not stored permanently on servers
- One-click face blur, plate blur, and background blur
- Batch processing for high-volume workflows

---

## Key Capabilities

| Capability | Description | Surfaces |
|---|---|---|
| **Background blur** | Soften busy backgrounds to keep focus on the subject | Video, Photo |
| **License plate blur** | Hide plate numbers in driving and street footage | Video |
| **Face blur** | Protect identities with clean face masking | Video, Photo |
| **Face anonymization** | Full anonymization for compliance and public sharing | Video |
| **Blur anything** | Prompt-based object blur — name objects to blur automatically | Video |
| **Motion tracking** | AI tracks moving faces, plates, and objects frame-to-frame | Video |
| **Bulk / batch blur** | Process hundreds of photos or multiple videos at once | Photo, Video |
| **GIF blur** | Blur animated GIFs and short-form motion content | GIF |
| **Screen blur** | Blur sensitive screen regions in recordings | Video |
| **NSFW blur** | Automatic sensitive content blurring | Video |
| **Voice anonymization** | Anonymize voice in audio/video uploads | Audio, Video |

---

## Product Lines

| Line | Audience | Notes |
|---|---|---|
| BGBlur Video | Creators, editors | Most popular — frame-perfect background blur |
| BGBlur Photo | Casual users, marketers | Fast photo background blur |
| BGBlur Enterprise | Security, CCTV, compliance teams | High-volume internal pipelines |
| BGBlur API & SDK | Developers | REST API + SDK for embedding blur in apps |

---

## Supported Formats

### Input
- Video: MP4, MOV, M4V
- Photo: JPG, PNG, WebP (inferred from photo product line)
- Audio (voice anon): direct upload or URL workflow

### Export
- MP4, MOV, WebM (HD quality maintained)

---

## Plan Limits

| Tier | Max file size | Max duration | Notes |
|---|---|---|---|
| Free | 500 MB | 5 minutes | Standard blur tools (face, plate, background, blur anything, screen, NSFW, face anonymization) |
| Paid | 1 GB | 10 minutes | Longer videos, unlimited processing |
| Object Remover | 1 GB | 10 seconds | MP4 and MOV only |
| Voice Anon (direct) | 100 MB | — | Direct upload |
| Voice Anon (URL) | 500 MB | < 10 minutes | Upload or URL workflow |

> **Resolved:** Some marketing pages previously showed free limits of 200 MB / 10 minutes; canonical values are 500 MB / 5 minutes as shown above, and `bgblur_spec.py::free_tier` now matches (Iteration 1).

---

## Target Personas

1. **Content creators** — vloggers, YouTubers needing quick background and plate blur
2. **Social media managers** — short-form compliance for TikTok, Instagram, YouTube
3. **Video editors / freelancers** — natural-looking adaptive blur for client deliverables
4. **Marketing & legal teams** — product demos with plate anonymization, faster legal review
5. **Educators** — campus tours and field demos with student privacy protection
6. **Enterprise / CCTV** — bulk anonymization for security footage pipelines
7. **Developers** — embed blur via API & SDK

---

## Privacy & Compliance Claims

- Processing runs **locally in the browser** via client-side technologies
- Files are **not uploaded or stored permanently** on external servers
- Designed for GDPR-style identity protection and platform compliance rules
- Face anonymization recommended for public sharing and sensitive data handling

---

## Reported Metrics (marketing)

- 120K+ blurred clips processed
- 500K+ license plates hidden

---

## Competitive Positioning

- No After Effects or manual roto required
- Motion-aware tracking vs static masks
- Browser-native vs desktop-only competitors
- Privacy-first (client-side) vs cloud-upload tools

---

## Known Evaluation Focus Areas

Use these when running the Product Evaluation Loop:

1. Capability completeness — are all marketed blur types documented and testable?
2. Limit consistency — do free/paid limits match across product.md, FAQ, and spec code?
3. Privacy claims — does implementation match "browser-local, no permanent storage"?
4. Scenario coverage — do real-use scenarios exist for each persona?
5. Export fidelity — are all advertised export formats supported in spec?
6. Mobile readiness — is mobile browser support documented and evaluable?
