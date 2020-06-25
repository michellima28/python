import pandas as pd
df = pd.read_csv('/home/michel/github/python/csv_to_json/sample_products.csv')
df.to_json('/home/michel/github/python/csv_to_json/sample_products.json')