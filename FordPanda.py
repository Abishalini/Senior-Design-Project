'''
Must have Panda library installed to use
For this project, we installed Panda on a virtual environment and ran from there
'''

from panda import Panda

panda = Panda()

speed = 0
adjAngle = 0
Direction = ''
brakePerc = 0

def DBCMessageDecode(PandaLine, msgNum, msgLen, msgScale, msgOffset):
    if PandaLine[0] == msgNum:
        bits = ''
        for byte in PandaLine[2]:
            bits = bits + bin(byte)[2:].zfill(8)
        #mesg = ???
        #print('\n')
        
        if msgNum == 1127:
            #print('Speed = ' + str(int(bits[40:40+msgLen],2)*msgScale+msgOffset))
            return int(bits[40:40+msgLen],2)*msgScale+msgOffset

        elif msgNum == 16:
            if bits[32] == '1':
                direct = 'Right'
            else:
                direct = 'Left'
            #print('Steering Angle = ' + str(int(bits[49:49+msgLen],2)*msgScale+msgOffset)+' '+direct)
            return direct,int(bits[49:49+msgLen],2)*msgScale+msgOffset

        elif msgNum == 125:
            #print('Brake Pedal Position = '+str(int(bits[0:0+msgLen],2)*msgScale+msgOffset)+'%')
            return int(bits[0:0+msgLen],2)*msgScale+msgOffset

        elif msgNum == 1125:
            #print('Latitude: ' + str(int(bits[0:8],2)-89)+str(int(bits[18:32],2)*.0001).lstrip('0'))
            return str(int(bits[0:8],2)-89)+str(int(bits[18:32],2)*.0001).lstrip('0'),str(int(bits[32:32+9],2)-179)+str(1-int(bits[33:33+14],2)*.0001).lstrip('0')
            #print('Longitude: ' + str(int(bits[32:32+9],2)-179)+str(1-int(bits[33:33+14],2)*.0001).lstrip('0'))

        
        elif msgNum == 516:
            #print('Acc pedal')
            #print(str(int(bits[6:6+msgLen],2)*msgScale+msgOffset))
            return int(bits[6:6+msgLen],2)*msgScale+msgOffset
        
                    
        return
    else:
        return

angle = 11111
direct = 'nope'
speed = 100
accPedal = 555
brake = 4535
lat = 'over there'
lon = 'over here'

while(True):
    A = panda.can_recv()
    for mesg in A:
        if mesg[0] == 1127:
            #Speed, 1127, bit start = 40
            speed = DBCMessageDecode(mesg,1127,8,1,0)

        elif mesg[0] == 16:
            #Angle, 16, bit start 49, but also the dir bit is 32
            direct,angle = DBCMessageDecode(mesg,16,16,.043945,0)

        elif mesg[0] == 125:
            #Brake Pedal Position
            brake = DBCMessageDecode(mesg,125,16,.125,0)

        elif mesg[0] == 516:
            #Accelerator Pedal Position
            accPedal = DBCMessageDecode(mesg,516,8,.390625,0)

        elif mesg[0] == 1125:
            #GPS, Lat appears to be first bit
            lat,lon = DBCMessageDecode(mesg,1125,14,.0001,0)

        
        print('\n')
        print('Speed = ' + str(speed) + ' mph')
        print('Steering Angle = ' + str(angle) + ' degrees to the ' + direct)
        print('Brake Pedal Position = ' + str(int(round(brake))) + '%')
        print('Accelerator Pedal Position = ' + str(int(round(accPedal))) + '%')
        print('Latitude = ' + lat)
        print('Longitude = ' + lon)
        
        
        #DBCMessageDecode(mesg,810,32,.001/60)
        #GPS Lat = 30.642ish
        #GPS Lon = -96.460ish
        #GPS Elv = 70m ish


