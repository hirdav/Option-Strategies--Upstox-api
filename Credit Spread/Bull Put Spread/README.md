`README.md`

```markdown
# Bear Put Spread Strategy Automation

## Overview
This project automates the **Bear Put Spread Strategy** using live option chain data fetched from the **Upstox API**. The strategy is designed to be **strike independent** and **premium dependent**, making decisions based on the option premiums rather than specific strikes.

### Key Features:
- **WebSocket Connection**: Establishes a WebSocket connection to fetch live option chain data.
- **Option Chain Fetching**: Continuously retrieves option chain data for a specified instrument (e.g., Nifty Bank) and expiry date.
- **Automated Order Placement**: Places market and stop-loss orders based on premium ranges.
- **Bear Put Spread Strategy**: Executes the Bear Put Spread strategy by placing buy and sell orders in two legs.

## Requirements
To run this project, ensure you have the following dependencies installed:
- `requests`: For making API requests.
- `websockets`: For establishing WebSocket connections.
- `asyncio`: For asynchronous event handling.
- `upstox_client`: For connecting to the Upstox API.
- `ssl`: For secure WebSocket connections.

Install the dependencies via `pip`:
```bash
pip install requests websockets asyncio ssl upstox-client
```

## Setup

### 1. Access Token
Replace the placeholder `access_token` with your Upstox access token:
```python
access_token = 'your_actual_access_token'
```

### 2. Instrument and Expiry Details
Modify the `instrument_key` and `expiry_date` to track the instrument and expiry date you want:
```python
params = {
    'instrument_key': 'NSE_INDEX|Nifty Bank',
    'expiry_date': '2024-09-18'  # Adjust as needed
}
```

## How It Works

### 1. Market Data Authorization
The script authorizes the WebSocket connection using the Upstox API:
```python
api_instance = upstox_client.WebsocketApi(upstox_client.ApiClient(configuration))
api_response = api_instance.get_market_data_feed_authorize(api_version)
```

### 2. Fetching Live Option Chain Data
The `fetch_market_data` function connects to Upstox WebSocket to fetch live option chain data. The data is analyzed based on the premium (price), not the strike price:
```python
url = "https://api.upstox.com/v2/option/chain"
response = requests.get(url, headers=headers, params=params)
```

### 3. Order Placement Logic
- The script checks if the **Last Traded Price (LTP)** of put options falls between specific ranges for executing the Bear Put Spread strategy:
  - **First Leg**: Places a BUY order if the premium falls between 110 and 150.
  - **Second Leg**: Places a SELL order if the premium falls between 240 and 280.
  
- Stop-loss orders can be automatically placed for each leg for risk management.

Order logic example:
```python
if ltp and 110 <= ltp <= 150:
    instrument_token = put_options['instrument_key']
    await place_order(instrument_token, 'BUY', 'MARKET', 15, 0)
```

### 4. Bear Put Spread Strategy
- The **Bear Put Spread** strategy is executed when both legs of the spread are successfully placed.
- You can adjust the premium conditions, quantities, and stop-loss logic as needed.

## Running the Script
To run the script, execute it using Python:
```bash
python script_name.py
```
This will:
- Establish a WebSocket connection.
- Fetch live market data.
- Place orders automatically based on the defined Bear Put Spread strategy.

## Notes
- Ensure valid Upstox API credentials and tokens are set up before running the script.
- Modify the LTP conditions, instrument parameters, and order logic according to your strategy.
```

