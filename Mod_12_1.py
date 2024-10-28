import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        mr_runner_1 = Runner('Alex')

        for _ in range(10):
            mr_runner_1.walk()

        self.assertEqual(mr_runner_1.distance, 50)

    def test_run(self):
        mr_runner_2 = Runner('Jane')

        for _ in range(10):
            mr_runner_2.run()

        self.assertEqual(mr_runner_2.distance, 100)

    def test_challenge(self):
        mr_runner_3, mr_runner_4 = Runner('Killian'), Runner('Anita')

        for _ in range(10):
            mr_runner_3.run()

        for _ in range(10):
            mr_runner_4.walk()

        self.assertNotEqual(mr_runner_3.distance, mr_runner_4.distance)


if __name__ == '__main__':
    unittest.main()
