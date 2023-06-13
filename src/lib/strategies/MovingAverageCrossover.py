from backtesting.lib import crossover
from backtesting import Strategy
from ..indicators.Average import SimpleMovingAverage as SMA


class MovingAverageCrossoverStrategy(Strategy):
    def init(self):
        price = self.data.Close

        self.short_ma = self.I(SMA, price, 10)

        self.long_ma = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.short_ma, self.long_ma):
            self.buy()
        elif crossover(self.long_ma, self.short_ma):
            self.sell()
