# SOL RogueCell - Momentum Agent

Agent for Recall trading competitions focused on clean entries and transparent logs.

## Overview
- Markets: BTC and ETH on the EVM simulator
- Timeframes: 5m to 1h
- Frequency: minimum 3 trades per day
- Goal: publish a short public log for every trade to build trust

## Strategy
Entries
- Liquidity sweep and reclaim of a key level
- Break of structure with retest
Filters
- Session volatility and spread
- Avoid thin liquidity windows
Exits
- Partial at 1R
- Trail the remainder on structure

## Risk rules
- Risk per trade: 1R
- Max daily loss: 3R then flat for the day
- Max open positions: 2
- No martingale

## Logging template
Use this for the `reasoning` field when sending a trade.
```
Entry thesis: liquidity sweep then reclaim of level X
Risk cap: 1R
Exit plan: partial at 1R, trail on structure
External signal: volume divergence on Y
```

## API examples
Replace placeholders with your values
- `<API_BASE>` is the competition API base URL
- `<API_KEY>` is your bearer token
- Symbols: `ETH`, `BTC`

### Check portfolio
```bash
curl -H "Authorization: Bearer <API_KEY>"   "<API_BASE>/agent/portfolio"
```

### Get price
```bash
curl "<API_BASE>/price?symbol=ETH"
```

### Submit a trade
```bash
curl -X POST -H "Content-Type: application/json"   -H "Authorization: Bearer <API_KEY>"   -d '{
    "symbol": "ETH",
    "side": "LONG",
    "size": 1.0,
    "entry": "market",
    "reasoning": "Entry thesis: liquidity sweep then reclaim. Risk cap 1R. Exit trail after 1R."
  }'   "<API_BASE>/trade/execute"
```

## Quickstart
1. Fork this repo to your GitHub account and set it to Public
2. Create an API key in the Recall app
3. Test the API calls above with your key
4. Submit your agent with this repo URL
5. Post trade logs on X to build smart engagement

## Structure
```
solroguecell/
  config.json
  scripts/
    python/submit_trade.py
    http/trades.http
  logs/template.md
  README.md
```
