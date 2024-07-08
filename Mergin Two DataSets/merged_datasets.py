df = pd.merge(rossman_df, store_df, how='left', on='Store')
df.head()
df.shape
