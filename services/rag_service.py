import ollama
def generate_ticket_response(text,category,priority,sentiment):
  """
  Generate professional telecom support response using olllama
  """
  system_prompt ="""
  you are a professional telecom support assistant.
  Guidelines:
  -respond professionally and concisely
  -show empathy if sentiment is negative
  -if priority is high,acknowledge urgency
  -do not invent policies or technica; details
  -if information is missing,politely ask for clarification
  -keep response under 15 words
  """
  User_prompt = f"""
  ticket details:
  category: {category}
  priority: {priority}
  sentiment: {sentiment}
  customer message: {text}
  """
  try:
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": system_prompt.strip()},
            {"role": "user", "content": User_prompt.strip()}],
        options={
            "temperature":0.5,
            "top_p":0.95,
            "max_tokens":128,
        }

    )
    return response["message"]["content"].strip()
  except Exception as e:
    print(f"Error generating ticket response: {e}")
    return "we are currently reviewing your issue"