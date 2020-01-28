import unittest
from HandComparator import HandComparator
from PokerHand import PokerHand
from Card import Card

class MyTestCase(unittest.TestCase):


    def test_create_card(self):
        card = Card("hearts", 5)
        self.assertEqual(card.getCard(), ["hearts", 5])

    def test_create_hand(self):
        card_list = []
        for i in range(5):
            card_list.append(Card())

        hand = PokerHand(card_list)

        self.assertFalse(hand.isEmpty())

    def test_get_hand(self):
        card_list = []
        for i in range(5):
            card_list.append(Card())

        hand = PokerHand(card_list)

        self.assertEqual(hand.getHand(), card_list)

    def test_remove_unused_positions(self):
        dummy_card_list = [[1, 5], [2, 0], [3, 1], [4, 0]]
        hand_comparator = HandComparator()
        refined_card_list = hand_comparator.remove_unused_positions(dummy_card_list)
        self.assertEqual([[1,5], [3,1]], refined_card_list)

    def test_check_if_straight_should_return_true_if_straight(self):
        dummy_card_list = [[5, 1], [6, 1], [7, 1], [8, 1], [9,1]]
        hand_comparator = HandComparator()
        is_straight = hand_comparator.check_if_straight(dummy_card_list)
        self.assertEqual(True, is_straight)

    def test_check_if_straight_should_return_false_if_not_straight(self):
        dummy_card_list = [[5, 1], [6, 1], [7, 1], [8, 1], [10,1]]
        hand_comparator = HandComparator()
        is_straight = hand_comparator.check_if_straight(dummy_card_list)
        self.assertEqual(False, is_straight)

    def test_four_kind_should_return_true_if_four_kind(self):
        dummy_card_list = [[13, 4], [6, 1]]
        hand_comparator = HandComparator()
        is_four_kind = hand_comparator.check_if_four_kind(dummy_card_list)
        self.assertEqual(True, is_four_kind)

    def test_four_kind_should_return_false_if_four_kind(self):
        dummy_card_list = [[1,3], [3, 2]]
        hand_comparator = HandComparator()
        is_four_kind = hand_comparator.check_if_four_kind(dummy_card_list)
        self.assertEqual(False, is_four_kind)

    def test_full_house_should_return_true_if_full_house(self):
        dummy_card_list = [[13, 2], [6, 3]]
        hand_comparator = HandComparator()
        is_full_house = hand_comparator.check_if_full_house(dummy_card_list)
        self.assertEqual(True, is_full_house)

    def test_full_house_should_return_false_if_not_house(self):
        dummy_card_list = [[1,1], [2, 2], [3, 2]]
        hand_comparator = HandComparator()
        is_full_house = hand_comparator.check_if_full_house(dummy_card_list)
        self.assertEqual(False, is_full_house)

    def test_three_kind_should_return_true_if_three_kind(self):
        dummy_card_list = [[2,1], [6, 1], [13, 3]]
        hand_comparator = HandComparator()
        is_three_kind = hand_comparator.check_if_three_kind(dummy_card_list)
        self.assertEqual(True, is_three_kind)

    def test_three_kind_should_return_false_if_not_three_kind(self):
        dummy_card_list = [[3,3], [7, 2]]
        hand_comparator = HandComparator()
        is_three_kind = hand_comparator.check_if_three_kind(dummy_card_list)
        self.assertEqual(False, is_three_kind)

    def test_two_pairs_should_return_true_if_two_pairs(self):
        dummy_card_list = [[2,1], [6, 2], [13, 2]]
        hand_comparator = HandComparator()
        is_two_pairs = hand_comparator.check_if_two_pairs(dummy_card_list)
        self.assertEqual(True, is_two_pairs)

    def test_two_pairs_should_return_false_if_not_two_pairs(self):
        dummy_card_list = [[3,3], [7, 2]]
        hand_comparator = HandComparator()
        is_two_pairs = hand_comparator.check_if_two_pairs(dummy_card_list)
        self.assertEqual(False, is_two_pairs)

    def test_pairs_should_return_true_if_pairs(self):
        dummy_card_list = [[2,1], [6, 1], [7, 1], [13, 2]]
        hand_comparator = HandComparator()
        is_pairs = hand_comparator.check_if_pairs(dummy_card_list)
        self.assertEqual(True, is_pairs)

    def test_pairs_should_return_false_if_not_pairs(self):
        dummy_card_list = [[3,3], [7, 2]]
        hand_comparator = HandComparator()
        is_pairs = hand_comparator.check_if_pairs(dummy_card_list)
        self.assertEqual(False, is_pairs)














"""
    def test_compare_hands(self):

        hand1 = PokerHand()
        hand2 = PokerHand()
        hand_comparator = HandComparator()
        winner = hand_comparator.comapre_hands(hand1, hand2)


        self.assertEqual(True, True)
"""

if __name__ == '__main__':
    unittest.main()
