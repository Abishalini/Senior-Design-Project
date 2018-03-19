from panda import Panda

panda = Panda()

speed = 0
adjAngle = 0
Direction = ''
brakePerc = 0
while(True):
    A = panda.can_recv()
    for mesg in A:
        
        #Speed
        if mesg[0] == 1001:
            bits = ''
            for byte in mesg[2]:
                bits = bits + bin(byte)[2:].zfill(8)
            speed = int(bits[0:16],2) * .01
            #print('Speed = ' + str(speed) + ' mph')
            
        #Steering Angle
        elif mesg[0] == 485:
            bits = ''
            for byte in mesg[2]:
                bits = bits + bin(byte)[2:].zfill(8)
            angle = int(bits[8:24],2)*.0625
            
            if angle < 2000:
                adjAngle = angle
                Direction = 'Left'
                #print('Steering Angle = ' + str(angle) + ' degrees to the left')
            else:
                adjAngle = 4096 - angle
                Direction = 'Right'
                #print('Steering Angle = ' + str(adjAngle) + ' degrees to the right')

        #Accelerator Pedal Position
        elif mesg[0] == 417:
            bits = ''
            for byte in mesg[2]:
                bits = bits + bin(byte)[2:].zfill(8)
            accPerc = int(bits[48:56],2)*100/255
            #print('Accelerator Pedal Position = ' + str(int(round(accPerc))) + '%')
                

        #Brake Pedal Position
        elif mesg[0] == 241:
            bits = ''
            for byte in mesg[2]:
                bits = bits + bin(byte)[2:].zfill(8)
            brakePerc = int(bits[9:17],2)*.392157
            #print('Brake Pedal Position = ' + str(int(round(brakePerc))) + '%')

    print('\n')
    print('Speed = ' + str(speed) + ' mph')
    print('Steering Angle = ' + str(adjAngle) + ' degrees to the ' + Direction)
    print('Brake Pedal Position = ' + str(int(round(brakePerc))) + '%')
    print('Accelerator Pedal Position = ' + str(int(round(accPerc))) + '%')
    
