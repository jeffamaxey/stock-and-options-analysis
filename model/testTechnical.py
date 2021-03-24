import Technical as Technical
import ray

# initialize multiprocessing
ray.init(ignore_reinit_error=True)

stock = Technical.Technical("aapl")
print(stock.get_rsi())
print(stock.get_mass_index())
print(stock.get_pivot_fib())
print(stock.get_macd())
print( stock.get_simple_moving_average_range_30_10())