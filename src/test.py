#!/usr/bin/env python
import os
import unittest

import settings



if __name__ == '__main__':
    loader = unittest.TestLoader()
    start_dir = os.path.join(settings.ROOT_DIR, 'tests')
    test_suites = loader.discover(start_dir)
    runner = unittest.TextTestRunner(verbosity=1)
    
    result = runner.run(unittest.TestSuite(test_suites))
