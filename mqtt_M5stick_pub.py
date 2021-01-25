#!usr/bin/python
# -*- coding: utf-8 -*- 

import paho.mqtt.client as mqtt     # MQTTのライブラリをインポート
from time import sleep              # 3秒間のウェイトのために使う
import time

# ブローカーに接続できたときの処理
def on_connect(client, userdata, flag, rc):
  print("Connected with result code " + str(rc))

# ブローカーが切断したときの処理
def on_disconnect(client, userdata, flag, rc):
  if rc != 0:
     print("Unexpected disconnection.")

# publishが完了したときの処理
def on_publish(client, userdata, mid):
  print("publish: {0}".format(mid))

# メイン関数   この関数は末尾のif文から呼び出される
def main():
  x = 0
  flg = 0
  client = mqtt.Client(client_id="pub_client")                 # クラスのインスタンス(実体)の作成
  client.on_connect = on_connect         # 接続時のコールバック関数を登録
  client.on_disconnect = on_disconnect   # 切断時のコールバックを登録
  client.on_publish = on_publish         # メッセージ送信時のコールバック


  #client.username_pw_set("token_HvlevplbmEyngEWT")
  client.username_pw_set(username="46323a3a", password="017f86d5b5690a13")
  client.connect("broker.shiftr.io", 1883, 60)  # 接続先は自分自身

  # 通信処理スタート
  client.loop_start()    # subはloop_forever()だが，pubはloop_start()で起動だけさせる

  # 永久に繰り返す
  while True:
    if flg == x: 
      client.publish("raspberry/PI", "Hello World")    # トピック名とメッセージを決めて送信
      break

if __name__ == '__main__':          # importされないときだけmain()を呼ぶ
  main()    # メイン関数を呼び出す

