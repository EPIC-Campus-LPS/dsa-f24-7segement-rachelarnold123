import RPi.GPIO as GPIO
import time
import tm1637
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUTTON_PIN = 27
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)

#Set up the GPIO pins for CLK and DIO (modify GPIO numbers to match your wiring)
CLK = 18  # Change this to your CLK pin number
DIO = 17  # Change this to your DIO `pin number

# Initialize the TM1637 display
display = tm1637.TM1637(clk=CLK, dio=DIO)
display.brightness(7)

# Clear the display
display.write([0, 0, 0, 0])
#Adds time to stopwatch display 
def start():
    digits = 0000
    while GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        GPIO.output(16, GPIO.HIGH)
        digits += 1
	
        display.show(str(digits))
        time.sleep(1)

#Calls funtion so when button is pressed it adds time. When pressed again it stops, pauses, and resets	
while 1>0:
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
        GPIO.output(16, GPIO.LOW)
        time.sleep(2)
        display.write([0, 0, 0, 0,])
        start()
        
	
    
