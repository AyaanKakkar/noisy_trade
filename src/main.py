import warnings

warnings.filterwarnings("ignore")

from backtesting import Backtest, Strategy
from lib.utils import get_data
from lib.strategies.MovingAverageCrossover import MovingAverageCrossoverStrategy
from backtesting.test import GOOG
import time

strategy = MovingAverageCrossoverStrategy

data = get_data("^NSEI")

bt = Backtest(data, strategy, exclusive_orders=True)
stats = bt.run()

print(stats)

date_time = time.strftime("%Y%m%d-%H%M%S")
filename = "results/" + strategy.__name__ + "_" + date_time

bt.plot(filename=filename)
