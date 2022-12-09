#!/usr/bin/python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from IPython.core.interactiveshell import InteractiveShell
import openpyxl

# InteractiveShell.ast_node_interactivity = "all"
# pd.set_option('max_column', 1000)
# pd.set_option('max_row', 30)
pd.options.display.max_rows = 30
pd.options.display.max_columns = 1000
pd.set_option("display.float_format", lambda x: '%.5f' % x)
# %matplotlib inline
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
# %config InlineBackend.figure_format = 'svg'

df6 = pd.DataFrame({
    'code': [1, 2, 2, 4, 5, 5, 6],
    'name': ['a', 'a', 'b', 'c', 'd', 'd', 'e'],
    'freq': [2, 3, 4, 2, 1, 4, 5],
    'value': [12, 14, 17, 20, 25, 26, 30]
})

print(df6.iloc[:, 1:3])
