
#!usr/bin/python3
# -*- coding: utf-8 -*- 
import time
import datetime
import mqtt_device_pub as pub_mqtt


def time_judge(msg):
    
    while True:
        # 時間取得・string変換
        now = datetime.datetime.now()
        now_time = str(now.time())
        time_s = now_time[:-10]     # 00:00の形式になる(秒はない)
        # print(time_s)             # 現在の時間を確認できる

        # 時間を判定
        if time_s == msg:
            pub_mqtt.main()         # 送信(pub)処理
            break
        
        time.sleep(5)               # 5秒に1回判定、精度を高めるため。


def main():
    
    msg = input("時間 00:00 の形で入力 ＞ ")           # 時間を入力
    
    time_judge(msg)
    
    print('終了しました')
 

if __name__ == "__main__":
    main()
