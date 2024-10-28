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


class TournamentTest(unittest.TestCase):
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

    def test_race_1(self):
        self.tournament = Tournament(90, self.runner_1, self.runner_3)
        self.all_results = self.tournament.start()
        last_runner = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_runner == "Nick")

    def test_race_2(self):
        self.tournament = Tournament(90, self.runner_2, self.runner_3)
        self.all_results = self.tournament.start()
        last_runner = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_runner == "Nick")

    def test_race_3(self):
        self.tournament = Tournament(90, self.runner_1,
                                     self.runner_2, self.runner_3)
        self.all_results = self.tournament.start()
        last_runner = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_runner == "Nick")

    def test_race_speeds(self):
        #  Testing high-speed runners finish before low-speed ones
        self.tournament = Tournament(90, self.runner_1,
                                     self.runner_2, self.runner_3)
        self.all_results = self.tournament.start()
        times = list(self.all_results.keys())
        self.assertTrue(times[0] < times[1] < times[2])


if __name__ == '__main__':
    unittest.main()
