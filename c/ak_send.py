from datetime import date, datetime, timedelta

#tday = date.today() # date
tday=datetime.now()
#fday = (datetime.now() - timedelta(days=5, hours=0)) #5 days, or 1 day
fday = (datetime.now() - timedelta(days=0, hours=24)) #5 days, or 1 day

#fiveday = fday.date() # date
et=str(tday)
st=str(fday)
et=et.split('.')[0]
st=st.split('.')[0]
print(st, "->", et)

import akshare as ak

stock = "HK"; print(stock)
stock_hk_spot_em_df = ak.stock_hk_spot_em()
#print(stock_hk_spot_em_df['名称'])
print(stock_hk_spot_em_df.columns)
print(stock_hk_spot_em_df[['名称', '最新价', '涨跌幅', '成交额', '代码']])

df=stock_hk_spot_em_df
# 按照'最高'列降序重新排序
df_sorted_ascending = df.sort_values(by='最高', ascending=False)
 
# 按照'最低'列升序重新排序
df_sorted_descending = df.sort_values(by='最低', ascending=True)
 
# 按照多列进行排序，先按'涨跌额'升序，然后按'最新价'降序
df_sorted_multi = df.sort_values(by=['涨跌额', '最新价'], ascending=[True, False])
 
print(df_sorted_ascending)
print(df_sorted_descending)
print(df_sorted_multi)

stock = stock_hk_spot_em_df[:1]['代码']; print(stock) #period 1 means 1 min
stock = str(stock).split()[1]
stock_hk_hist_min_em_df = ak.stock_hk_hist_min_em(symbol=stock, period='1', adjust='hfq', start_date=st, end_date=et)
print(stock_hk_hist_min_em_df)

stock = "US"; print(stock)
stock_us_spot_em_df = ak.stock_us_spot_em()
print(stock_us_spot_em_df.columns)

print(stock_us_spot_em_df[['名称', '最新价', '涨跌幅', '成交额', '代码']])

df=stock_us_spot_em_df
# 按照'最高'列降序重新排序
df_sorted_ascending = df.sort_values(by='最高价', ascending=False)
 
# 按照'最低'列升序重新排序
df_sorted_descending = df.sort_values(by='最低价', ascending=True)
 
# 按照多列进行排序，先按'涨跌额'升序，然后按'换手率'降序
df_sorted_multi = df.sort_values(by=['涨跌额', '换手率'], ascending=[True, False])
 
print(df_sorted_ascending)
print(df_sorted_descending)
print(df_sorted_multi)

stock = stock_us_spot_em_df[:1]['代码']; print(stock) #1 min
stock = str(stock).split()[1]

stock_us_hist_min_em_df = ak.stock_us_hist_min_em(symbol=stock, start_date=st, end_date=et)
print(stock_us_hist_min_em_df)
