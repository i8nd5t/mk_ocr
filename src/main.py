import time

from LoungeTracker import LoungeTracker
from OBS import OBS
from OCR import OCR
from models import ImageRegion

if __name__ == "__main__":
    try:
        lounge_tracker = LoungeTracker()
        while True:
            obs = OBS()
            obs.connect()
            screen_shot = obs.get_source_screen_shot()

            ocr = OCR()
            # 順位表のプレーヤー名の範囲
            region = ImageRegion()
            detected_strings = ocr.extract_text(screen_shot, region)
            print(detected_strings)

            if not lounge_tracker.is_valid_leaderboard_screenshot(detected_strings):
                time.sleep(1)
                continue
            print(detected_strings)
            lounge_tracker.update_total_scores(detected_strings)
            print(lounge_tracker)

            time.sleep(60)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        obs.disconnect()
