from Misty_actions import MISTY_ARM_ACTIONS, MISTY_HEAD_ACTIONS
from Misty_actions import MistyActions
import time
def emote_behavior(robot_handler: MistyActions, openai_response: str) -> None:
    
    for action in MISTY_ARM_ACTIONS.keys():
        if action in openai_response:
            # get function name, arguments and call it
            getattr(robot_handler,MISTY_ARM_ACTIONS[action][0])(MISTY_ARM_ACTIONS[action][1],MISTY_ARM_ACTIONS[action][2])
            time.sleep(0.5)
    for action in MISTY_HEAD_ACTIONS.keys():
        if action in openai_response:
            # print(MISTY_HEAD_ACTIONS[action])
            getattr(robot_handler,MISTY_HEAD_ACTIONS[action])()
            time.sleep(0.5)

if __name__ == "__main__":
    ip = "10.5.6.13"
    actionClass = MistyActions(ip)
    # actionClass.nod()
    actions = "<lift left arm>,<nod>"
    emote_behavior(actionClass,actions)

