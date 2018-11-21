#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:55:19 2018

@author: crantu
"""

from gpiozero import Servo

from read_setting_json import Setting
from time import sleep
pin_fig = Setting("pin")

"""
gpiozero.AngularServo(pin, *,
initial_angle=0, min_angle=-90, max_angle=90,
min_pulse_width=1/1000, max_pulse_width=2/1000,
frame_width=20/1000, pin_factory=None)
"""


class RemoveStopper:
    def __init__(self):
        servo_pin = int(pin_fig.setting_json["motor"]["remove_stopper"])
        self.servo = Servo(servo_pin)
        print(pin_fig.setting_json["motor"]["remove_stopper"])
        self.servo.min()
        sleep(1)

    def on(self):
        self.servo.value = 0.4
        sleep(1)
        print("remove stopper on")

    def off(self):
        print("remove stopper off")


if __name__ == "__main__":
    setting_time = Setting("time")
    rs = RemoveStopper()
    print("wating...")
    for i in range(10):
        print("{}, ", end="")
        sleep(1)
    print("")
    rs.on()
    # sleep(float(setting_time.setting_json["fire_and_conveyor"]
    #                                      ["remove_stopper"]
    #                                      ["operation_time"]))
