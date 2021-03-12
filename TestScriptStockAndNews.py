import datetime
import Stock as Stock


begin_time = datetime.datetime.now()
s1 = Stock.Stock("aapl")

print(s1.get_stock_price())
print(s1.get_market_cap())
print(s1.get_stock_company_name())
print(s1.get_volume())
print(s1.get_three_month_volume())
print(s1.get_three_month_volume())
print(s1.get_eps())
print(s1.get_pe_ratio())
print(s1.get_beta())
print(s1.get_open())
print(s1.get_previous_close())
print(s1.get_bid())
print(s1.get_ask())
print(s1.get_fifty_two_week_range())
print(s1.get_daily_range())
print(s1.get_earnings_date())
print(s1.get_one_year_estimate())
print(s1.has_dividend())
print(s1.get_forward_annual_dividend_rate())
print(s1.get_dividend_yield())
print(s1.get_dividend_date())
print(s1.get_ex_dividend())
print(s1.get_news().news_tostring())
print(datetime.datetime.now() - begin_time)




#
# print(si.get_holders("aapl"))
# print(si.get_analysts_info("aapl"))