#!usr/bin/python
# -*- coding: utf-8 -*- 
import time
import datetime
import test
import mqtt_M5stick_pub as pub_mqtt


def time_judge(msg):
    
    while True:

        now = datetime.datetime.now()
        now_time = str(now.time())
        time_s = now_time[:-10]
        # print(time_s)

        if time_s == msg:
            pub_mqtt.main()
            break
        
        time.sleep(5)


def main():
    
    msg = input()
    
    time_judge(msg)
    
    print('終了しました')
 

if __name__ == "__main__":
    main()
