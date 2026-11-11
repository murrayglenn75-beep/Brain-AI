"""Read-only evaluation gate for harness promotion; cannot change permission levels."""
import math

def wilson_upper(failures, count, z=1.645):
    if type(failures) is not int or type(count) is not int or count <= 0 or not 0 <= failures <= count:
        raise ValueError("invalid counts")
    p = failures / count
    denominator = 1 + z*z/count
    return min(1.0, (p + z*z/(2*count) + z*math.sqrt((p*(1-p)+z*z/(4*count))/count))/denominator)

def assess_promotion(baseline, candidate, *, min_cases=35, max_failure_upper=0.10):
    """Evaluation hint only. String label_origin is not authenticated evidence."""
    errors = []
    if not isinstance(baseline, list) or not isinstance(candidate, list):
        return {"eligible":False,"reasons":["invalid datasets"]}
    if type(min_cases) is not int or min_cases < 1 or not 0 < max_failure_upper < 1:
        raise ValueError("invalid evaluation thresholds")
    def index(rows, name):
        indexed = {}
        for row in rows:
            if not isinstance(row, dict) or set(row) != {"case_id","passed","critical_failure","label_origin"}:
                errors.append(f"{name}: malformed result")
                continue
            case_id = row["case_id"]
            if not isinstance(case_id, str) or not case_id.strip() or case_id in indexed:
                errors.append(f"{name}: invalid or duplicate case")
                continue
            if type(row["passed"]) is not bool or type(row["critical_failure"]) is not bool:
                errors.append(f"{name}: invalid verdict")
                continue
            if row["critical_failure"] and row["passed"]:
                errors.append(f"{name}: inconsistent critical verdict")
                continue
            if row["label_origin"] != "independent_human":
                errors.append(f"{name}: independent labels required")
                continue
            indexed[case_id] = row
        return indexed
    a, b = index(baseline, "baseline"), index(candidate, "candidate")
    if set(a) != set(b):
        errors.append("case sets differ")
    if len(b) < min_cases:
        errors.append("not enough cases")
    bad = sum(not x["passed"] for x in b.values())
    upper = wilson_upper(bad, len(b)) if b else 1.0
    if upper > max_failure_upper:
        errors.append("failure confidence bound too high")
    if any(x["critical_failure"] for x in b.values()):
        errors.append("candidate critical failures")
    regressions = sorted(k for k in a.keys() & b.keys() if a[k]["passed"] and not b[k]["passed"])
    if regressions:
        errors.append("case regressions")
    if b and sum(x["passed"] for x in b.values()) <= sum(x["passed"] for x in a.values()):
        errors.append("no measured pass-count improvement")
    return {"eligible":not errors,"reasons":errors,"cases":len(b),"failures":bad,
            "failure_upper_bound":round(upper,6),"regressions":regressions,
            "note":"evaluation hint; never an authority grant"}
