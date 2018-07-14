import strategy

class Arbitrage(strategy.Strategy):

	def __init__(self):
		strategy.Strategy.__init__()
		self.trading_options = ['BABA', 'BABZ']

	def trade(self):

		while True:
			response_exchange = self.read_from_exchange()
			self.arbi_trade(response_exchange)

	def arbi_trade(self, response_exchange):
		response_exchange







