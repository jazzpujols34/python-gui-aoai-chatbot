# GPT-Powered Chatbot

This project is a simple graphical user interface (GUI) for a chatbot powered by Azure OpenAI's GPT-3 model. The chatbot can answer a wide range of questions and is designed to respond in Traditional Chinese.

## Features

- Simple and intuitive GUI built with Tkinter.
- Real-time interaction with the chatbot
- "Typing..." status to indicate when the bot is generating a response
- Dark mode toggle for a more comfortable user experience

## Setup

1. Clone this repository to your local machine.

2. Install the required Python packages using pip:

```
pip install -r requirements.txt
```

3. Set up your OpenAI API key. You can do this by creating a `.env` file in the root directory of the project with the following content:

```
OPENAI_API_KEY = <your-aoai-key>
OPENAI_API_BASE = <your-aoai-base>
```

Replace `your-aoai-key` with your actual Azure OpenAI API key.
Replace `your-aoai-base` with your actual Azure OpenAI API url.

4. Run the application:

```
python chatgpt_chatbot.py
```


## Usage

1. Type your message into the text box at the bottom of the application window.
2. Press Enter to send your message. The chatbot will start generating a response, indicated by the "Bot: typing..." status.
3. Once the chatbot has generated a response, it will be displayed in the chat area.
4. To switch between light and dark modes, click the "Toggle Dark Mode" button.



