import logging
import unittest

logger = logging.getLogger('Mod_12_4')
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('Mod_12_4.log', mode='w', encoding='UTF-8')
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.info('Logging setup completed')


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Name can only be a string, now {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f"Speed can't be negative, now {speed}")

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Tests are frozen')
    def test_walk(self):
        try:
            mr_runner_1 = Runner('Alex', -4)

            for _ in range(10):
                mr_runner_1.walk()

            self.assertEqual(mr_runner_1.distance, 50)
            logger.info('test_walk completed successfully')
        except ValueError:
            logger.warning('Incorrect speed for Runner object', exc_info=True)

    @unittest.skipIf(is_frozen, 'Tests are frozen')
    def test_run(self):
        try:
            mr_runner_2 = Runner(444)

            for _ in range(10):
                mr_runner_2.run()

            self.assertEqual(mr_runner_2.distance, 100)
            logger.info('test_run completed successfully')
        except TypeError:
            logger.warning('Incorrect type for Runner object', exc_info=True)

    @unittest.skipIf(is_frozen, 'Tests are frozen')
    def test_challenge(self):
        mr_runner_3, mr_runner_4 = Runner('Killian'), Runner('Anita')

        for _ in range(10):
            mr_runner_3.run()

        for _ in range(10):
            mr_runner_4.walk()

        self.assertNotEqual(mr_runner_3.distance, mr_runner_4.distance)


if __name__ == '__main__':
    unittest.main()
