---
name: genpark-quant-black-litterman-portfolio-rebalancer-skill
description: Quant Black-Litterman Bayesian portfolio rebalancer integrating market equilibrium with subjective agent views and covariance constraints.
category: Service
version: 1.0.0
license: MIT
tools:
  - {'name': 'rebalance_portfolio', 'description': 'Compute optimal Bayesian asset allocation weights blending equilibrium and views.'}
---

# Genpark Quant Black Litterman Portfolio Rebalancer Skill

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Genpark Quant Black Litterman Portfolio Rebalancer Skill**.
Your primary directive is to execute: Quant Black-Litterman Bayesian portfolio rebalancer integrating market equilibrium with subjective agent views and covariance constraints.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `{'name': 'rebalance_portfolio', 'description': 'Compute optimal Bayesian asset allocation weights blending equilibrium and views.'}`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `{'name': 'rebalance_portfolio', 'description': 'Compute optimal Bayesian asset allocation weights blending equilibrium and views.'}`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
