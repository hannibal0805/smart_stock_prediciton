import tushare as ts
import warnings
warnings.filterwarnings("ignore")
stock = '600519'
start_date = '2010-04-26'
end_date = '2020-04-26'
df1 = ts.get_k_data(stock, ktype='D', start=start_date, end=end_date)
# 更改第一个参数：六位股票代码，下载需要的股票历史数据


datapath1 = "./SH600519.csv"

df1.to_csv(datapath1)

