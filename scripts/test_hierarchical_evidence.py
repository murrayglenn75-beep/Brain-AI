import tempfile
import unittest
from pathlib import Path
from context_layer import Principal, Collection, AccessDenied
from hierarchical_evidence import retrieve_sections

class SectionRetrievalTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "manual.md").write_text("# Overview\nintro\n## Revenue\nRevenue is gross.\n### Refunds\nRefunds reduce net.\n## Security\nUnauthorized calls must fail.\n", encoding="utf-8")
        self.col = Collection("manual", "company", self.root)
        self.p = Principal("user", "company", frozenset({"manual"}))
    def tearDown(self):
        self.tmp.cleanup()
    def test_section_path(self):
        r = retrieve_sections(self.p, self.col, "Refunds")
        self.assertEqual(r[0]["section_title"], "Refunds")
        self.assertEqual(r[0]["section_start"], 5)
        self.assertEqual(r[0]["section_end"], 6)
    def test_section_boundary(self):
        r = retrieve_sections(self.p, self.col, "Revenue is")
        self.assertEqual(r[0]["section_title"], "Revenue")
        self.assertEqual(r[0]["section_end"], 6)
    def test_provenance(self):
        r = retrieve_sections(self.p, self.col, "Unauthorized")[0]
        self.assertEqual(r["line"], 8)
        self.assertEqual(len(r["sha256"]), 64)
    def test_cross_tenant(self):
        with self.assertRaises(AccessDenied):
            retrieve_sections(Principal("bad", "other", frozenset({"manual"})), self.col, "Revenue")
    def test_empty(self):
        self.assertEqual(retrieve_sections(self.p, self.col, ""), [])
    def test_invalid_limit(self):
        with self.assertRaises(ValueError):
            retrieve_sections(self.p, self.col, "Revenue", limit=0)
if __name__ == "__main__":
    unittest.main()
