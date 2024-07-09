import base64
import os
from twilio.rest import Client
source_number='+18156271878'
destination_numbers=['+14388881882']
def twilio_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)
 
    account_sid = 'AC58d7f7ae0e01e16b0659b75f6717d396'
    auth_token = '2af20187fc2e525cc9ba3f78381e0b05'
    client = Client(account_sid, auth_token)
    for each_destination_number in destination_numbers:
          message = client.messages.create(
                                        body='Message from twillo pubsub : ' +pubsub_message,
                                        from_=source_number,
                                        to=each_destination_number
                                   )
 
    print(message.sid)
  #twilio
