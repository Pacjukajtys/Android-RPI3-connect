import socket 
import sys
import RPi.GPIO as GPIO
import time

#Tym razem na pinie GPIO18, fizyczny 12
PWM_PIN = 18
PWM_PINX = 23
PWM_PINY = 24

#Korzystamy ze schematu BCM, ustawiamy pin jako wyjscie
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(PWM_PIN, GPIO.OUT)
GPIO.setup(PWM_PINX, GPIO.OUT)
GPIO.setup(PWM_PINY, GPIO.OUT)

#Tworzymy obiekt klasy PWM; ustawiamy 50Hz (co 20ms)
pwm = GPIO.PWM(PWM_PIN, 500)
pwmx = GPIO.PWM(PWM_PINX, 500)
pwmy = GPIO.PWM(PWM_PINY, 500)

HOST = '192.168.0.28'
#HOST = '192.168.1.52'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.socket: must use to create a socket.
#socket.AF_INET: Address Format, Internet = IP Addresses.
#socket.SOCK_STREAM: two-way, connection-based byte streams.
print 'Socket stworzony'

#Bind socket to Host and Port
try:
	s.bind((HOST,PORT))
except socket.error as err:
	print 'Nie udalo sie polaczyc ' + str(err[0]) + ', Message: ' + err[1]
	sys.exit()
	
s.listen(1)

print 'Socket czeka na wiadomosc'
(conn, addr) = s.accept()
print 'Polaczone' 

while True:
    conn, addr = s.accept()
    print 'Connect with ' + addr[0] + ':' + str(addr[1])
    buf = conn.recv(1024)
    print buf
    uff = buf.split(";")
    print uff
    xx = float(uff[0])
    print xx
    zz = float(uff[1])
    print zz
    yy = float(uff[2])
    print yy
    
# sterowanie napieciem dla osi Z
    if zz<=-9:
        pwm.start(99)
    if zz>-9 and zz<=-8:
        pwm.start(96)
    if zz>-8 and zz<=-7:
        pwm.start(93)
    if zz>-7 and zz<=-6:
        pwm.start(90)
    if zz>-6 and zz<=-5:
        pwm.start(88)
    if zz>-5 and zz<=-4:
        pwm.start(85)
    if zz>-4 and zz<=-3:
        pwm.start(83)
    if zz>-3 and zz<=-2:
        pwm.start(81)
    if zz>-2 and zz<=-1:
        pwm.start(79)
    if zz>-1 and zz<=0:
        pwm.start(77)
    if zz>0 and zz<=1:
        pwm.start(74)
    if zz>1 and zz<=2:
        pwm.start(71)
    if zz>2 and zz<=3:
        pwm.start(68)
    if zz>3 and zz<=4:
        pwm.start(65)
    if zz>4 and zz<=5:
        pwm.start(62)
    if zz>5 and zz<=6:
        pwm.start(59)
    if zz>6 and zz<=7:
        pwm.start(56)
    if zz>7 and zz<=8:
        pwm.start(53)
    if zz>8:
        pwm.start(51)
        
#Sterowanie napieciem dla osi X
    if xx<=-9:
        pwmx.start(95)
    if xx>-9 and xx<=-8:
        pwmx.start(92)
    if xx>-8 and xx<=-7:
        pwmx.start(90)
    if xx>-7 and xx<=-6:
        pwmx.start(87)
    if xx>-6 and xx<=-5:
        pwmx.start(85)
    if xx>-5 and xx<=-4:
        pwmx.start(82)
    if xx>-4 and xx<=-3:
        pwmx.start(80)
    if xx>-3 and xx<=-2:
        pwmx.start(77)
    if xx>-2 and xx<=-1:
        pwmx.start(75)
    if xx>-1 and xx<=0:
        pwmx.start(72)
    if xx>0 and xx<=1:
        pwmx.start(70)
    if xx>1 and xx<=2:
        pwmx.start(67)
    if xx>2 and xx<=3:
        pwmx.start(65)
    if xx>3 and xx<=4:
        pwmx.start(62)
    if xx>4 and xx<=5:
        pwmx.start(60)
    if xx>5 and xx<=6:
        pwmx.start(57)
    if xx>6 and xx<=7:
        pwmx.start(55)
    if xx>7 and xx<=8:
        pwmx.start(52)
    if xx>8:
        pwmx.start(50)
        
        #Sterowanie napieciem dla osi y
    if yy<=-0.9:
        pwmy.start(50)
    if yy>-0.9 and yy<=-0.8:
        pwmy.start(52)
    if yy>-0.8 and yy<=-0.7:
        pwmy.start(55)
    if yy>-0.7 and yy<=-0.6:
        pwmy.start(57)
    if yy>-0.6 and yy<=-0.5:
        pwmy.start(60)
    if yy>-0.5 and yy<=-0.4:
        pwmy.start(62)
    if yy>-0.4 and yy<=-0.3:
        pwmy.start(65)
    if yy>-0.3 and yy<=-0.2:
        pwmy.start(67)
    if yy>-0.2 and yy<=-0.1:
        pwmy.start(70)
    if yy>-0.1 and yy<=0:
        pwmy.start(72)
    if yy>0. and yy<=0.1:
        pwmy.start(75)
    if yy>0.1 and yy<=0.2:
        pwmy.start(77)
    if yy>0.2 and yy<=0.3:
        pwmy.start(80)
    if yy>0.3 and yy<=0.4:
        pwmy.start(82)
    if yy>0.4 and yy<=0.5:
        pwmy.start(85)
    if yy>0.5 and yy<=0.6:
        pwmy.start(87)
    if yy>0.6 and yy<=0.7:
        pwmy.start(90)
    if yy>0.7 and yy<=0.8:
        pwmy.start(92)
    if yy>0.9:
        pwmy.start(95)
        
#    if buf == 'elo':
#        #inicjalizujemy wypelnieie 10%
#        pwm.start(50)
#	print 'no siema'
#    if buf == 'elo2':
#        #inicjalizujemy wypelnieie 10%
#        pwm.start(75)
#    if buf == 'elo3':
#        #inicjalizujemy wypelnieie 10%
#        pwm.start(100)
#    if buf == 'tak':
#        pwm.stop()
        #GPIO.cleanup()
#        print 'koniec'
        
conn.close()
GPIO.cleanup()
s.close()

