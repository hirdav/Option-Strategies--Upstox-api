`Option-Strategies--Upstox-api`:

```markdown
Option Strategies with Upstox API

Overview
This repository contains Python scripts that implement various options trading strategies using the Upstox API. The strategies are divided into Debit Spreads and Credit Spreads, showcasing different approaches to trading options.

Repository Structure
The repository is organized into the following folders:

- Debit Spread: Contains strategies where the net premium paid is positive.
  - Bear Put Spread: A bearish strategy 
  - Bull Call Spread : A bullish Strategy
- Credit Spread: Contains strategies where the net premium received is positive.
  - Bear Call Spread: A bearish strategy .
  - Bull Put Spread: A bullish strategy .

Folder Details

Debit Spread

Bear Put Spread
- File: `BEAR PUT SPREAD.py`
- Description:  1. Buying an In the money Put option (leg 1) or Higher Premium
                2. Selling an Out of the Money Put option (leg 2) or lower Premiuim

Bull Call Spread
- File: `BULL CALL SPREAD.py`
- Description : 1. Buy 1 ATM call option (leg 1) or Higher Premium 
                2. Sell 1 OTM call option (leg 2) or lower Premiuim


Bull Call Spread Max loss = Net Debit of the Strategy 
Net Debit = Premium Paid for lower strike (higher premium) – Premium Received for higher strike (lower premium) 
Bull Call Spread Max Profit = Spread – Net Debit 


Credit Spread

Bear Call Spread
- `BEAR CALL SPREAD.py`
- Description: Implements the Bear Call Spread strategy using live option chain data. Executes orders based on premium ranges for call options.

Bull Put Spread
- File: `BULL PUT SPREAD.py`
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


Example Usage

To execute the **Bear Put Spread** strategy:

python Debit_Spread/BEAR PUT SPREAD.py
```

To execute the **Bear Call Spread** strategy:
```bash
python Credit_Spread/BEAR CALL SPREAD.py
```

## Notes
- Ensure that valid Upstox API credentials are configured before running the scripts.
- Adjust the parameters and logic according to your trading needs and preferences.
Read Api Documentation for any api related issue :
## 📚 Documentation
- [Upstox API Documentation](https://upstox.com/developer/api/v2/)