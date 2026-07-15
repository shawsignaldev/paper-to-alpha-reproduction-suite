from paper_to_alpha_reproduction_suite.reproduction import Evidence, reproduction_score, reproduction_status

def test_reproduction_score_counts_evidence_items() -> None:
    score = reproduction_score(Evidence(has_code=True, has_data=False, has_metrics=True, has_notes=True))
    assert score == 0.75

def test_reproduction_status_requires_high_score() -> None:
    assert reproduction_status(0.75) == "partial"
    assert reproduction_status(1.0) == "reproduced"
