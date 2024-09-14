`Option-Strategies--Upstox-api`:

```markdown
Option Strategies with Upstox API

Overview
This repository contains Python scripts that implement various options trading strategies using the Upstox API. The strategies are divided into Debit Spreads and Credit Spreads, showcasing different approaches to trading options.

Repository Structure
The repository is organized into the following folders:

- Debit Spread: Contains strategies where the net premium paid is positive.
  - Bear Put Spread: A bearish strategy involving buying and selling put options.
  - Call Spread: Details of different call spread strategies.
  
- Credit Spread: Contains strategies where the net premium received is positive.
  - Bear Call Spread: A bearish strategy involving buying and selling call options.
  - Bull Put Spread: A bullish strategy involving buying and selling put options.

Folder Details

Debit Spread

Bear Put Spread
- File: `bear_put_spread.py`
- Description: Implements the Bear Put Spread strategy using live option chain data. Executes orders based on premium ranges for put options.

Call Spread
- File: `call_spread.py`
- Description : Implements various call spread strategies using live option chain data.

Credit Spread

Bear Call Spread
- bear_call_spread.py
- Description: Implements the Bear Call Spread strategy using live option chain data. Executes orders based on premium ranges for call options.

Bull Put Spread
- File: `bull_put_spread.py`
- Description: Implements the Bull Put Spread strategy using live option chain data. Executes orders based on premium ranges for put options.

Getting Started

Prerequisites
Ensure you have the following Python packages installed:
- `requests`
- `websockets`
- `asyncio`
- `ssl`
- `upstox_client`

Install the dependencies using `pip`:
pip install requests websockets asyncio ssl upstox-client
```

Setup

1. Access Token: Replace the placeholder `access_token` with your Upstox API access token in each script.
2. Instrument and Expiry Details: Modify the `instrument_key` and `expiry_date` parameters in the scripts to track the desired options.

Running the Scripts
To run any of the strategy scripts, execute the following command in your terminal:

python path/to/strategy_script.py
```

Replace `path/to/strategy_script.py` with the path to the specific strategy script you want to run.

Example Usage

To execute the **Bear Put Spread** strategy:

python Debit_Spread/bear_put_spread.py
```

To execute the **Bear Call Spread** strategy:
```bash
python Credit_Spread/bear_call_spread.py
```

## Notes
- Ensure that valid Upstox API credentials are configured before running the scripts.
- Adjust the parameters and logic according to your trading needs and preferences.