from nlp_engine.llm_agent import LLMAgent

agent = LLMAgent()

# Simulate a conversation
history = []
user_input = "Salam, mera mobile chor ho gaya"
print(f"User: {user_input}")
response = agent.get_response(user_input, history)
print(f"Agent: {response}")
history.append({"role": "user", "content": user_input})
history.append({"role": "assistant", "content": response})

# Continue with next user response (mock)
user_input = "Mera naam Ali hai"
print(f"User: {user_input}")
response = agent.get_response(user_input, history)
print(f"Agent: {response}")