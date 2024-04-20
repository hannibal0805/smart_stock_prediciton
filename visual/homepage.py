import streamlit as st
import pandas as pd
import tushare as ts

# 设置页面标题
st.title('股票历史数据查询')

# 用户输入股票代码和日期范围
stock_code = st.text_input('请输入股票代码（六位数字）:', '600519')
start_date = st.date_input('请选择开始日期:', pd.to_datetime('2010-04-26'))
end_date = st.date_input('请选择结束日期:', pd.to_datetime('2020-04-26'))

# 当用户点击“查询”按钮时执行以下操作
if st.button('查询'):
    # 获取股票历史数据
    df = ts.get_k_data(stock_code, ktype='D', start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    
    # 将数据保存到CSV文件
    datapath = f"./{stock_code}.csv"
    df.to_csv(datapath, index=False)
    
    # 显示数据
    st.write(df)
    
    # 提示数据已保存
    st.success(f'数据已保存到文件: {datapath}')
