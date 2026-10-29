# -*- coding: utf-8 -*-
"""
GenPark Quant Black-Litterman Portfolio Rebalancer
Standard Library only: math, typing.
Bayesian portfolio asset allocation blending market equilibrium returns with
subjective agent views and covariance matrices, enforcing long-only constraints.
"""

import math
from typing import Dict, List, Any

class GenParkQuantBlackLittermanPortfolioRebalancer:
    def __init__(self, risk_aversion: float = 2.5, tau: float = 0.05):
        self.risk_aversion = risk_aversion
        self.tau = tau

    def _dot(self, A: List[float], B: List[float]) -> float:
        return sum(a * b for a, b in zip(A, B))

    def _mat_vec_mul(self, M: List[List[float]], v: List[float]) -> List[float]:
        return [self._dot(row, v) for row in M]

    def rebalance_portfolio(self, assets: List[str],
                            market_weights: List[float],
                            covariance_matrix: List[List[float]],
                            agent_views: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        assets: ["BTC", "ETH", "SOL"]
        market_weights: [0.6, 0.3, 0.1]
        covariance_matrix: 3x3 annual covariance
        agent_views: list of {"asset": "SOL", "expected_excess_return": 0.25, "confidence": 0.8}
        """
        n = len(assets)
        if len(market_weights) != n or len(covariance_matrix) != n:
            raise ValueError("Dimension mismatch between assets, weights, and covariance")

        # 1. Implied equilibrium excess returns: Pi = delta * Sigma * w_mkt
        pi = [self.risk_aversion * val for val in self._mat_vec_mul(covariance_matrix, market_weights)]

        # 2. Blend views into posterior expected returns
        posterior_returns = list(pi)
        for view in agent_views:
            idx = assets.index(view["asset"]) if view["asset"] in assets else -1
            if idx != -1:
                q = float(view["expected_excess_return"])
                conf = max(0.1, min(1.0, float(view.get("confidence", 0.5))))
                # Bayesian shrinkage between equilibrium and subjective view
                posterior_returns[idx] = (1.0 - conf) * pi[idx] + conf * q

        # 3. Mean-variance optimal weights: w* = (1 / delta) * inv(Sigma) * E[R]
        # Diagonal inverse approximation for standard library stability
        diag_inv = [1.0 / max(1e-4, covariance_matrix[i][i]) for i in range(n)]
        raw_weights = [(1.0 / self.risk_aversion) * diag_inv[i] * posterior_returns[i] for i in range(n)]

        # 4. Long-only constraint and normalization: w_i >= 0, sum(w_i) = 1.0
        clipped = [max(0.0, w) for w in raw_weights]
        tot = sum(clipped)
        final_weights = [round(w / tot, 4) for w in clipped] if tot > 0 else market_weights

        # Portfolio expected metrics
        port_ret = sum(final_weights[i] * posterior_returns[i] for i in range(n))
        port_var = 0.0
        for i in range(n):
            for j in range(n):
                port_var += final_weights[i] * final_weights[j] * covariance_matrix[i][j]
        port_vol = math.sqrt(max(0.0, port_var))
        sharpe = round(port_ret / max(1e-4, port_vol), 2)

        return {
            "assets": assets,
            "market_weights": market_weights,
            "optimal_rebalanced_weights": final_weights,
            "implied_equilibrium_returns": [round(r, 4) for r in pi],
            "posterior_expected_returns": [round(r, 4) for r in posterior_returns],
            "portfolio_expected_excess_return": round(port_ret, 4),
            "portfolio_expected_volatility": round(port_vol, 4),
            "expected_sharpe_ratio": sharpe
        }
