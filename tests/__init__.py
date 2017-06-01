import os
import unittest

import settings


class TestBase(unittest.TestCase):
    pass


def run():
    loader = unittest.TestLoader()
    start_dir = os.path.join(settings.ROOT_DIR, '..')
    test_suites.append(loader.discover(start_dir))
    runner = unittest.TextTestRunner(verbosity=verbosity)
    
    result = runner.run(unittest.TestSuite(test_suites))
