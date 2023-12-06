"""
Misty robot action library
"""
import time
import mistyPy_modified as mistyPy_modified
from matplotlib import colors

# line up natural language actions with function name
MISTY_HEAD_ACTIONS = {"nod":"nod", "shake head":"shakehead", "lower head":"lowerHead"}
MISTY_ARM_ACTIONS = {"lift left arm":["arm","left",0], "lift right arm":["arm","right",0]}
MISTY_FACE_ACTIONS = {"joy face":"joy_face","love face":"love_face", "neutral face":"neutral_face", "angry face":"angry_face", "sleepy face": "sleepy_face", 
                      "surprised face":"suprise_face", "sad face":"sad_face", "feared face":"fear_face"}

class MistyActions():
    def __init__(self,ipAddress):
        # connnect to Misty with IP address
        self.robot = mistyPy_modified.Robot(ipAddress)
        self.facial_expressions = self.robot.images_saved
        self.audios = self.robot.audio_saved
    def reset(self):
        self.robot.moveArms("left",90)
        self.robot.moveArms("right",90)
        self.robot.changeImage('e_DefaultContent.jpg')
        self.robot.moveHead(roll=0,pitch=0,yaw=0, velocity=100)
        time.sleep(0.5)
    def show_expression(self, expression: str):
        image = 'e_' + expression + '.jpg'
        if image in self.facial_expressions:
            self.robot.changeImage(image)
    def arm(self, arm, position=90):
        # print("func called!")
        if arm == "left":
            if position in range(-360,360):
                self.robot.moveArms(arm,position)
                # self.robot.moveArms("right",90)
        elif arm == "right":
            # print("lift right!")
            if position in range(-360,360):
                self.robot.moveArms(arm,position)
                # self.robot.moveArms("left",90)
        time.sleep(0.5)
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
    def neutral_face(self):
        self.robot.changeImage('e_DefaultContent.jpg')
    def angry_face(self):
        self.robot.changeImage('e_Anger.jpg')
    def sleepy_face(self):
        self.robot.changeImage('e_Sleepy.jpg')
    def suprise_face(self):
        self.robot.changeImage('e_Surprise.jpg')
    def sad_face(self):
        self.robot.changeImage('e_Sadness.jpg')
    def fear_face(self):
        self.robot.changeImage('e_Fear.jpg')

if __name__ == "__main__":
    ip = "10.5.1.51"
    misty = MistyActions(ip)
    misty.robot.populateImages()
    # misty.love_face()
# misty.shakehead()
# mia.changeLED(225,0,0)
# mia.changeImage('e_Joy.jpg')
# # mia.playAudio('s_Joy4.wav')
# mia.moveHead(-1,-5,3, velocity = 5)
