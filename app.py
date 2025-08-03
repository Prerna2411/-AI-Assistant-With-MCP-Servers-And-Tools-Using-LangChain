import asyncio

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from mcp_use import MCPAgent,MCPClient
import os

async def run_memory_chat():
    """Run a chat using MCPAgent's built-in conversation memory"""
    ##LOAD ENVIRONMENT VARIABLE FOR API KEYS
    load_dotenv()
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

    ##CONFIG FILE PATH ---CHANGE THIS TO YOUR CONFIG FILE
    config_file="browser_mcp.json"

    print("Initializing a chat...")

    ##create MCP Client and agent with memory enabled
    client=MCPClient.from_config_file(config_file)
    llm=ChatGroq(model="llama3-70b-8192")


    ##create agent with memory enabled

    agent=MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True   ##enable built in conversational memory

    )



    print("\n==== Interactive MCP Chat====")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear conversation history")

     # Loop for user interaction
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chat.")
            break

        elif user_input.lower() == "clear":
            agent.clear_memory()
            print("Conversation history cleared.")
            continue

        try:
            # Run the agent and get response
            response = await agent.run(user_input)
            print(f"MCP: {response}")
        except Exception as e:
            print(f"Error: {e}")





if __name__=="__main__":
    asyncio.run(run_memory_chat())
