"""Verify the Brain AI public disclosure bundle."""

import hashlib
import json
import math
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "MANIFEST.sha256.json"
EVIDENCE = ROOT / "evidence/public-r013-summary.json"


def tracked_files():
    result = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=ROOT
    )
    return sorted(
        Path(p.decode("utf-8"))
        for p in result.split(b"\0")
        if p and p != b"MANIFEST.sha256.json"
    )


def digest(path):
    """Hash the Git index blob, independent of Windows/Linux line endings."""
    content = subprocess.check_output(
        ["git", "show", f":{path.relative_to(ROOT).as_posix()}"],
        cwd=ROOT,
    )
    return hashlib.sha256(content).hexdigest()


def build_manifest():
    return {
        p.as_posix(): digest(ROOT / p)
        for p in tracked_files()
    }


def validate_evidence():
    data = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    r = data["results"]

    worlds = r["worlds"]
    resolved = r["resolved"]
    correct = r["correct_resolutions"]
    incorrect = r["incorrect_resolutions"]

    assert worlds == 1_000_000
    assert resolved == correct + incorrect
    assert 0 <= resolved <= worlds

    accuracy = correct / resolved * 100
    false_rate = incorrect / worlds * 100

    assert math.isclose(
        accuracy,
        r["resolved_accuracy_percent"],
        abs_tol=0.000001,
    )

    assert math.isclose(
        false_rate,
        r["false_resolution_rate_percent_all_worlds"],
        abs_tol=0.000001,
    )

    assert data["implementation_included"] is False
    print("PASS: R-013 published arithmetic and disclosure metadata")


def main():
    validate_evidence()
    expected = build_manifest()

    if "--write-manifest" in sys.argv:
        MANIFEST.write_text(
            json.dumps(expected, indent=2) + "\n",
            encoding="utf-8",
        )
        print("Updated public SHA-256 manifest")
        return

    actual = json.loads(MANIFEST.read_text(encoding="utf-8"))

    if actual != expected:
        missing = sorted(set(expected) - set(actual))
        extra = sorted(set(actual) - set(expected))
        changed = sorted(
            p for p in set(actual) & set(expected)
            if actual[p] != expected[p]
        )
        print("FAIL: Public manifest mismatch")
        print("Missing:", missing)
        print("Extra:", extra)
        print("Changed:", changed)
        sys.exit(1)

    print(f"PASS: SHA-256 manifest ({len(expected)} tracked files)")


if __name__ == "__main__":
    main()
