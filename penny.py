#### PENNY TRADING STRATEGY
import random
import strategy

class Penny(strategy.Strategy):

	def trade(self):
		while True:
			response_exchange = self.read_from_exchange()
			self.penny_trade(response_exchange)

	def penny_trade(self, exchange_response):

	    if exchange_response['type'] == 'book':
	        max_buy_price = exchange_response['buy'][0][0]
	        min_sell_price = exchange_response['sell'][0][0]

	        try: 
		        self.order_id += 1
		        buy_request = {"type": "add", "order_id": self.order_id, "symbol": "BOND", "dir": "BUY", "price": max_buy_price, "size": 5}
		        self.write_to_exchange(buy_request)
		        print(self.read_from_exchange())

		        self.order_id += 1
		        sell_request = {"type": "add", "order_id": self.order_id, "symbol": "BOND", "dir": "SELL", "price": min_sell_price, "size": 5}
		    	self.write_to_exchange(sell_request)
		    	print(self.read_from_exchange())
		    
		    except: 
		    	continue




