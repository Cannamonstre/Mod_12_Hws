import unittest
from Mod_12_3_1 import RunnerTest, TournamentTest


tourTS = unittest.TestSuite()
tourTS.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
tourTS.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))

runner_ttr = unittest.TextTestRunner(verbosity=2)
runner_ttr.run(tourTS)
