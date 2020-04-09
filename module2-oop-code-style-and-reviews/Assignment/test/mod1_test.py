
# THIS IS NOT COMPLETE

import unittest

import pandas

from dc_lambdata.mod1 import full_state_name

class TestMod1(unittest.TestCase):

    # Individual test case
    def test_name_conversion(self):
        # self.assertEqual()
        df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
        # full_df = full_state_name(df)
        # print(full_df.head())
        self.assertEqual(df.columns.tolist(), ['abbrev'])
        full_state_name(df)
        self.assertEqual(df.columns.tolist(), ['abbrev', 'state_name'])

        # TODO: consider also testing the actual values (perhaps the first row)


if __name__ == '__main__':
    unittest.main()