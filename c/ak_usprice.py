import akshare as ak

stock_us_spot_em_df = ak.stock_us_spot_em()
#print(stock_us_spot_em_df)

e = stock_us_spot_em_df[stock_us_spot_em_df['代码'].str[4:6] == 'WO']
#print(e)

stock_us_hist_min_em_df = ak.stock_us_hist_min_em(symbol="106.WOLF")
#print(stock_us_hist_min_em_df.tail(20))

df = stock_us_hist_min_em_df[stock_us_hist_min_em_df['时间'] > '2024-10-16 21:30:00']
print(df.head())
and_operator = df[(df['最高'] > 16.0) & (df['最低'] < 15.5)]
print(and_operator.head()[['时间', '最新价']])
print(and_operator.shape)

and_operator1 = df[(df['最高'] > 16.0)]
print(and_operator1.head()[['时间', '最高']])
print(and_operator1.shape)
a1=and_operator1.loc[:, ['时间', '最高']]
a1.rename(columns = {'最高':'价格'}, inplace = True)
and_operator2 = df[(df['最低'] < 15.5)]
print(and_operator2.head()[['时间', '最低']])
print(and_operator2.shape)
a2=and_operator2.loc[:, ['时间', '最低']]
a2.rename(columns = {'最低':'价格'}, inplace = True)

import pandas as pd
result = pd.concat([a1, a2])
df_sorted_ascending = result.sort_values(by='时间', ascending=True)
gfg = (df_sorted_ascending[['时间', '价格']])

#print(gfg.to_markdown())

#import sys
#sys.exit("no plot")
import matplotlib.pyplot as plt

plt.figure()

plt.plot(gfg['时间'], gfg['价格'])
plt.gcf().autofmt_xdate()

plt.title('Prices For the Period in One Day (HK)')
 
plt.show()
