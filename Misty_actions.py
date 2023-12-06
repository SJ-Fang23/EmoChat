"""
Misty robot action library
"""
import time
import mistyPy_modified
from matplotlib import colors

# line up natural language actions with function name
MISTY_HEAD_ACTIONS = {"nod":"nod", "shake head":"shakehead", "lower head":"lowerHead"}
MISTY_ARM_ACTIONS = {"lift left arm":["arm","left",0], "lift right arm":["arm","right",0]}

class MistyActions():
    def __init__(self,ipAddress):
        # connnect to Misty with IP address
        self.robot = mistyPy_modified.Robot(ipAddress)
        self.facial_expressions = self.robot.images_saved
        self.audios = self.robot.audio_saved
    def reset_pose(self):
        self.robot.moveArms("left",90)
        self.robot.moveArms("right",90)
    def show_expression(self, expression: str):
        image = 'e_' + expression + '.jpg'
        if image in self.facial_expressions:
            self.robot.changeImage(image)
    def arm(self, arm, position=90):
        if arm in ["left", "right"]:
            if position in range(-360,360):
                self.robot.moveArms(arm, position)
    def nod(self):
        self.robot.moveHead(roll=0,pitch=20,yaw=0, velocity=100)
        time.sleep(1)
        self.robot.moveHead(roll=0, pitch=0,yaw=0,velocity=100)
    def shakehead(self):
        self.robot.moveHead(roll=0,pitch=0,yaw=20, velocity=100)
        time.sleep(1)
        self.robot.moveHead(roll=0, pitch=0,yaw=-20,velocity=100)
        time.sleep(1)
        self.robot.moveHead(roll=0, pitch=0,yaw=0,velocity=100)
    def lowerHead(self):
        self.robot.moveHead(roll=0,pitch=20,yaw=0, velocity=100)
        time.sleep(1)    
    def changeled(self,color):
        assert color in list(colors.cnames.keys()), "invalid colors!"
        rgb = colors.to_rgb(color)
        self.robot.changeLED(rgb[0],rgb[1],rgb[2])
    
    def joy_face(self):
        self.robot.changeImage('e_{}.jpg'.format("Joy"))
    def love_face(self):
        self.robot.changeImage('e_Love.jpg')

if __name__ == "__main__":
    ip = "10.5.6.13"
    misty = MistyActions(ip)
    # misty.robot.populateImages()
    misty.love_face()
# misty.shakehead()
# mia.changeLED(225,0,0)
# mia.changeImage('e_Joy.jpg')
# # mia.playAudio('s_Joy4.wav')
# mia.moveHead(-1,-5,3, velocity = 5)
