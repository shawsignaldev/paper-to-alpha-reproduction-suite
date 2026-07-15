from dataclasses import dataclass

@dataclass(frozen=True)
class Evidence:
    has_code: bool
    has_data: bool
    has_metrics: bool
    has_notes: bool

def reproduction_score(evidence: Evidence) -> float:
    return sum([evidence.has_code, evidence.has_data, evidence.has_metrics, evidence.has_notes]) / 4

def reproduction_status(score: float) -> str:
    return "reproduced" if score >= 1.0 else "partial" if score >= 0.5 else "insufficient"
