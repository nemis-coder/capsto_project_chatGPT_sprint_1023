#!/usr/bin/env python3

import os
import openai
#from dotenv import load_dotenv
from openai import OpenAI


class ChatGPT:
    """A class to interact with OpenAI's ChatGPT model."""

    def __init__(self):
        # Load environment variables from the .env file
        #load_dotenv()

        # Retrieve the OPENAI_API_KEY environment variable
        self.api_key = os.getenv("OPENAI_API_KEY")
        #print("---->",self.api_key)

        # Set the retrieved API key for the OpenAI library
        openai.api_key = self.api_key

        # A constant to describe the role or behavior of the chatbot
        self.MAIN_ROLE = "This is the behavior of chatGPT"
        self.client = OpenAI(api_key=self.api_key)

    def request_openai(self, message, role="system"):
        """
        Make a request to the OpenAI API.

        Args:
        - message (str): The message to be sent to the OpenAI API.
        - role (str, optional): The role associated with the message. Defaults to "system".

        Returns:
        - str: The response content from the OpenAI API.
        """

        # Create a chat completion with the provided message and role
        response = self.client.chat.completions.create(model="gpt-3.5-turbo-1106",messages=[{
            "role": "system",
            "content": message}],temperature=1.5,response_format={"type": "json_object"})

        # Return the message content from the API response
        return response

# If you need to test or use this directly, you can do:
# if __name__ == "__main__":
#     chat_gpt = ChatGPT()
#     print(chat_gpt.request_openai("Hello!"))

