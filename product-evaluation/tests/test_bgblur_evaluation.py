import pytest

from src.bgblur_spec import BgBlurProductSpec


@pytest.fixture
def spec():
    return BgBlurProductSpec()


class TestBlurCapabilities:
    def test_background_blur_documented(self, spec):
        assert spec.has_capability("background_blur")
        assert "video" in spec.capabilities["background_blur"]["surfaces"]

    def test_license_plate_blur_documented(self, spec):
        assert spec.has_capability("license_plate_blur")

    def test_face_blur_and_anonymization_documented(self, spec):
        assert spec.has_capability("face_blur")
        assert spec.has_capability("face_anonymization")

    def test_blur_anything_documented(self, spec):
        assert spec.has_capability("blur_anything")


class TestPrivacyAndLimits:
    def test_privacy_claims_consistent(self, spec):
        assert spec.privacy["processing"] == "browser_local"
        assert spec.privacy["permanent_server_storage"] is False

    def test_free_tier_limits_match_product_doc(self, spec):
        assert spec.limits_match_product_doc()

    def test_export_formats_include_webm(self, spec):
        assert spec.export_format_supported("webm")


class TestScenarioCoverage:
    def test_dashcam_scenario_exists(self, spec):
        assert "dashcam_license_plate" in spec.scenarios

    def test_mobile_scenario_exists(self, spec):
        assert "mobile_browser_blur" in spec.scenarios

    def test_all_capabilities_have_scenarios(self, spec):
        assert spec.all_capabilities_have_scenarios()


class TestProductLinesAndPersonas:
    def test_api_sdk_product_line_documented(self, spec):
        assert "api_sdk" in spec.product_lines

    def test_enterprise_persona_covered(self, spec):
        assert "enterprise" in spec.personas
        assert "enterprise_cctv_redaction" in spec.scenarios
