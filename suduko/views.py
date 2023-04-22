from django.shortcuts import render
from django.http import JsonResponse
from .solver import empty_cell, solve
from .apps import boards
import random
import copy
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home(response):
    global initial_board
    initial_board=random.choice(boards)
    sudoku_board= copy.deepcopy(initial_board)
    speed_options={
        "Normal": 0.7,
        "Medium": 0.4,
        "Fast": 0,
    }
    context={
        "sudoku_board": sudoku_board,
        "speed_options": speed_options
    }

    return render(response, "sudoku/index.html", context)

@login_required
def check(response):
    if response.method=="POST":
        data=response.POST
        sudoku_board= copy.deepcopy(initial_board)
        x, p=data.get('pos').split('x')
        x,y=int(x), int(p)
        val=data.get('val')

        if not str(val).isdigit() or int(val)==0 or len(str(val))>1:
            return JsonResponse({'is_correct': False,
                                 'all_solved': False })
        sudoku_board[x][y]=int(val)

        is_correct, _, _=solve(sudoku_board,[])
        if is_correct:
            initial_board[x][y]=int(val)
        else:
            initial_board[x][y]=0
        
        all_solved=not bool(empty_cell(initial_board))
        data={
            'is_correct': is_correct,
            'all_solved': all_solved
        }

        return JsonResponse(data)
    else:
        return JsonResponse({})

@login_required
def get_steps(response):
    if response.method=="POST":
        sudoku_board=copy.deepcopy(initial_board)
        d=[]
        ifsolved, steps, _ = solve(sudoku_board, d)
        return JsonResponse({'steps': steps,
                             'ifsolved': ifsolved})
    else:
        return JsonResponse({})
    
# @login_required
# def index(request):
#     scores= Score.objects.order_by('time')[:10]

#     return render(request, 'sudoku/leaderboard.html',{
#         'scores': scores
#     })

# @login_required
# def submit(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         time = float(request.POST.get('time'))
#         scores=Score(name=name, time=time, date=timezone.now())
#         scores.save()
#         return redirect('index')