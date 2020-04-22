#Author: Lana Chen
#Update: April 22th, 2020
import pandas as pd
l_name=['null','Lisa','Rose','Jennie','Jisoo','Wendy']#yourself
df=pd.DataFrame({'Name':l_name})
df.to_csv('employee_table.csv')