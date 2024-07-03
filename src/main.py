import asyncio
import cv2
import numpy as np
from obswebsocket import obsws, requests
from io import BytesIO
from PIL import Image
import logging
logging.basicConfig(level=logging.DEBUG)

# OBS WebSocket設定
host = "192.168.134.167"
port = 4455
password = "ylim2gCbnEutyIpY"  # OBS WebSocketで設定したパスワード

async def capture_obs_output():
    print("== start ==")
    ws = obsws(host, port, password)
    ws.connect()
    # print("connect: ", ws)

    try:
        # # バージョン情報の取得
        # version_request = requests.GetVersion()
        # version_response = ws.call(version_request)
        # print(f"Response: {version_response}")
        # print(f"Response Data: {version_response.datain}")

        # ソース（入力）リストを取得
        inputs_response = ws.call(requests.GetInputList())
        
        print("Available sources:")
        for input in inputs_response.datain['inputs']:
            print(f"Source: {input['inputName']} (Type: {input['inputKind']})")

        # スクリーンショットの取得
        source_name = "gameCapture"  # OBSで設定したソース名
        
        print(f"Sending request with sourceName: {source_name}")
        screenshot_response = ws.call(requests.GetSourceScreenshot(
            sourceName=source_name,imageFormat="png"
        ))
        print(f"Screenshot Response: {screenshot_response}")
        if screenshot_response.status:
            print(f"Screenshot Data: {screenshot_response.datain['imageData'][:100]}...")
        else:
            print(f"Screenshot Error: {screenshot_response.datain}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ws.disconnect()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    asyncio.run(capture_obs_output())