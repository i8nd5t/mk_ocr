import cv2
import base64
import numpy as np
import easyocr
from io import BytesIO
from PIL import Image

from models import ImageRegion


class OCR:
    def extract_text(self, base64_image: str, region: ImageRegion):
        """
        Base64形式の画像データから、指定された範囲の文字を抽出する

        Args:
            base64_image_data (str): Base64形式の画像データ
            region (ImageRegion): 抽出範囲を表すデータ構造

        Returns:
            detected_strings（str） 抽出された文字列のリスト
        """

        # Base64データをデコードして画像に変換
        image_data = base64.b64decode(base64_image.split(",")[1])
        image = Image.open(BytesIO(image_data))

        # PIL ImageをOpenCV形式に変換
        cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # 順位表の領域を特定（この部分は実際の画像に合わせて調整が必要）
        height, width = cv_image.shape[:2]
        rankings_area = cv_image[
            int(height * region.start_y_ratio) : int(height * region.end_y_ratio),
            int(width * region.start_x_ratio) : int(width * region.end_x_ratio),
        ]

        # EasyOCRでテキストを抽出
        reader = easyocr.Reader(["en"])  # 英語を認識
        result = reader.readtext(rankings_area)

        # 文字列を抽出
        detected_strings = []
        for line in result:
            detected_strings.append(line[1])

        return detected_strings