#### PENNY TRADING STRATEGY
import time

def write_to_exchange(exchange, obj):
    json.dump(obj, exchange)
    exchange.write("\n")

def trade(exchange_response, team_name, order_id):

    if exchange_response['type'] == 'book' and exchange_response['symbol'] == 'BOND':
        max_buy_price = interpreter['buy'][0][0]
        min_sell_price = interpreter['sell'][0][0]

        buy_request = {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": max_buy_price, "size": 5}
        sell_request = 
    	write_to_exchange(exchange, request)




def main(response_exchange, team_name, order_id):
	trade(response_to_exchange, team_name, order_id)


