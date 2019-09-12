from ubidots import ApiClient

api = ApiClient(token='BBFF-4NVRsn1LmZy3Ak8gJEuoNEDIqbdr1r')
my_variable = api.get_variable('5d2ec1ca1d8472654464329b')

import time
import RPi.GPIO as led
led.setmode(led.BOARD)
led.setup(12,led.OUT)
led.setup(7,led.IN,pull_up_down=led.PUD_DOWN)

x=led.PWM(12,50)
x.start(2.5)
c=0
while 1:
        last_value = my_variable.get_values(1)
        a=last_value[0]['value']
        print(a)
        if c%2==0:
            if a==5 or a==1:
                c+=1
                x.ChangeDutyCycle(2.5)
                time.sleep(1)
                x.ChangeDutyCycle(7.5)
                time.sleep(1)
                x.ChangeDutyCycle(12.5)
                time.sleep(1)
                if led.input(7)==1:
                        new_value = my_variable.save_value({'value': 0})
        elif c%2!=0:
                if a==0:
                    c+=1
                    x.ChangeDutyCycle(7.5)
                    time.sleep(1)
                    x.ChangeDutyCycle(2.5)
                    time.sleep(1)
        print("pir= ",led.input(7))
        if led.input(7)==1:
            new_value = my_variable.save_value({'value': 0})
x.stop()

                

                

                
