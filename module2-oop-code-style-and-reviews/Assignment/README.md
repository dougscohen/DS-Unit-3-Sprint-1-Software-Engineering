
# dc_lambdata (Assignment #2)

## Installation 

```sh
pip install _________________ # get address from pypi and update this line
```

## Usage

```py
from dc_lambdate.mod1 import full_state_name

df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
full_df = full_state_name(df)
print(full_df.head())
```

```py
from dc_lambdata.mod2 import split_date

df = pandas.DataFrame({"date": ["01/02/2018", "03/17/2004", "03/30/1459", "10/11/1260"]})
full_df = split_date(df)
print(full_df.head())
```