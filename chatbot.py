import openai
import gradio as gr
import os

# Set OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the system role
messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

# Define the chatbot function
def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

# Create the Gradio user interface
interface = gr.Interface(
    chatbot,
    inputs=gr.inputs.Textbox(lines=7, label="Talk with ChatGPT"),
    outputs=gr.outputs.Textbox(label="Reply"),
    title="ChatGPT in Python",
    description="Ask Away",
    theme="compact"
)

# Launch the Gradio user interface
interface.launch()
