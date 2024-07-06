import time

from ImageService import ImageService
from LoungeTracker import LoungeTracker
from OBS import OBS

if __name__ == "__main__":
    try:
        lounge_tracker = LoungeTracker()
        while True:
            obs = OBS()
            obs.connect()
            screen_shot_base64 = obs.get_source_screen_shot()
            image_service = ImageService()

            player_rank = image_service.get_player_rank(screen_shot_base64)
            # 順位を取得できない（順位表が表示されていない）場合は1秒待って取得し直す
            if not player_rank:
                time.sleep(1)
                continue

            ranked_players = image_service.recognize_ranked_player_names(screen_shot_base64)
            print(ranked_players)

            lounge_tracker.add_race_result(ranked_players)
            print(lounge_tracker)
            time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        obs.disconnect()
