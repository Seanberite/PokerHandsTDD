class HandComparator(object):

    def remove_unused_positions(self, card_counter_list):
        new_list = []
        for element in card_counter_list:
            if element[1] > 0:
                new_list.append(element)

        return new_list

    def check_if_straight(self, refined_card_list):
        if len(refined_card_list) == 5:
            last_element = refined_card_list[0][0]
            for element in refined_card_list:
                if element[0] - last_element >1:
                    return False
                last_element = element[0]
            return True
        else:
            return False

    def check_if_four_kind(self, refined_card_list):
        if len(refined_card_list) != 2:
            return False
        if (refined_card_list[0][1] == 4 or refined_card_list[1][1] == 4):
            return True
        else:
            return False


    def check_if_full_house(self, refined_card_list):
        if len(refined_card_list) != 2:
            return False
        if(refined_card_list[0][1] == 3 or refined_card_list[1][1]==3):
            return True
        else:
            return False

    def check_if_three_kind(self,refined_card_list):
        if len(refined_card_list) != 3:
            return False
        for element in refined_card_list:
            if element[1] == 3:
                return True
        return False


    def check_if_two_pairs(self, refined_card_list):
        if len(refined_card_list) != 3:
            return False
        pair_counter = 0
        for element in refined_card_list:
            if element[1] == 2:
                pair_counter += 1
        if pair_counter == 2:
            return True
        return False

    def check_if_pairs(self, refined_card_list):
        if len(refined_card_list) == 4:
            return True
        else:
            return False


    def comapre_hands(self, hand1, hand2):
        card_list_1 = hand1.getHand()
        card_list_2 = hand2.getHand()
        card_counter_list_1 = []
        card_hand_1_is_flush = True

        for i in range(13):
            card_counter_list_1.append([i,0])

        last_card_suit = card_list_1[0].getCard()[0]

        for card in card_list_1:
            card_suit, card_value = card.getCard()
            if card_suit != last_card_suit:
                card_hand_1_is_flush = False

            card_counter_list_1[card_value-1][1] += 1
            last_card_suit = card_suit


        refined_card_list = self.remove_unused_positions(card_counter_list_1)




        return