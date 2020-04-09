
import unittest

import pandas as pd

from dc_lambdata.mod2 import split_date

class TestMod2(unittest.TestCase):

    # Individual test case, name of fucntion needs to be "test_%"
    def test_split_date(self):
        '''test to confirm that a dataframe with one column "date" will be
        converted to 4 columns ('date', 'year', 'month', 'day') using the
        split_date() function.
        '''
        df = pd.DataFrame({"date": ["01/02/2018", "03/17/2004", "03/31/1990",
                                    "10/24/1960"]})
        self.assertEqual(df.columns.tolist(), ['date'])
        full_df = split_date(df)
        self.assertEqual(full_df.columns.tolist(), ['date', 'year', 'month',
                                                    'day'])

        # test the length of the dataframe
        self.assertEqual(len(full_df['year']), 4)


if __name__ == '__main__':
    unittest.main()