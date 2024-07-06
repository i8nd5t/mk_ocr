from obswebsocket import obsws, requests

# OBS WebSocket設定
host = "192.168.134.167"
port = 4455
password = "ylim2gCbnEutyIpY"  # OBS WebSocketで設定したパスワード

class OBS:
    """
    OBSとの通信、画面キャプチャの取得を行う
    """
    ws = None

    # obsに接続
    def connect(self):
        self.ws = obsws(host, port, password)
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
