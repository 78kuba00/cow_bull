class Game:
    def play(number_guess_list, number_computer_list):
        cow_numbers, bull_numbers = [], []
        try:
            for index in range(len(number_guess_list)):
                if number_computer_list[index] == int(number_guess_list[index]):
                    bull_numbers.append(index)
                elif int(number_guess_list[index]) in number_computer_list:
                    cow_numbers.append(index)
            return cow_numbers, bull_numbers
        except:
            return cow_numbers, bull_numbers

    def is_valid_count(number_list):
        if len(number_list) == 4:
            return True
        return False

    def is_unique_numbers(number_list):
        s = set()
        for x in number_list:
            if x in s:
                return False
            s.add(x)
        return True

    def is_valid_range(number_list):
        for x in number_list:
            if int(x) < 1 or int(x) > 9:
                return False
            return True

    # def history(request):
    #     game_history = []
    #     attempt = 1
    #     if game_history:
    #         attempt += game_history[+1]['attempt']
    #         print (attempt)
    #         game_history.append(
    #             {
    #                 'attempt': attempt,
    #                 'result': f" Cows {cow_numbers} Bulls: {bull_numbers}",
    #             }
    #         )