import unittest
from promotion_gate import wilson_upper, assess_promotion
def make(n, failures=0):
    return [{"case_id":str(i),"passed":i>=failures,"critical_failure":False,"label_origin":"independent_human"} for i in range(n)]
class Tests(unittest.TestCase):
    def test_improvement(self): self.assertTrue(assess_promotion(make(100,20),make(100))["eligible"])
    def test_small_sample(self): self.assertFalse(assess_promotion(make(30,10),make(30))["eligible"])
    def test_no_improvement(self): self.assertFalse(assess_promotion(make(100),make(100))["eligible"])
    def test_regression(self):
        base=make(100,2);candidate=make(100);candidate[50]["passed"]=False
        self.assertIn("case regressions",assess_promotion(base,candidate)["reasons"])
    def test_critical(self):
        candidate=make(100);candidate[0].update(passed=False,critical_failure=True)
        self.assertIn("candidate critical failures",assess_promotion(make(100,20),candidate)["reasons"])
    def test_fake_label(self):
        candidate=make(100);candidate[0]["label_origin"]="model"
        self.assertFalse(assess_promotion(make(100,20),candidate)["eligible"])
    def test_case_mismatch(self):
        candidate=make(100);candidate.pop()
        self.assertIn("case sets differ",assess_promotion(make(100,20),candidate)["reasons"])
    def test_duplicate(self):
        candidate=make(100);candidate.append(candidate[0])
        self.assertFalse(assess_promotion(make(100,20),candidate)["eligible"])
    def test_failure_bound(self): self.assertFalse(assess_promotion(make(100,40),make(100,10))["eligible"])
    def test_zero_failure_upper(self): self.assertLess(wilson_upper(0,100),.1)
    def test_bad_count(self):
        with self.assertRaises(ValueError): wilson_upper(0,0)
if __name__=="__main__": unittest.main()
