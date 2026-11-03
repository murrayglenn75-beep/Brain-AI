import tempfile
import unittest
from pathlib import Path
from knowledge_index import search

class KnowledgeIndexTests(unittest.TestCase):
    def test_exact_line_and_rank(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "decisions.md").write_text("first\nauthority authority\n", encoding="utf-8")
            (root / "notes.md").write_text("authority\n", encoding="utf-8")
            result = search(root, "authority")
            self.assertEqual(result[0]["path"], "decisions.md")
            self.assertEqual(result[0]["line"], 2)
            self.assertEqual(result[0]["score"], 2)

    def test_no_match_or_empty_query(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "x.md").write_text("alpha", encoding="utf-8")
            self.assertEqual(search(root, "beta"), [])
            self.assertEqual(search(root, ""), [])

    def test_symlink_is_ignored(self):
        with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as outside:
            root = Path(d)
            source = Path(outside) / "secret.md"
            source.write_text("secret", encoding="utf-8")
            (root / "link.md").symlink_to(source)
            self.assertEqual(search(root, "secret"), [])

if __name__ == "__main__":
    unittest.main()
