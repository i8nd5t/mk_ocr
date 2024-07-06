from obswebsocket import obsws, requests
import os
from dotenv import load_dotenv

load_dotenv()

class OBS:
    """
    OBSとの通信、画面キャプチャの取得を行う
    """

    ws = None

    # obsに接続
    def connect(self):
        self.ws = obsws(
            os.environ["OBS_HOST"], os.environ["OBS_PORT"], os.environ["OBS_PASSWORD"]
        )
        self.ws.connect()

    # スクリーンショットを取得しBase64形式で返却する
    def get_source_screen_shot(self, source_name="gameCapture"):
        screenshot_response = self.ws.call(
            requests.GetSourceScreenshot(sourceName=source_name, imageFormat="png")
        )

        return screenshot_response.datain["imageData"]

    # obsから切断
    def disconnect(self):
        self.ws.disconnect()
