#app id : 1137299228423635014
#public key : 2f900e9e2854fd17960ad392c3541270ccf47be5527d63209d44783c802c9ace
import discord
import os
import openai


file= input("Enter 1,2 or 3 for chat:\n")
match(file) :
  case "1":
    file= "chat1.txt"
  case "2":
    file= "chat2.txt"
  case "3":
    file= "chat3.txt"
  case _:
    file= "Invalid"
    exit()
with open(file,"r") as f:
  chat = f.read()

openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("SECRET_KEY")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        chat += f"{message.author}: {message.content}\n"
        print(f'Message from {message.author}:  {message.content}')
        print(message.mentions)
        if self.user != message.author :
            if self.user in message.mentions :
              print(chat)
              channel = message.channel
              response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"{chat}\nAmoghGPT: ",
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
              )
              messageToSend = response.choices[0].text
              await channel.send(messageToSend)
      
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
