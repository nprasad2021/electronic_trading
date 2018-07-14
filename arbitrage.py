import strategy

class Arbitrage(strategy.Strategy):

	def __init__(self):
		strategy.Strategy.__init__()
		self.trading_options = ['BABA', 'BABZ']
		self.momentum_avg = 0
		self.timestep = 0
		

	def trade(self):

		while True:
			response_exchange = self.read_from_exchange()
			self.arbi_trade(response_exchange)

	def arbi_trade(self, response_exchange):
		if response_exchange['type'] == 'book':
			if response_exchange['symbol'] in self.trading_options:










