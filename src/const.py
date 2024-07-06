import numpy as np

SCORE_MAPPING = {
    1: 15,
    2: 12,
    3: 10,
    4: 9,
    5: 8,
    6: 7,
    7: 6,
    8: 5,
    9: 4,
    10: 3,
    11: 2,
    12: 1,
}

RACE_PLAYER_COUNT = 12

# 自分の順位であることを示す黄色の色範囲を定義
LOWER_YELLOW = np.array([20, 150, 150])
UPPER_YELLOW = np.array([30, 255, 255])