#### PENNY TRADING STRATEGY
import time

def write_to_exchange(exchange, obj):
    json.dump(obj, exchange)
    exchange.write("\n")

def trade(exchange_response, team_name):

    if exchange_response['type'] == 'book' and exchange_response['symbol'] == 'bond':
        max_buy_price = interpreter['buy'][0][0]
        min_sell_price = interpreter['sell'][0][0]

        request = {"type": "add", "order_id": N, "symbol": "SYM", "dir": "BUY", "price": N, "size": N}
    	write_to_exchange(exchange, {"type": "hello", "team": team_name.upper()})

def main(response_exchange, team_name):

	trade(response_to_exchange, team_name)


