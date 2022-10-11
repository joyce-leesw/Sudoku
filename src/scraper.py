import requests
import json
import numpy as np

def get_page():
    URL = "https://www.nytimes.com/puzzles/sudoku/easy"
    res = requests.get(URL)
    return res.text

def parse_page_data(html):
    key = "window.gameData"
    start = html.find(key)
    
    assert start != -1
    
    obj_start = html.find("{", start)
    
    assert html[obj_start] == "{"
    
    count = 0
    for i in range(obj_start, len(html)):
        if html[i] == "{":
            count += 1
        elif html[i] == "}":
            count -= 1
            if count == 0:
                return json.loads(html[obj_start:i+1])

def parse_easy_game_data(obj, difficulty):
    easy = obj["easy"]["puzzle_data"]["puzzle"]
    medium = obj["medium"]["puzzle_data"]["puzzle"]
    hard = obj["hard"]["puzzle_data"]["puzzle"]

    if difficulty == 'easy':
        arr = np.array(easy).reshape((9,9))
    elif difficulty == 'medium':
        arr = np.array(medium).reshape((9,9))
    elif difficulty == 'hard':
        arr = np.array(hard).reshape((9,9))
    return arr

def get_easy_game():
    html = get_page()
    obj = parse_page_data(html)
    difficulty = ''
    flag = 1
    while flag == 1:
        difficulty = input("Please select difficulty of Sudoku. Easy, medium, hard?: ")
        difficulty = difficulty.lower()
        if difficulty == 'easy' or difficulty == 'medium' or difficulty == 'hard':
            flag = 0
        else:
            print("Invalid Key")
    return parse_easy_game_data(obj, difficulty)



