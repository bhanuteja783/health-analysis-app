import unittest

from logic import detect_diseases


class TestHealthTermDetection(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(detect_diseases(""), {})

    def test_detects_common_lab_terms(self):
        result = detect_diseases(
            "TSH is reported. LDL and HDL are listed. HbA1c and BP are also present."
        )
        self.assertIn("thyroid", result)
        self.assertIn("cholesterol", result)
        self.assertIn("blood sugar", result)
        self.assertIn("blood pressure", result)

    def test_case_insensitive_matching(self):
        result = detect_diseases("Patient has FEVER and elevated BILIRUBIN.")
        self.assertIn("fever", result)
        self.assertIn("jaundice", result)


if __name__ == "__main__":
    unittest.main()
