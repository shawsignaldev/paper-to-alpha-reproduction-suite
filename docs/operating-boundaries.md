# Operating Boundaries

## Public-Safe Scope

This repo uses synthetic examples and public-safe logic. It does not connect to venues, external
brokerage endpoints, paid market datasets, or live execution systems. That boundary is intentional: it
keeps the portfolio inspectable while protecting private research and credentials.

## Main Risk

a paper can be reproduced mechanically while still failing economic robustness or data-availability constraints. A serious reviewer should see that this risk is named directly rather than hidden behind
clean code. The prototype should be read as a controlled component, not a complete trading platform.

## Usage Rule

Use the model for education, fixtures, architecture review, and as a seed for deeper private
experiments. Do not treat its output as an isolated decision signal. Downstream systems need data lineage,
transaction-cost assumptions, timing assumptions, and human review gates.

## Future Work

The next useful additions are structured run reports, generated diagrams, richer failure fixtures,
and a unified portfolio dashboard that shows which repos are reference models, which are validated
prototypes, and which are paper-reproduction artifacts.
