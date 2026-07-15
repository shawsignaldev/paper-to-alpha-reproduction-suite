# Validation Evidence

## Current Evidence

The current repository proves deterministic behavior through unit tests. The important evidence
themes are: evidence booleans, reproduction score, partial/reproduced labels, and missing-evidence tests. These checks are deliberately modest, but they establish a baseline that
should not regress as the implementation grows.

## Stronger Validation

Stronger validation should include point-in-time fixtures, multiple synthetic regimes, invalid-input
cases, and a small generated report. For market-data systems, replay and sequence integrity should
be explicit. For options systems, spread, Greeks, and expiration mechanics should be represented.
For agentic research systems, evidence gates and human-approval boundaries should be enforced.

## Promotion Criteria

A repo graduates from toy model to serious prototype when it has deterministic tests, documented
assumptions, validation reports, failure-mode notes, and a clear interface for downstream dashboards.
Performance or research claims should only be made after the evidence records are in the repo.

## Regression Policy

Every discovered bug should become a test fixture. Every changed assumption should update the docs.
Every new metric should have a deterministic example and a plain-language explanation.
