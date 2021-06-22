import pandas as pd

df = pd.read_html('https://www.basketball-reference.com/boxscores/202106200PHO.html')


#print(df[8])

df[8].to_csv('suns6-20-21.csv')
