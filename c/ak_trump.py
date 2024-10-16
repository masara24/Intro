import akshare as ak

stock_concept_cons_futu_df = ak.stock_concept_cons_futu(symbol="特朗普概念股")
print(stock_concept_cons_futu_df)

for i in stock_concept_cons_futu_df['代码']:
    print(i)
    usstock = i
    
    try:
        stock_us_hist_min_em_df = ak.stock_us_hist_min_em(symbol='105.'+usstock, start_date='20241006', end_date='20241010')
    except:
        stock_us_hist_min_em_df = ak.stock_us_hist_min_em(symbol='106.'+usstock, start_date='20241006', end_date='20241010')
    finally:
        print(stock_us_hist_min_em_df.tail())
        stock_us_daily_df = ak.stock_us_daily(symbol=usstock, adjust="")
        print(stock_us_daily_df[-2:])
