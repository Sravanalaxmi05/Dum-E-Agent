import uuid

import requests

# Base URLs for the API
BASE_URL_V1 = "https://agent.api.lyzr.app/v1"
BASE_URL_V2 = "https://agent.api.lyzr.app/v2"

# Your API key for authentication
API_KEY = "lyzr-zuCDK2lUfb1HbxadW6zhRIST"  # Replace with your actual API key

# Headers including the API key
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "x-api-key": API_KEY,
}


def create_user():
    url = f"{BASE_URL_V1}/users/"
    unique_user_id = str(uuid.uuid4())  # Generate a unique user ID
    payload = {
        "user_id": unique_user_id,
        "email": f"user_{unique_user_id}@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "metadata": {},
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        user_data = response.json()
        print(f"Create user response: {user_data}")  # Debug line to see the response
        # Adjust this line based on the actual response structure
        user_id = (
            user_data.get("user_id")
            or user_data.get("user_id", {}).get("$oid")
            or user_data.get("id")
        )
        user_id = (
            user_id.get("user_id")
            or user_id.get("user_id", {}).get("$oid")
            or user_id.get("id")
        )
        print(f"User created with ID: {user_id}")
        return user_id
    else:
        print(f"Error creating user: {response.status_code} - {response.text}")
        return None


def create_session(user_id):
    url = f"{BASE_URL_V1}/sessions/"
    payload = {"user_id": user_id, "metadata": {}}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        session_data = response.json()
        session_id = session_data.get("session_id")
        print(f"Session created with ID: {session_id}")
        return session_id
    else:
        print(f"Error creating session: {response.status_code} - {response.text}")
        return None


def chat_with_agent(agent_id, user_id, session_id):
    url = f"{BASE_URL_V2}/chat/"
    print("\nYou can start chatting with the agent. Type 'exit' to quit.")
    while True:
        message = input("You: ")
        if message.lower() == "exit":
            break
        payload = {
            "user_id": user_id,
            "agent_id": agent_id,
            "message": message,
            "session_id": session_id,
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            chat_response = response.json()
            agent_reply = chat_response.get("response", "No response from agent.")
            print(f"Agent: {agent_reply}")
        else:
            print(f"Error during chat: {response.status_code} - {response.text}")


def main():
    # Step 1: Create User
    user_id = create_user()
    if not user_id:
        return

    # Step 2: Create Session
    session_id = create_session(user_id)
    if not session_id:
        return

    # Step 5: Chat with Agent
    chat_with_agent("6723984161f92e3cfee9e1ab", user_id, session_id)


if __name__ == "__main__":
    main()
