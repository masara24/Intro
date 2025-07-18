import akshare as ak

fund_etf_spot_em_df = ak.fund_etf_spot_em()
print(fund_etf_spot_em_df.columns)

df=fund_etf_spot_em_df
df_sorted_ascending = df.sort_values(by='涨跌幅', ascending=False)
fetf = (df_sorted_ascending[['代码', '名称', '最新价', 'IOPV实时估值', '涨跌幅']]).tail()

gfg = fetf.to_markdown(
        numalign="left",
        stralign="left",
    )

print(gfg)

fund_lof_spot_em_df = ak.fund_lof_spot_em()
print(fund_lof_spot_em_df.columns)

df=fund_lof_spot_em_df

no_nans = df[~df['涨跌幅'].isna()]

df_sorted_ascending = no_nans.sort_values(by='涨跌幅', ascending=True)

flof = (df_sorted_ascending[['代码', '名称', '最新价', '换手率', '涨跌幅']]).tail()

gfg = flof.to_markdown(
        numalign="left",
        stralign="left",
    )

print(gfg)

fund = "160644"
print(fund)
fund_open_fund_info_em_df = ak.fund_open_fund_info_em(symbol=fund, indicator="单位净值走势")
#print(fund_open_fund_info_em_df)
df1 = fund_open_fund_info_em_df

fund_open_fund_info_em_df = ak.fund_open_fund_info_em(symbol=fund, indicator="累计净值走势")
#print(fund_open_fund_info_em_df)
df2 = fund_open_fund_info_em_df
import pandas as pd
result = pd.merge(df1, df2, on='净值日期')
print(result.tail(30).to_markdown())
print(type(result.loc[2]['净值日期']))

from datetime import date
a = date(2024, 6, 30)
print(a)

print(result[result['净值日期'] == a]) #buy

b = date(2024, 6, 30)
c = date(2024, 7, 30)

date_filter = result[(result['净值日期'] >= b) & (result['净值日期'] < c)]
print(date_filter)
