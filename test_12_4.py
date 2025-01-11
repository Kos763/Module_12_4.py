from main import Runner
import logging
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("Вася", -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info("'test_walk' выполнен успешно")
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner\n{e}")

    def test_run(self):
        try:
            runner = Runner(0)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info("'test_run' выполнен успешно")
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner\n{e}")

    def test_challenge(self):
        runner_1 = Runner('Runner1')
        runner_2 = Runner('Runner2')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)
        logging.info("'test_challenge' выполнен успешно")


logging.basicConfig(level=logging.INFO, filemode='w',
                    filename='runner_tests.log', encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')
