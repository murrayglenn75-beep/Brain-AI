"""Evidence-grounded static inspection benchmark, public fixtures only."""
from collections import Counter

def score(expected, predicted):
    """Input items are (fixture_id, finding_id, line) tuples."""
    for group in (expected, predicted):
        if any(not isinstance(x, (list, tuple)) or len(x) != 3 for x in group):
            raise ValueError("Expected triples (fixture, rule, line)")
    a, b = set(map(tuple, expected)), set(map(tuple, predicted))
    tp, fp, fn = len(a & b), len(b - a), len(a - b)
    precision = tp / (tp + fp) if tp + fp else 1.0 if not a else 0.0
    recall = tp / (tp + fn) if tp + fn else 1.0
    return dict(tp=tp, fp=fp, fn=fn, precision=precision,
                recall=recall, f1=2*precision*recall/(precision+recall)
                if precision+recall else 0.0)

def evaluate_fixtures(fixtures, inspector):
    """Inspector fixture input is kept separate from ground truth to avoid leakage."""
    expected, predicted = [], []
    for fixture in fixtures:
        item = fixture["id"]
        expected.extend((item, x["rule"], x["line"]) for x in fixture["ground_truth"])
        output = inspector(fixture["input"])
        predicted.extend((item, x["rule"], x["line"]) for x in output)
    return score(expected, predicted)
