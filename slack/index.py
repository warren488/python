from slackclient import SlackClient
import time

sc = SlackClient("xoxb-223596553904-q1LvYYqJLun4OyJtFKEt0QWQ")

if sc.rtm_connect():
    while True:
        variable = sc.rtm_read()
        if (len(variable) > 0):
            if ('type' in variable[0]) & (variable[0]['type'] == "message") & (variable[0].get('text') == 'hello python'):
                print(variable)
                sc.api_call(  "chat.postMessage",  channel=variable[0]['channel'],  text="Hello from Python! :tada:")
        time.sleep(1)
else:
    print("Connection Failed, invalid token?")