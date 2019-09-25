#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 12:07:30 2019

@author: adamsiegel
"""

import random

def game(inning):
    home_score = 0
    away_score = 0
    
    current_inning_index = inning
    
    away_score = 0
    home_score = 0
    
    while(current_inning_index < 10):
        away_score = half_inning(away_score, current_inning_index)
        home_score = half_inning(home_score, current_inning_index)
        current_inning_index += 1
        
    while (home_score == away_score):
        away_score = half_inning(away_score, current_inning_index)
        home_score = half_inning(home_score, current_inning_index)
        current_inning_index += 1
    
    final_inning = current_inning_index - 1
        
    return(home_score, away_score, final_inning)
    
def plate_appearance():
    event = random.random()
    outcome = ""
    if event <= 0.14:
        outcome = "1B"
    elif event > 0.14 and event <= 0.19:
        outcome = "2B"
    elif event > 0.19 and event <= 0.195:
        outcome = "3B"
    elif event < 0.195 and event <= 0.23:
        outcome = "HR"
    elif event < 0.23 and event <= 0.46:
        outcome = "K"
    elif event < 0.46 and event <= 0.545:
        outcome = "BB"
    elif event < 0.545 and event <= 0.85:
        outcome = "groundout"
    else:
        outcome = "flyout"

    return(outcome)
    
def half_inning(team_score, inning):
    score = team_score
    runner_on_first = False
    if inning > 9:
        runner_on_second = True
    else:
        runner_on_second = False
    runner_on_third = False
    
    outs = 0
    while(outs < 3):
        current_pa = plate_appearance()
        if current_pa == "1B":
            if runner_on_third:
                score += 1
                runner_on_third = False
            if runner_on_second:
                runner_on_third = True
                runner_on_second = False
            if runner_on_first:
                runner_on_second = True
                runner_on_first = False
            runner_on_first = True
        elif current_pa == "2B":
            if runner_on_third:
                score += 1
                runner_on_third = False
            if runner_on_second:
                score += 1
                runner_on_second = False
            if runner_on_first:
                runner_on_third = True
                runner_on_first = False
            runner_on_second = True
        elif current_pa == "3B":
            if runner_on_third:
                score += 1
                runner_on_third = False
            if runner_on_second:
                score += 1
                runner_on_second = False
            if runner_on_first:
                score += 1
                runner_on_first = False
            runner_on_third = True
        elif current_pa == "HR":
            if runner_on_third:
                score += 1
            if runner_on_second:
                score += 1
            if runner_on_first:
                score += 1
            runner_on_third = False
            runner_on_second = False
            runner_on_first = False
            score += 1
        elif current_pa == "K":
            outs += 1
        elif current_pa == "BB":
            if runner_on_first:
                if runner_on_second:
                    if runner_on_third:
                        score += 1
                    else:
                        runner_on_third = True
                else:
                    runner_on_second = True
            else:
                runner_on_first = True
        elif current_pa == "groundout":
            outs += 1
        else:
            outs += 1
        
    return(score)
    



    

     
    
    
    
    
    