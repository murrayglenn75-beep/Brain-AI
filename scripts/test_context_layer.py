import tempfile
import unittest
from pathlib import Path
from context_layer import Principal, Collection, AccessDenied, retrieve

class ContextLayerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "notes.md").write_text("first\nauthority authority\n", encoding="utf-8")
        self.collection = Collection("docs", "tenant-a", self.root)
        self.user = Principal("alice", "tenant-a", frozenset({"docs"}))

    def tearDown(self):
        self.tmp.cleanup()

    def test_exact_source_and_provenance(self):
        hits = retrieve(self.user, self.collection, "authority")
        self.assertEqual((hits[0]["path"], hits[0]["line"], hits[0]["score"]), ("notes.md", 2, 2))
        self.assertEqual(len(hits[0]["sha256"]), 64)
        self.assertEqual(hits[0]["status"], "untrusted_source")

    def test_cross_tenant_denied(self):
        with self.assertRaises(AccessDenied):
            retrieve(Principal("bob", "tenant-b", frozenset({"docs"})), self.collection, "authority")

    def test_collection_denied(self):
        with self.assertRaises(AccessDenied):
            retrieve(Principal("alice", "tenant-a", frozenset()), self.collection, "authority")

    def test_symlink_denied(self):
        with tempfile.TemporaryDirectory() as d:
            secret = Path(d) / "secret.md"
            secret.write_text("secrethit")
            (self.root / "link.md").symlink_to(secret)
            self.assertEqual(retrieve(self.user, self.collection, "secrethit"), [])

    def test_empty(self):
        self.assertEqual(retrieve(self.user, self.collection, ""), [])

    def test_bad_limit(self):
        with self.assertRaises(ValueError):
            retrieve(self.user, self.collection, "authority", 0)

    def test_missing_identity(self):
        with self.assertRaises(AccessDenied):
            retrieve(Principal("", "tenant-a", frozenset({"docs"})), self.collection, "authority")

if __name__ == "__main__":
    unittest.main()
