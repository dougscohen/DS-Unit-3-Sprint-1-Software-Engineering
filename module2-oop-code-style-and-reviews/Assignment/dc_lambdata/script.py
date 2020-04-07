
# dc_lambdata\scipt.py

import pandas as pd

from dc_lambdata.mod1 import full_state_name
from dc_lambdata.mod2 import split_date

df3 = pd.DataFrame({"abbrev": ["TN", "DC", "MI", "AL", "CO", "SC"]})
full_df3 = full_state_name(df3)
print(full_df3.head())

print("----------")

df4 = pd.DataFrame({"date": ["01/21/2018", "11/17/2004", "03/31/1995", "10/14/1960"]})
full_df4 = split_date(df4)
print(full_df4.head())