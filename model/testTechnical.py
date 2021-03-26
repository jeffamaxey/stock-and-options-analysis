from model.Technical import Technical
import ray

# initialize multiprocessing
ray.init(ignore_reinit_error=True)

ticker = "aapl"
tech = Technical(ticker)
print(tech.to_string_summary())

