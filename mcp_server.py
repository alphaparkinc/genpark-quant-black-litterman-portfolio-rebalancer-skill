# -*- coding: utf-8 -*-
import sys, json, math
from client import GenParkQuantBlackLittermanPortfolioRebalancer

rebalancer = GenParkQuantBlackLittermanPortfolioRebalancer()

def run_tool(name, args):
    if name == "rebalance_portfolio":
        assets = args.get("assets", ["BTC", "ETH"])
        mkt_weights = args.get("market_weights", [0.7, 0.3])
        cov = args.get("covariance_matrix", [[0.16, 0.10], [0.10, 0.25]])
        views = args.get("agent_views", [])
        return rebalancer.rebalance_portfolio(assets, mkt_weights, cov, views)
    else:
        raise ValueError(f"Unknown tool: {name}")

def main():
    if "--test" in sys.argv:
        print("[TEST] Running GenPark Black-Litterman Rebalancer Self-Test...")
        assets = ["BTC", "ETH"]
        w = [0.7, 0.3]
        cov = [[0.16, 0.10], [0.10, 0.25]]
        views = [{"asset": "ETH", "expected_excess_return": 0.30, "confidence": 0.8}]
        res = rebalancer.rebalance_portfolio(assets, w, cov, views)
        assert len(res["optimal_rebalanced_weights"]) == 2
        assert math.isclose(sum(res["optimal_rebalanced_weights"]), 1.0, abs_tol=1e-2)
        print("[TEST] All tests passed successfully!")
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = run_tool(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"jsonrpc": "2.0", "id": req.get("id"), "result": res}))
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
