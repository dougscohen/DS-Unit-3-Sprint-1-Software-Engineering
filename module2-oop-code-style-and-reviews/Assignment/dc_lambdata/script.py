
# dc_lambdata\scipt.py

import pandas as pd

from dc_lambdata.mod1 import full_state_name

df3 = pd.DataFrame({"abbrev": ["TN", "DC", "MI", "AL", "CO", "SC"]})
full_df3 = full_state_name(df3)
print(full_df3.head())