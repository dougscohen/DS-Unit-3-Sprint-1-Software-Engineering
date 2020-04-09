
import unittest

import pandas

from dc_lambdata.mod1 import full_state_name

class TestMod1(unittest.TestCase):

    # Individual test case, name of fucntion needs to be "test_%"
    def test_name_conversion(self):
        
        df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
        self.assertEqual(df.columns.tolist(), ['abbrev'])
        df = full_state_name(df)
        self.assertEqual(df.columns.tolist(), ['abbrev', 'state_name'])

        # TODO: consider also testing the actual values (perhaps the first row)


if __name__ == '__main__':
    unittest.main()