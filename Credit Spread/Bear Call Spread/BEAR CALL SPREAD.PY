

import asyncio
import json
import ssl
import upstox_client
import websockets
import requests

access_token='eyJ0eXAiOiJiOiUzZGY5NWY3N2MzNzA2OTZiNjIxN2EiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaWF0IjoxNzI2MjA5OTQxLCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3MjYyNjQ4MDB9.GQSpRPSzG9hYwuSzwx6t-E-qoIijzb219DOpgoRFUDo'


# Define a dictionary to store option contract details
option_contracts = {}

def get_market_data_feed_authorize(api_version, configuration):
    """Get authorization for market data feed."""
    api_instance = upstox_client.WebsocketApi(
        upstox_client.ApiClient(configuration))
    api_response = api_instance.get_market_data_feed_authorize(api_version)
    return api_response

async def place_order(instrument_token, transaction_type, order_type, quantity, price, trigger_price=None):
    """Place an order."""
    url = "https://api.upstox.com/v2/order/place"
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        "quantity": quantity,
        "product": "D",
        "validity": "DAY",
        "price": price,
        "tag": "string",
        "instrument_token": instrument_token,
        "order_type": order_type,
        "transaction_type": transaction_type,
        "disclosed_quantity": 0,
        "trigger_price": trigger_price if trigger_price else 0,
        "is_amo": False
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print("Failed to place order. Status code:", response.status_code)
        return None

async def fetch_market_data():
    """Fetch market data using WebSocket and manage orders."""
    # Create default SSL context
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    # Configure OAuth2 access token for authorization
    configuration = upstox_client.Configuration()
    configuration.access_token = access_token
    # Get market data feed authorization
    response = get_market_data_feed_authorize(api_version='2.0', configuration=configuration)
    async with websockets.connect(response.data.authorized_redirect_uri, ssl=ssl_context) as websocket:
        print('Connection established [BEAR CALL SPREAD]')
        await asyncio.sleep(2)  # Wait for 1 second
        # Fetch live option chain data using the API
        url = "https://api.upstox.com/v2/option/chain"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {access_token}',  # Replace with your access token
        }
        params = {
            'instrument_key': 'NSE_INDEX|Nifty Bank',
            'expiry_date': '2024-09-18'  # Replace with the desired expiry date
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = json.loads(response.text)
            option_chain = data['data']
            # Print the option chain data for debugging
            print("Option Chain Data:")
            print(json.dumps(option_chain, indent=4))
            # Check if the option chain data is in the expected format
            if isinstance(option_chain, list) and len(option_chain) > 0:
                for option in option_chain:
                    # Check if call options exist at the given range
                    if 'call_options' in option:
                        call_options = option['call_options']
                        if isinstance(call_options, dict) and 'market_data' in call_options:
                            market_data = call_options['market_data']
                            ltp = market_data.get('ltp')
                            if ltp and 110 <= ltp <= 150:
                                # Place SELL [FIRST LEG] order for the call option
                                instrument_token = call_options['instrument_key']
                                order_response = await place_order(instrument_token, 'BUY', 'MARKET', 15, 0)
                                if order_response:
                                    print("SELL order placed for call option[FIRST LEG]:", order_response)
                                    # Place stop-loss order for the executed call option
                                    sl_price = ltp + 30  # Set stop-loss price 30 points below entry price IF THERE IS ANY NEED FOR STOPLOSS
                                    sl_order_response = await place_order(instrument_token, 'SELL', 'SL', 15, sl_price, trigger_price=sl_price-1)
                                    if sl_order_response:
                                        print("Stop-loss order placed for call option[FIRST LEG]:", sl_order_response)
                            
                    # Check if call  options exist at the given range
                    if 'call_options' in option:
                        call_options = option['call_options']
                        if isinstance(call_options, dict) and 'market_data' in call_options:
                            market_data = call_options['market_data']
                            ltp = market_data.get('ltp')
                            if ltp and  340<= ltp <= 400:
                                # Place buy order for the CALL option [SECOND LEG]
                                instrument_token = call_options['instrument_key']
                                order_response = await place_order(instrument_token, 'SELL', 'MARKET', 15, 0)
                                if order_response:
                                    print("BUY order placed for call option[SECOND LEG]:", order_response)
                                    # Place stop-loss order for the executed put option
                                    sl_price = ltp + 30  # Set stop-loss price 30 points ABOVE entry price [use stoploss if you need any stoploss with this strategy []
                                    sl_order_response = await place_order(instrument_token, 'BUY', 'SL', 15, sl_price, trigger_price=sl_price+1)
                                    if sl_order_response:
                                        print("Stop-loss order placed for call option[SECOND LEG]:", sl_order_response)
                            
        else:
            print("Failed to fetch option chain data. Status code:", response.status_code)

# Run the fetch_market_data function in an asyncio event loop
asyncio.run(fetch_market_data())
