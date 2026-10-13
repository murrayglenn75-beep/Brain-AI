import unittest
from benchmark import score, evaluate_fixtures

class BenchmarkTests(unittest.TestCase):
    def test_perfect(self):
        self.assertEqual(score([("a","rule",1)], [("a","rule",1)])["f1"],1)
    def test_false_positive(self):
        r=score([], [("a","rule",1)])
        self.assertEqual(r["fp"],1)
        self.assertEqual(r["precision"],0)
    def test_missing_evidence(self):
        r=score([("a","rule",2)], [])
        self.assertEqual(r["fn"],1)
        self.assertEqual(r["recall"],0)
    def test_fixture_separation(self):
        cases=[{"id":"owned1","input":"sample","ground_truth":[{"rule":"eval","line":1}]}]
        self.assertEqual(evaluate_fixtures(cases,lambda _: [{"rule":"eval","line":1}])["tp"],1)

if __name__=="__main__":
    unittest.main()
