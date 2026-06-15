from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv
import os 

from pathlib import Path
load_dotenv(Path(__file__).parent / ".env")
def main():
   model = ChatOpenAI(temperature=0)

   tools=[]
   agent_executor=create_agent(model,tools)

   print("welcome! I am your Ai assistant.Type 'quit' to exit")
   print("you can ask me to perform calculations or chat with me")

   while True:
      user_input=input("\n you:").strip()

      if user_input=="quit":
         break

      print("\nAssistant:",end="")
      for chunk in agent_executor.stream(
         {"messages":[HumanMessage(content=user_input)]}
         ):

       if "agent" in chunk and "messages" in chunk["agent"]:
         for message in chunk["agent"]["messages"]:
          print(message.content,end="")

         print()

if __name__=="__main__":
 main()
