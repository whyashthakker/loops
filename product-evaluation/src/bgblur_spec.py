"""Structured BGBlur product spec for evaluation loops.

Derived from products/bgblur/product.md. Intentionally incomplete in places
so the Product Evaluation Loop can identify and fix gaps.
"""


class BgBlurProductSpec:
    """Machine-readable product specification for BGBlur."""

    name = "BGBlur"
    url = "https://bgblur.com"
    tagline = "Blur license plates & backgrounds. Anonymize or blur faces with AI."

    capabilities = {
        "background_blur": {"surfaces": ["video", "photo"]},
        "license_plate_blur": {"surfaces": ["video"]},
        "face_blur": {"surfaces": ["video", "photo"]},
        "face_anonymization": {"surfaces": ["video"]},
        "blur_anything": {"surfaces": ["video"]},
        "motion_tracking": {"surfaces": ["video"]},
        "bulk_blur": {"surfaces": ["photo", "video"]},
        "gif_blur": {"surfaces": ["gif"]},
    }

    input_formats = ["mp4", "mov", "m4v"]
    export_formats = ["mp4", "mov"]  # gap: WebM advertised on site

    free_tier = {"max_mb": 200, "max_minutes": 10}  # gap: product.md says 500 MB / 5 min
    paid_tier = {"max_mb": 1024, "max_minutes": 10}

    privacy = {
        "processing": "browser_local",
        "permanent_server_storage": False,
    }

    product_lines = ["video", "photo", "enterprise"]  # gap: api_sdk missing

    scenarios = {
        "vlogger_background_blur": "background_blur",
        "social_face_anonymization": "face_anonymization",
        "bulk_photo_blur": "bulk_blur",
        "custom_object_blur": "blur_anything",
        # gaps: dashcam, mobile, enterprise cctv, api embed
    }

    personas = [
        "content_creator",
        "social_media_manager",
        "video_editor",
        "marketing_legal",
        "educator",
    ]  # gap: enterprise, developer

    def has_capability(self, name: str) -> bool:
        return name in self.capabilities

    def scenario_covers_capability(self, capability: str) -> bool:
        return capability in self.scenarios.values()

    def all_capabilities_have_scenarios(self) -> bool:
        covered = set(self.scenarios.values())
        return covered == set(self.capabilities.keys())

    def export_format_supported(self, fmt: str) -> bool:
        return fmt.lower() in self.export_formats

    def limits_match_product_doc(self) -> bool:
        """Free tier should match canonical limits in product.md (500 MB, 5 min)."""
        return self.free_tier == {"max_mb": 500, "max_minutes": 5}
