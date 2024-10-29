import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        time = 0  # time var to track the time from start of a race
        while self.participants:
            time += 1  # Every iteration increases time var
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[time] = participant
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Tests are frozen')
    def test_walk(self):
        mr_runner_1 = Runner('Alex')

        for _ in range(10):
            mr_runner_1.walk()

        self.assertEqual(mr_runner_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Tests are frozen')
    def test_run(self):
        mr_runner_2 = Runner('Jane')

        for _ in range(10):
            mr_runner_2.run()

        self.assertEqual(mr_runner_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Tests are frozen')
    def test_challenge(self):
        mr_runner_3, mr_runner_4 = Runner('Killian'), Runner('Anita')

        for _ in range(10):
            mr_runner_3.run()

        for _ in range(10):
            mr_runner_4.walk()

        self.assertNotEqual(mr_runner_3.distance, mr_runner_4.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Usain', speed=10)
        self.runner_2 = Runner('Andrew', speed=9)
        self.runner_3 = Runner('Nick', speed=3)

    @classmethod
    def tearDownClass(cls):
        for result, runner in cls.all_results.items():
            print(f'{result}: {runner}')

    @unittest.skipIf(is_frozen, 'Tests are frozen')
    def test_race_1(self):
        self.tournament = Tournament(90, self.runner_1, self.runner_3)
        self.all_results = self.tournament.start()
        last_runner = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_runner == "Nick")

    @unittest.skipIf(is_frozen, 'Tests are frozen')
    def test_race_2(self):
        self.tournament = Tournament(90, self.runner_2, self.runner_3)
        self.all_results = self.tournament.start()
        last_runner = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_runner == "Nick")

    @unittest.skipIf(is_frozen, 'Tests are frozen')
    def test_race_3(self):
        self.tournament = Tournament(90, self.runner_1,
                                     self.runner_2, self.runner_3)
        self.all_results = self.tournament.start()
        last_runner = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_runner == "Nick")

    @unittest.skipIf(is_frozen, 'Tests are frozen')
    def test_race_speeds(self):
        #  Testing high-speed runners finish before low-speed ones
        self.tournament = Tournament(90, self.runner_1,
                                     self.runner_2, self.runner_3)
        self.all_results = self.tournament.start()
        times = list(self.all_results.keys())
        self.assertTrue(times[0] < times[1] < times[2])


if __name__ == '__main__':
    unittest.main()
