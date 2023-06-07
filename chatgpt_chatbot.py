import tkinter as tk
from tkinter import ttk
import random
from dotenv import load_dotenv
import os
import openai
import threading

load_dotenv()

openai.api_type = "azure"
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize messages list with the system message
messages = [
    {"role": "system", "content": "You are an AI assistant that helps people find information. \
                                   You will anything within your knowledge range. \
                                   You will say I don't know if the user's question is out of your knowledge. \
     							   You will refrain from speaking simplified Chinese and mainly respond in Traditional Chinese"},
]

def aoai_chat_model(chat, callback):
    # Append the user's message to the messages list
    messages.append({"role": "user", "content": chat})

    # Only send the last 5 messages to the API
    recent_messages = messages[-5:]
    
	# Send the recent messages to the OpenAI API and get the response
    response_chat = openai.ChatCompletion.create(
        engine="gpt-35-turbo",
        messages=recent_messages,
        temperature=0.7,
        max_tokens=300,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    # Append the assistant's response to the messages list
    messages.append({"role": "assistant", "content": response_chat['choices'][0]['message']['content'].strip()})

    # Call the callback function with the response
    callback(response_chat['choices'][0]['message']['content'].strip())

class ChatbotGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Chatbot")
        self.geometry("400x500")

        self.configure(bg='white')

        self.chat_area = tk.Text(self, bg='white', fg='black')
        self.chat_area.pack(expand=True, fill='both')

        self.message_entry = tk.Text(self, height=2, bg='white', fg='black')
        self.message_entry.pack(fill='x')
        self.message_entry.bind("<Return>", self.send_message)
        self.message_entry.bind("<Shift-Return>", lambda event: self.message_entry.insert(tk.INSERT, '\n'))

        self.send_button = tk.Button(self, text="Send", command=self.send_message, bg='white', fg='black')
        self.send_button.pack()

        self.dark_mode_button = tk.Button(self, text="Toggle Dark Mode", command=self.toggle_dark_mode, bg='white', fg='black')
        self.dark_mode_button.pack()

        self.is_dark_mode = False

    def send_message(self, event=None):
        message = self.message_entry.get("1.0", 'end-1c')
        if message:
            self.chat_area.insert(tk.END, "You: " + message + '\n')
            self.message_entry.delete("1.0", tk.END)
            self.chat_area.insert(tk.END, "Bot: typing...\n")
            self.typing_index = self.chat_area.index(tk.END + "-2 lines")
            threading.Thread(target=aoai_chat_model, args=(message, self.display_response)).start()
        return 'break'
    
    def display_response(self, response):
        def _delete_typing_message():
            self.chat_area.delete(self.typing_index, tk.END)
            self.chat_area.insert(tk.END, "\nBot: " + response + '\n')

        # Schedule _delete_typing_message to be called after 1000 milliseconds (1 second)
        self.after(1000, _delete_typing_message)

    def toggle_dark_mode(self):
        self.is_dark_mode = not self.is_dark_mode
        new_bg = 'black' if self.is_dark_mode else 'white'
        new_fg = 'white' if self.is_dark_mode else 'black'

        self.configure(bg=new_bg)
        self.chat_area.configure(bg=new_bg, fg=new_fg)
        self.message_entry.configure(bg=new_bg, fg=new_fg)
        self.send_button.configure(bg=new_bg, fg=new_fg)
        self.dark_mode_button.configure(bg=new_bg, fg=new_fg)

if __name__ == "__main__":
    chatbot_gui = ChatbotGUI()
    chatbot_gui.mainloop()