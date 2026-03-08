# Credit Score Prediction System

## What This Project Is About

This project is about building a machine learning system that predicts whether a borrower is likely to default on a loan, using historical Lending Club loan data.

The objective is twofold:
- Learn machine learning deeply (not just train a model).
- Build an end-to-end system that can move from model development to production-style deployment.

## Scope For This Phase

For the current phase, this project is framed as a **post-issuance / post-underwriting default prediction** task.

That means:
- We predict default risk using features that are available after loan issuance decisions.
- Feature inclusion/exclusion decisions are made based on this prediction timestamp.

## Development to Deployment

This project is being developed in progressive layers so it can evolve from experimentation to production-style ML.

1. Framing the ML task and understanding the dataset
- Define target, prediction timestamp, and leakage boundaries.
- Build a column-level data dictionary and domain understanding.

2. Data preparation and splitting
- Global deterministic cleaning (rename, deduplicate, target null handling, irrelevant-column removal).
- Train/validation/test split with reproducible logic.

3. Model development
- Train preprocessing + model pipelines.
- Baseline models and iterative improvements.
- Evaluation using appropriate metrics and error analysis.

4. Experimentation and reproducibility
- Track model versions, parameters, and results.
- Save reproducible artifacts (datasets, pipelines, metrics, model files).

5. Production-style ML engineering (next phase)
- Modular training and inference scripts.
- Model packaging and API serving.
- Containerization and deployment-ready structure.
- Pipeline orchestration and model lifecycle tooling as the project matures.
