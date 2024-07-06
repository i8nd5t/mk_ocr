from typing import List

from const import RACE_PLAYER_COUNT, SCORE_MAPPING


class LoungeTracker:
    """
    ラウンジのスコアを追跡し管理するクラス
    """
    def __init__(self):
        self.total_team_scores = {}

    def __str__(self):
        return str(
            sorted(self.total_team_scores.items(), key=lambda x: x[1], reverse=True)
        )

    def is_valid_leaderboard_screenshot(self, detected_strings: List[str]) -> bool:
        return len(detected_strings) == RACE_PLAYER_COUNT

    def update_total_scores(self, ranked_player_names: List[str]) -> None:
        for rank, name in enumerate(ranked_player_names, start=1):
            # プレイヤー名の頭文字を取得（大文字に変換）
            team = name[0].upper()

            if team in self.total_team_scores:
                self.total_team_scores[team] += SCORE_MAPPING[rank]
            else:
                self.total_team_scores[team] = SCORE_MAPPING[rank]
