import runner_with_ex  # импорт модуля, где находится тестируемый класс
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):  # тестовый класс
    is_frozen = False  # атрибут заморозки тестов

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            obj1 = runner_with_ex.Runner('cup', speed=-5)
            for i in range(10):
                obj1.walk()
            self.assertEqual(obj1.distance, 50)
            logging.info('test_walk выполнен успешно')
        except ValueError:
            logging.warning('test_walk / Неверная скорость для runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            obj2 = runner_with_ex.Runner(15)
            for i in range(10):
                obj2.run()
            self.assertEqual(obj2.distance, 100)
            logging.info('test_run выполнен успешно')
        except TypeError:
            logging.warning('test_run / Неверный тип данных для объекта runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        try:
            obj3 = runner_with_ex.Runner('milk')
            obj4 = runner_with_ex.Runner('beer')
            for i in range(10):
                obj3.walk()
            for i in range(10):
                obj4.run()
            self.assertNotEqual(obj3.distance, obj4.distance)
            logging.info('test_challenge / Всё верно, бегун быстрее гуляки')
        except (TypeError, ValueError):
            logging.warning('test_challenge / Что-то ты накосорезил, братан )))')


if __name__ == '__main__':
    unittest.main()
