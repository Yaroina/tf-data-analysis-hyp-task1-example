import pandas as pd
import numpy as np


chat_id = 395384260 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.09
    from statsmodels.stats.proportion import proportions_ztest
    p = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='smaller')[1]
    
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return p < alpha
