# Project Concept

<p align="center">
  MystiCookie
</p>

<div align="center">
<img src="logo/mysticcookielogo.png" alt="Logo" width="200" height="200"/>
</div>


## Goal
To provide users with a unique and entertaining virtual fortune cookie experience, offering daily fortunes, wisdom, or humorous sayings.

## Key Features

### Daily Fortune Generation
- Use the ChatGPT API to generate short, fortune cookie-style messages. These could range from wise sayings and predictions to light-hearted and humorous quips.

### User Interaction
- Allow users to generate a virtual fortune cookie.
- Users could interact using the following questions:
    - "What color best describes your mood today?"
    - "In which month were you born?" Use the numbers from (1-12) 
    - "Pick one superpower: flying, invisibility, or telepathy?"
    - "What animal do you consider your spirit guide?"
    - "In one word, what's your dream travel destination?" 
    - "Choose one mystical creature as your companion: dragon, unicorn, phoenix, gnome, siren ?"

## Enhanced User Experience with DALL-E Integration

### Image Generation Based on Fortune Messages
- In a unique blend of textual and visual creativity, users can opt to receive an image generated by OpenAI's DALL-E, based on the message provided by the Fortune Cookie Bot.
- This feature transforms the text of the fortune cookie message into a vivid layer of engagement and personalization.

### Email Delivery of Fortune and Image
- Users will have the option to receive their daily fortune and its corresponding DALL-E generated image directly via email.
- This ensures a delightful surprise in their inbox, enhancing the overall experience.
- The email will include the text of the fortune, along with the visually captivating image inspired by the message, creating a more immersive and memorable interaction.

This project offers a blend of creativity and technical implementation :) <3.  
This innovative integration of DALL-E with the Fortune Cookie Bot not only enriches the user experience but also showcases the harmonious blend of AI in text and image generation, making each day’s fortune a unique and engaging encounter.

## Installation

### Setting Up Your Python Environment

To set up your Python environment for running the application, you will need to install the necessary packages listed in `requirements.txt`. Follow these steps to install them:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/nemis-coder/capsto_project_chatGPT_sprint_1023
   cd capsto_project_chatGPT_sprint_1023
2. **Create and Activate a Virtual Environment (optional but recommended):**:
    ```python
    python3 -m venv env
    source env/bin/activate
3. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
### Configuring Environment Variables
For the application to function properly, you need to set up the following environment variables:

- **OPENAI_API_KEY**: This is your API key for accessing the OpenAI API. It allows the application to make calls to the OpenAI services.
- **EMAIL_BOT**: The email address that will be used to send emails.
- **PWD_EMAIL_BOT**: The password for the email account specified in EMAIL_BOT.

## Usage & Demo

### How to Use the Application

Provide step-by-step instructions on how to use the application. This could include:

1. **Starting the Application**:
   You need to run the following command in the directory: capsto_project_chatGPT_sprint_1023
   ```python
   python main
<div align="center">
<img src="screens/start.png" alt="Logo" width="610" height="400"/>
</div>


2. **Navigating the Interface**:
  You need to answer the questions like the following example:
  <div align="center">
  <img src="screens/questions.png" alt="Logo" width="610" height="300"/>  
  </div>

3. **The response**::
   This is an exmaple of response.
  <div align="center">
  <img src="screens/message.png" alt="Logo" width="610" height="300"/>
  </div>


### Visual Preview

#### Screenshot of Email
This is how looks the email 
<div align="center">
<img src="screens/emailget.png" alt="Logo" width="610" height="50"/>
</div>

<div align="center">
<img src="screens/emailsent.png" alt="Logo" width="610" height="300"/>
</div>
