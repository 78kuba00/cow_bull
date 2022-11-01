from django.shortcuts import render
from .game import Game
import random

# Create your views here.

attempt = []
step = 0
def play(request):
    secret_combination = [1, 2, 3, 4]
    global step
    if request.method == "GET":
        context = {
            "result": None,
            "message": "",
        }
        return render(request, "index.html")
    else:
        numbers_str = str(request.POST.get('numbers')).split()
        if not Game.is_valid_count(numbers_str):
            context = {
                "result": 'error',
                "message": "Please enter 4 number separated by space",
                "list_of_attempts": 'history',
            }
        elif not Game.is_unique_numbers(numbers_str):
            context = {
                "result": 'error',
                "message": "Numbers are not unique",
                "list_of_attempts": 'history',
            }
        elif not Game.is_valid_range(numbers_str):
            context = {
                "result": 'error',
                "message": "Numbers must be 1-9",
                "list_of_attempts": 'history',
            }
        else:
            result = Game.play(numbers_str, secret_combination)
            print(result)
            step += 1
            attempt.append({'step': step, 'result': f"Cows {len(result[0])} Bulls {len(result[1])}"})
            print(attempt)
            context = {
                "result": 'success',
                "message": f"Cows {len(result[0])} Bulls {len(result[1])}",
                "list_of_attempts": attempt,
            }
    return render(request, "index.html", context)



