# to creat a dataframe from a csv file, we can use the following code:
df = pd.DataFrame()

# example:
import pandas as pd
df = pd.DataFrame({
       'Column1': [1, 2, 3, 4, 5],
       'Column2': ['A', 'B', 'C', 'D', 'E'],
       'Column3': [True, False, True, False, True]})




# 1. Exporting to a CSV File:
# CSV files are versatile for tabular data. Use the following code to export a DataFrame to CSV:

df.to_csv('filename.csv', index=False) #index=False prevents writing the DataFrame index to the file.
from google.colab import files #Should import files first so that I can do download
files.download('filename.csv')


# 2. Writing to a JSON File:
# JSON is ideal for nested data structures. To export data in JSON format, use:

df.to_json('filename.json')