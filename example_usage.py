# -*- coding: utf-8 -*-
from client import GenParkQuantBlackLittermanPortfolioRebalancer

def main():
    rebalancer = GenParkQuantBlackLittermanPortfolioRebalancer(risk_aversion=2.5)
    print("=== GenPark Quant Black-Litterman Portfolio Rebalancer ===")

    assets = ["BTC", "ETH", "SOL"]
    market_weights = [0.60, 0.30, 0.10]
    # Covariance matrix (annualized)
    cov = [
        [0.18, 0.12, 0.10],
        [0.12, 0.24, 0.15],
        [0.10, 0.15, 0.35]
    ]

    # Agent subjective view: SOL will outperform with 28% excess return (confidence 0.85)
    views = [
        {"asset": "SOL", "expected_excess_return": 0.28, "confidence": 0.85}
    ]

    res = rebalancer.rebalance_portfolio(assets, market_weights, cov, views)
    print("Assets:", res["assets"])
    print("Prior Market Weights:   ", res["market_weights"])
    print("Optimal Rebalanced Alloc:", res["optimal_rebalanced_weights"])
    print(f"Portfolio Expected Return: {res['portfolio_expected_excess_return']*100:.1f}%, Sharpe: {res['expected_sharpe_ratio']}")

if __name__ == "__main__":
    main()
