from yowsup.stacks                             import YowStackBuilder
from yowsup.common                             import YowConstants
from yowsup.layers                             import YowLayerEvent
from layer                                     import EchoLayer
from yowsup.layers.auth                        import YowAuthenticationProtocolLayer
from yowsup.layers.coder                       import YowCoderLayer
from yowsup.layers.network                     import YowNetworkLayer
from yowsup.env                                import YowsupEnv
import time
time.sleep(10)
#Uncomment to log
#import logging
#logging.basicConfig(level=logging.DEBUG)

CREDENTIALS = ("phone number","<password from yowsup lib.>") #replace with your phone
if __name__==  "__main__":
    stackBuilder = YowStackBuilder()

    stack = stackBuilder\
        .pushDefaultLayers(True)\
        .push(EchoLayer)\
        .build()

    stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)       #setting credentials
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))          #sending the connect signal
    stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])           #whatsapp server address
    stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)
    stack.setProp(YowCoderLayer.PROP_RESOURCE, YowsupEnv.getCurrent().getResource())  #info about us as WhatsApp client
    stack.loop() 
    #stack.loop( timeout = 0.5, discrete = 0.5 )                                      #this is the program mainloop
    










