import os
import glob
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pin_kb_btn = 24
pin_relay = 23
pin_sd_btn = 25

GPIO.setup(pin_kb_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin_sd_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin_relay, GPIO.OUT)

# Setup DS18B20 & Fan
base_dir = '/sys/bus/w1/devices/'
dev_dir = glob.glob(base_dir + '28*')[0]
dev_file = dev_dir + '/w1_slave'
fan = False
max_temp = 30   # Max Temp in Celcius

# DS18B20 Methods

def read_raw_temp():
    fh = open(dev_file, 'r')
    lines = fh.readlines()
    fh.close()
    return lines

def read_temp():
    lines = read_raw_temp()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.02)
        lines = read_raw_temp()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

def btn_kb_callback(channel):
    os.system('/home/pi/apocpi/togglekb.sh')

def btn_sd_callback(channel):
    os.system('sudo halt')

GPIO.add_event_detect(pin_kb_btn, GPIO.RISING, callback=btn_kb_callback, bouncetime=200)
GPIO.add_event_detect(pin_sd_btn, GPIO.RISING, callback=btn_sd_callback, bouncetime=200)

while(True):
    temp = read_temp()
    print(temp)

    # Turn fan off or on depending on temp
    if temp >= max_temp and fan == False:
        GPIO.output(pin_relay, GPIO.HIGH)
        fan = True
    elif temp <= (max_temp-1) and fan == True:
        GPIO.output(pin_relay, GPIO.LOW)
        fan = False

    time.sleep(0.02)
