import runner_and_tournament as test
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runer_1 = test.Runner('Усэйн', 10)
        self.runer_2 = test.Runner('Андрей', 9)
        self.runer_3 = test.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def test_tournament_1(self):
        tournament_1 = test.Tournament(90, self.runer_1, self.runer_3)
        result = tournament_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник должен быть последним')
        self.all_results['test_tournament_1'] = result

    def test_tournament_2(self):
        test_tournament_2 = test.Tournament(90, self.runer_2, self.runer_3)
        result = test_tournament_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник должен быть последним')
        self.all_results['test_tournament_2'] = result

    def test_tournament_3(self):
        test_tournament_3 = test.Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = test_tournament_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник должен быть последним')
        self.all_results['test_tournament_3'] = result

    def test_tournament_4(self):
        test_tournament_4 = test.Tournament(6, self.runer_1, self.runer_2, self.runer_3)
        result = test_tournament_4.start()
        self.assertTrue(result[list(result.keys())[1]] == 'Ник', 'Ошибка! Ник должен быть последним')
        self.all_results['test_tournament_4'] = result

    if __name__ == '__main__':
        unittest.main()
