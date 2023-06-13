import pandas as pd
s = {'một' : pd.Series([1., 2., 3., 5.,], index=['a','b', 'c', 'e'])
	'hai' : pd.Series([1., 2., 3., 4.,], index=['a', 'b', 'c', 'd'])
	'ba' : pd.Series ([9., -1., 6.5, -46.], index=['a', 'b', 'c', 'd'])}
	df = pd.DataFrame(s)
	#chọn cột ba
	df_ba = df['ba']
	print(df_ba)