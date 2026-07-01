Start the "Product Evaluation Loop" loop.

Goal: Ensure comprehensive evaluation and enhancement of BGBlur product quality
Product: BGBlur (https://bgblur.com)
Product data: products/bgblur/product.md
Scenarios: products/bgblur/scenarios.md
Max iterations: 10
Between iterations run: product evaluation (see evaluation-criteria.md in this folder)
Exit when: All evaluation criteria pass
Document findings in: findings.md (in this folder)

Guardrails:
- Do not skip any evaluation steps
- Do not modify evaluation criteria mid-loop
- Do not introduce changes outside the documented fix plan
- Do not proceed to the next iteration without completing the current one
- Base all evaluations on real-use scenarios in products/bgblur/scenarios.md

You are now entering the Product Evaluation Loop for BGBlur. Your goal is to evaluate the product against defined capability criteria, identify weaknesses in product data and spec coverage, implement fixes, and re-evaluate until quality standards are met.

Begin by reading products/bgblur/product.md and evaluation-criteria.md, then run evaluations (`cd product-evaluation && python -m pytest`). Document baseline findings in findings.md. For each weakness, update product.md, scenarios.md, and src/bgblur_spec.py as needed, then rerun evaluations before moving on.

Self-pace this loop. After each iteration, run `product evaluation` against evaluation-criteria.md and pytest. Only continue if the exit condition is not met. Stop when all criteria pass or 10 iterations are reached. Give a short status update each pass.
