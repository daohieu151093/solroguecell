import os
import requests

API_BASE = os.getenv("API_BASE", "https://api.example.com")
API_KEY = os.getenv("API_KEY", "replace_me")

def auth():
    return {"Authorization": f"Bearer {API_KEY}"}

def get_price(symbol="ETH"):
    r = requests.get(f"{API_BASE}/price", params={"symbol": symbol})
    r.raise_for_status()
    return r.json()

def portfolio():
    r = requests.get(f"{API_BASE}/agent/portfolio", headers=auth())
    r.raise_for_status()
    return r.json()

def submit_trade(symbol="ETH", side="LONG", size=1.0, reasoning=""):
    payload = {
        "symbol": symbol,
        "side": side,
        "size": size,
        "entry": "market",
        "reasoning": reasoning or "Entry thesis: liquidity sweep then reclaim. Risk cap 1R. Exit trail after 1R."
    }
    r = requests.post(f"{API_BASE}/trade/execute", json=payload, headers=auth())
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    print("Price:", get_price("ETH"))
    print("Portfolio:", portfolio())
    print("Trade:", submit_trade())
