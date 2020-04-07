
# dc_lambdata\mod2.py

import pandas as pd

def split_date(dataframe):
    """
    Creates 3 new columns with year, month, and day

    Params: dataframe with column called "date" which has the date in the
    format "MM/DD/YYYY"
    """
    
    df = dataframe.copy()
    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day

    return df


if __name__ == "__main__":

    df3 = pd.DataFrame({"date": ["01/02/2018", "03/17/2004", "03/31/1990", "10/24/1960"]})
    full_df3 = split_date(df3)
    print(full_df3.head())