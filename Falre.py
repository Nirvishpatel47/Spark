from browseweb import browse_the_web as browse
import vork
from pytsx import say
from AnswersAdv import jarvis_simple
from opensearch import get_wikipedia_summary
import threading
from plyer import notification
import time
import sys

print("Text or Speak")
def Flare(TS=1):
    try: 
        if TS == 1:
            global jarvis_running
            user_query = input("You: ")
            ele = browse(user_query)
            if "off" == user_query:
                jarvis_running = False
                show_notifications("Jarvis has been turned off.")
                sys.exit()
                
            elif ele == "Sorry, I don't understand that.":
                ans = jarvis_simple(user_query)
                print(ans)
                """ if ans == "V2 error":
                    print(get_wikipedia_summary(user_query)) """
            
            else:
                print("Good by")
        elif TS == 2:
            user_query = vork.main()
            ele = browse(user_query)
            if ele == "Sorry, I don't understand that.":
                ans = jarvis_simple(user_query)
                print(ans)
                if ans == "V2 error":
                    print(get_wikipedia_summary(user_query))
            elif "off" in user_query:
                jarvis_running = False
                show_notifications("Jarvis has been turned off.")
                sys.exit()
                
            else:
                print("Good by")
    except Exception as e:
        print("Some error occured, And error is: ",e)

def show_notifications(mesage):
    notification.notify(
        title="Jarvis Assistant",
        message = mesage,
        timeout=5
    )

def jarvis_loop():
    while jarvis_running:
        command = Flare(TS=2)
        time.sleep(1)

""" if __name__ == "__main__":
    jarvis_running = True
    jarvis_thread = threading.Thread(target=jarvis_loop)
    jarvis_thread.start() """
    
