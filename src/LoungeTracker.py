from collections import deque
from typing import List

from const import SCORE_MAPPING


class LoungeTracker:
    """
    ラウンジのスコアを追跡し管理するクラス
    """

    def __init__(self):
        self.total_team_scores = {}
        self.ranked_player_names_history = deque([])

    def __str__(self):
        return str(
            sorted(self.total_team_scores.items(), key=lambda x: x[1], reverse=True)
        )

    def add_race_result(self, ranked_player_names: object):
        self.ranked_player_names_history.append(ranked_player_names)
        self.__update_total_scores(ranked_player_names)

    def __update_total_scores(self, ranked_player_names: object) -> None:
        for rank, name in ranked_player_names.items():
            # プレイヤー名の頭文字を取得（大文字に変換）
            team = name[0].upper()

            if team in self.total_team_scores:
                self.total_team_scores[team] += SCORE_MAPPING[rank]
            else:
                self.total_team_scores[team] = SCORE_MAPPING[rank]
