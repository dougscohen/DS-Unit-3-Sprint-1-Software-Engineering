
# dc_lambdata\mod1.py

import pandas

def full_state_name(my_df):
    """
    Creates a new column called "state_name" which has the corresponding state
    name.

    Params my_df (pandas.DataFrame) with with column called "abbrev" which has
    state abbrevs

    See: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
    """
    df = my_df.copy()
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
        }
        
    print(type(df["abbrev"])) #> <class 'pandas.core.series.Series'>
    df["state_name"] = df["abbrev"].map(states)
    return df



if __name__ == "__main__":

    df1 = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
    full_df1 = full_state_name(df1)
    print(full_df1.head())
    
    df2 = pandas.DataFrame({"abbrev": ["GA", "NY", "NC", "WY"]})
    full_df2 = full_state_name(df2)
    print(full_df2.head())