import google.generativeai as genai
import os
import requests

def read_api_token():
    with open('geminai.txt', 'r') as file:
        token = file.readline().strip()
    return token

API_TOKEN = read_api_token()

genai.configure(api_key=API_TOKEN)

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content(""" can you explain this to me as if you are a lawyer explaining it to a 16 yr old
### content 
We collect information about the apps, browsers, and devices you use to access Google services, which helps us provide features like automatic product updates and dimming your screen if your battery runs low.

The information we collect includes unique identifiers, browser type and settings, device type and settings, operating system, mobile network information including carrier name and phone number, and application version number. We also collect information about the interaction of your apps, browsers, and devices with our services, including IP address, crash reports, system activity, and the date, time, and referrer URL of your request.

We collect this information when a Google service on your device contacts our servers — for example, when you install an app from the Play Store or when a service checks for automatic updates. If you’re using an Android device with Google apps, your device periodically contacts Google servers to provide information about your device and connection to our services. This information includes things like your device type and carrier name, crash reports, which apps you've installed, and, depending on your device's settings, other information about how you’re using your Android device.

Your activity

We collect information about your activity in our services, which we use to do things like recommend a YouTube video you might like. The activity information we collect may include:

Terms you search for
Videos you watch
Views and interactions with content and ads
Voice and audio information
Purchase activityvc
People with whom you communicate or share content
Activity on third-party sites and apps that use our services
Chrome browsing history you’ve synced with your Google Account
If you use our services to make and receive calls or send and receive messages, we may collect call and message log information like your phone number, calling-party number, receiving-party number, forwarding numbers, sender and recipient email address, time and date of calls and messages, duration of calls, routing information, and types and volumes of calls and messages.
""")

print(response.text)