## steps

- Created a "thing" on aws iot core, registered rpi and downloaded all the certificates
- Moved the certificates on the rpi (as they were downloaded on my mac) and stored them in /home/pi/certs. These certificates are used as credentials in the iot.py script
- Created the iot.py script that is able to both publish and subscribe to the topic car/move on aws iot mqtt client
- the iot script is now able to communicate with mqtt client i.e send and recieve payloads
- it was now time to set up sns (do not remember all the steps exactly but this is a rough guide
- created an sns topic and its subscription
- on the subscription defined the protocol as sms and put down phone number in the end point
- went back to the iot core console and created a rule under message routing. This rule is subscribed to the topic car/move and says when this topic recieve x message (payload) defined in the sql statememnt, use that sns topic/subscription to send a msg to the endpoint defined in the sns topic.
- now the rpi can publish a msg to the topic car/move which has a rule to send a message through sns
- all the links are bookmarked in browser under rpi resources

## the logic (as it is in my head)

carscript --> iot script --> aws iot core --> sns --> phone number (end point)

--> = talks to
