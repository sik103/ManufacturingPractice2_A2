#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:35:37 2018

@author: crantu
"""

from pygame import mixer
from gpiozero import LED
from os import path

from read_setting_json import Setting
pin_fig = Setting("pin")


class Siren:
    def __init__(self, audiofiles_dir):
        self.led_siren = LED(int(pin_fig.setting_json["led"]
                                                     ["describe_fire_truck"]))
        self.mixer_siren = mixer
        self.audiofiles_dir = audiofiles_dir

    def on(self):
        siren_mp3_path = path.join(self.audiofiles_dir,
                                   "ambulance-siren2.mp3")
        self.mixer_siren.init()
        self.mixer_siren.music.load(siren_mp3_path)  # 12sec
        self.mixer_siren.music.play(-1)
        self.led_siren.blink()
        print("siren on")

    def off(self):
        self.mixer_siren.music.stop()
        self.led_siren.off()
        print("siren off")


if __name__ == "__main__":
    from time import sleep
    setting_time = Setting("time")
    siren = Siren(audiofiles_dir="../../MP2_A2_audiofiles/AudioFiles/")
    siren.on()
    sleep(float(setting_time.setting_json['fire_and_conveyor']
                                         ['describe_fire_truck']
                                         ['operation_time']))
    siren.off()
