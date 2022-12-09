#!/usr/bin/python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.interactiveshell import InteractiveShell
import openpyxl
InteractiveShell.ast_node_interactivity = "all"
pd.set_option('max_columns',1000)
pd.set_option('max_irow',30)
pd.set_option("display.float_format", lambda x: '%.5f' % x)
# %matplotlib inline
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
# %config InlineBackend.figure_format = 'svg'

