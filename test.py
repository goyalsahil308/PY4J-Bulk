class PythonPlayer(object):

    def multii(self,a):
       result=y.multi(a)
       print(result)
    def divii(self,b):
        result2=y.divi(b)
        print(result2)

from threading import Thread
from py4j.java_gateway import JavaGateway, CallbackServerParameters
gateway = JavaGateway(callback_server_parameters=CallbackServerParameters())
y=gateway.entry_point
pong_player = PythonPlayer()
for i in range(1000):
    t1=Thread(target=pong_player.multii,args=(i,))
    t1.start()
for i in range(400,601,2):
    t1=Thread(target=pong_player.divii,args=(i,))
    t1.start()
