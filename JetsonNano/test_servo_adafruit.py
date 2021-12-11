from adafruit_servokit import ServoKit
import adafruit_pca9685
import board
import busio
import time

i2c_bus0 = busio.I2C(board.SCL_1, board.SDA_1)

kit = list()
kit.append(ServoKit(channels=16, i2c=i2c_bus0, address=0x40))
kit.append(ServoKit(channels=16, i2c=i2c_bus0, address=0x41))

# val_list =[90, 90, 90, 90, 90, 90]
val_list =[90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]


if __name__ == '__main__':
    for x in range(len(val_list)):
        kit[int(x/6)].servo[int(x%6)].angle = val_list[x]
    print('Servo on: ')
    # while True:
    #     pass
    while True:
        for angle in range(70, 110):
            for num in range(0,len(val_list)):
                prev_angle = val_list[num]
                kit[int(num/6)].servo[int(num%6)].angle=angle
                time.sleep(0.01)
                print('Servo moving')
            val_list[num] = angle
        for angle in range(70, 110):
            for num in range(0,len(val_list)):
                prev_angle = val_list[num]
                kit[int(num/6)].servo[int(num%6)].angle=(180-angle)
                time.sleep(0.01)
                print('Servo moving')
            val_list[num] = angle
