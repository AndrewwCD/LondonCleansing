import pandas as pd
import numpy as np

data = pd.read_csv("BL-Flickr-Images-Book-truncated50.csv")
london_filtered = data[["Place of Publication","Date of Publication","Publisher","Title","Author"]]

london_filtered = london_filtered[london_filtered["Place of Publication"].str.contains(
                    "london", case = False, na = False
                    )]
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
print(london_filtered)
