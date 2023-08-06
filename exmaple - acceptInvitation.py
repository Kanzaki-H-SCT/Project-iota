from services import *
from akad import *
from thrift import *

import gevent.monkey
gevent.monkey.patch_all()

# from liff import * [not using here]

# THIS IS ONLY A EXAMPLE OF HOW TO USE CHATS SERVICE. YOU CAN CHANGE IT DEPEND ON YOUR USAGE.
# Author: CT / CT Core Team
# Project: IOTA
# This Script Version: Final

client = LINE("","")

print(f"Client Token: {client.authToken}")

def HelloWorld(op):
    if op.type == 124 and op.param3 == client.profile.mid:
        print(f"Invitation Detected - From User: {op.param2}")
        client.acceptChatInvitation(op.param1)
        print(f"Invitation Accepted: {op.param1}")

while True:
    ops = OEPoll(client).singleTrace(count=50)
    for op in ops or []:
        OEPoll(client).setRevision(op.revision)
        gevent.spawn(HelloWorld, op) 