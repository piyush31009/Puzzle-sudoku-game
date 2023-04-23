# Sudoku Game And Solver
This repository conatian the full stack web development on a Sudoku puzzle with login and signup page as without signup user cann't access the game page

# Tech Stack:
- Python
- Django
- HTML
- CSS
- Bootstrap
- Javascript
- Code Editor/tools and database: VS code, Command prompt, Powershell, SQLite

# Soft Skills:
- Time Management: Running time gives how to utilize and manage.
- Critical Thinking: Solving and understanding the problem statement requires interactive thinking.
- Patience: Take a time to make the good project  so at that period patience is necessary.
- Problem solving skills - Good amount of brain power and smart technique to solve such a puzzle.

# Puzzle Solving Techniques:
- Skeleton lookup: Logic-based puzzle that involves filling a 9x9 grid with numbers from 1 to 9 in such a way that each row, column, and 3x3 sub-grid contains all the numbers from 1 to 9 without any repetition. 
- Scanning: If only one place is empty in each row, column and 3x3 sub-grid then by identifying the place will be filled by that number.
- Penciling in: Finding a subset of cells in a sub-grid that can only contain a specific set of numbers. You can then eliminate these numbers from the possibilities for the rest of the cells in that sub-grid.
- Guessing: Guessing: If all else fails, you may need to make an educated guess and then work through the rest of the puzzle to see if your guess is correct. If it's not, you'll need to backtrack and try another possibility.

# Dead-ends of puzzle sudoku:
- Dead ends occur when a player makes a mistake while filling out the puzzle and reaches a point where no valid move can be made. This can happen when the player fills in a number in a cell that contradicts the rules of the game.
- When a player fills in a number in a cell that makes it impossible to fill in the remaining cells in that row, column, or box, it can also lead to a dead end.
- In some cases, dead ends can be avoided by using logical reasoning and deduction to eliminate possible numbers from cells and narrow down the possible solutions.

# Steps to setup:
Note: Before going to the steps of setup, Make sure that the operating system must installed with python and pip.  
- make the directory before yor start cloning
- clone this reprository by using git clone
- after cloning open the folder and with the help of https://drive.google.com/file/d/1sEUaT-cjxMuqUxBEkChUwg920uBUqapV/view?usp=share_link download the sudoku.csv file 
- get out of clonend folder and make the virtual environment and activate for project using the command: 
        --  pip install virtualenv
        --  virtualenv puzzle
        --  cd puzzle/Scripts
        --  activate
- now install django and numpy using: - pip install django
                                      - pip install numpy
- go inside the cloned folder and run manage.py by running command as: python manage.py runserver
- this will start the app on port 8000 and visit the app from localhost:8000

# Features :
- User can create an account and login using email and password.
 - User has to find the clues and it is guaranteed that there are atleast 5 clues in the whole puzzle.
 - User can play and complete a sudoku game.
 - User can reach more than 2 dead-ends in a game.
 - The always has one unique solution.
 - On refreshing or changing the browser, user progress is restored.
 - Admin dashboard is working and shows all the required data

# DEMO of web application:
![DashBoaard - Vivaldi 2023-04-23 14-29-34](https://user-images.githubusercontent.com/85010286/233832134-67203602-6bec-47a0-ae7f-0271641f56dd.gif)
![DashBoaard - Vivaldi 2023-04-23 14-29-34 (1)](https://user-images.githubusercontent.com/85010286/233832209-ba235c47-a80c-4108-b278-44f224531f74.gif)
![DashBoaard - Vivaldi 2023-04-23 14-29-34 (2)](https://user-images.githubusercontent.com/85010286/233832445-2eecfc8e-f30a-4d03-ad7f-6a5e2ed253ce.gif)
![DashBoaard - Vivaldi 2023-04-23 14-29-34 (3)](https://user-images.githubusercontent.com/85010286/233832460-5c5c1081-5276-4e35-91f3-731610e66ede.gif)
![DashBoaard - Vivaldi 2023-04-23 14-29-34 (4)](https://user-images.githubusercontent.com/85010286/233832568-9a206fd6-04fe-4a24-a2fd-b599e5cbc435.gif)
![DashBoaard - Vivaldi 2023-04-23 14-29-34 (5)](https://user-images.githubusercontent.com/85010286/233832577-79259016-8507-4ebe-95d6-2152697cbb8d.gif)
![DashBoaard - Vivaldi 2023-04-23 14-29-34 (6)](https://user-images.githubusercontent.com/85010286/233832660-d66a829f-0cbf-4c05-96bc-0ce52f27b5d3.gif)

# Website link:
For viewing the web application kindly clone and run with the help of steps to setup the project.
