import os
from twilio.rest import Client
import openai

# Set your Twilio credentials
TWILIO_ACCOUNT_SID = 'your twilio account sid'
TWILIO_AUTH_TOKEN = 'your twilio auth token'
TWILIO_PHONE_NUMBER = 'your twilio phone number'

# Set your OpenAI GPT-3 API key
OPENAI_API_KEY = 'your openai api key'

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

# Function to send a WhatsApp message
def send_whatsapp_message(to, message):
    client.messages.create(
        to=f'whatsapp:{to}',
        from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
        body=message
    )

# Function to generate a response using GPT-3
def generate_response(message):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=50
    )
    return response.choices[0].text

# Listen for incoming WhatsApp messages
while True:
    incoming_messages = client.messages.list()

    for message in incoming_messages:
        if message.direction == "inbound":
            user_message = message.body
            user_number = message.from_

            # Generate a response using GPT-3
            response = generate_response(user_message)

            # Send the response back to the user
            send_whatsapp_message(user_number, response)
