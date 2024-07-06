import cv2
import base64
import numpy as np
import easyocr

from const import LOWER_YELLOW, RACE_PLAYER_COUNT, UPPER_YELLOW


class ImageService:
    def recognize_ranked_player_names(self, base64_image: str) -> object:
        image = self.__preprocess_and_decode_base64_image(base64_image)
        # easyOCRのリーダーを初期化（英語を認識）
        reader = easyocr.Reader(["en"])

        ranked_player_names = {}

        for rank in range(1, RACE_PLAYER_COUNT + 1):
            start_y = 75 + 70 * (rank - 1) + 8 * (rank - 1)
            end_y = 75 + 70 * rank + 8 * (rank - 1)

            region = image[start_y:end_y, 1010:1430]
            cv2.imwrite(f"player_name_region{rank}.png", region)

            # OCR実行
            result = reader.readtext(region, detail=0)

            # 認識されたテキストがある場合は最初のものを使用、ない場合は不明とする
            player_name = result[0] if result and result[0] else "不明"

            ranked_player_names[rank] = player_name
        return ranked_player_names

    def get_player_rank(self, base64_image):

        # base64形式の画像データをデコードしてOpenCV形式の画像に変換
        image = self.__preprocess_and_decode_base64_image(base64_image)

        cv2.imwrite("full_image.png", image)

        yellow_region_count = 0
        # 画像を順位ごとに切り出す
        for rank in range(1, RACE_PLAYER_COUNT + 1):
            start_y = 75 + 70 * (rank - 1) + 8 * (rank - 1)
            end_y = 75 + 70 * rank + 8 * (rank - 1)
            region = image[start_y:end_y, 828:1841]
            cv2.imwrite(f"region{rank}.png", region)

            if self.__is_yellow_region(region):
                yellow_region_count += 1

        print(f"yellow_region_count: {yellow_region_count}")

        # ちょうど1つの黄色い領域があれば順位表とみなす
        return yellow_region_count == 1

    def __is_yellow_region(self, region):
        # 画像をHSV色空間に変換
        hsv = cv2.cvtColor(region, cv2.COLOR_BGR2HSV)

        # 黄色のマスクを作成
        yellow_mask = cv2.inRange(hsv, LOWER_YELLOW, UPPER_YELLOW)

        # 黄色ピクセルの割合を計算
        yellow_ratio = cv2.countNonZero(yellow_mask) / (
            region.shape[0] * region.shape[1]
        )
        # print(f"yellow_ratio: {yellow_ratio}")

        # 黄色の割合が80%以上なら黄色の領域とみなす
        return yellow_ratio > 0.8

    def __preprocess_and_decode_base64_image(self, base64_image):
        # Data URIスキームの部分を削除（前処理）
        if base64_image.startswith("data:"):
            base64_image = base64_image.split(",", 1)[1]
        base64_image = base64_image.replace("\n", "").replace("\r", "").replace(" ", "")
        missing_padding = len(base64_image) % 4
        if missing_padding:
            base64_image += "-" * (4 - missing_padding)
        # print(base64_image[:100])
        # print(len(base64_image))
        image_bytes = base64.b64decode(base64_image)
        image = cv2.imdecode(
            np.frombuffer(image_bytes, dtype=np.uint8), cv2.IMREAD_COLOR
        )

        return image
