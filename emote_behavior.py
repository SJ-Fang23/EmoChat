from Misty_actions import MISTY_ARM_ACTIONS, MISTY_HEAD_ACTIONS
from Misty_actions import MistyActions
import time
def emote_behavior(openai_response: str) -> None:
    actionClass = MistyActions()
    for action in MISTY_ARM_ACTIONS.keys():
        if action in openai_response:
            # get function name, arguments and call it
            getattr(actionClass,MISTY_ARM_ACTIONS[action][0])(MISTY_ARM_ACTIONS[action][1],MISTY_ARM_ACTIONS[action][2])
            time.sleep(0.5)
    for action in MISTY_HEAD_ACTIONS.keys():
        if action in openai_response:
            getattr(actionClass,MISTY_ARM_ACTIONS[action])
            time.sleep(0.5)


