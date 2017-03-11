'''
binarySearchのテスト
'''
import unittest
import March2017.Practice6
class BinarySearchTest(unittest.TestCase):
    def test_normal_case(self):
        # 最初のindex
        expected = 0
        actual = March2017.Practice6.binary_search([1, 3, 4, 4, 5, 7, 9, 20], 1)
        self.assertEqual(expected, actual)

        # 4が二回続くが、最初の4のindexを返すかどうかをテスト
        expected = 2
        actual = March2017.Practice6.binary_search([1, 3, 4, 4, 5, 7, 9, 10], 4)
        self.assertEquals(expected, actual)

        # 最終index
        expected = 7
        actual = March2017.Practice6.binary_search([1, 3, 4, 4, 5, 7, 9, 10], 10)
        self.assertEqual(expected, actual)
        print("aaaaaaaaaaaaaaaaaaaaa")
    def tes_illegal_case(self):
            # listのどの値よりも小さい値を検索
        expected = -1
        actual = March2017.Practice6.binary_search([1, 3, 4, 4, 5, 7, 9, 10], -3)
        self.assertEquals(expected, actual)

        # listのどの要素よりも大きい値を検索
        expected = -1
        actual = March2017.Practice6.binary_search([1, 3, 4, 4, 5, 7, 9, 10], 123)
        self.assertEquals(expected, actual)

        # listにない要素を検索
        expected = -1
        actual = March2017.Practice6.binary_search([1, 3, 4, 4, 5, 7, 9, 10], 2)
        self.assertEquals(expected, actual)

        # 空のlistを代入
        expected = -1
        actual = March2017.Practice6.binary_search([], -3)
        self.assertEquals(expected, actual)
















