import json

import requests

from base import BASE_URL_V2, create_session, create_user, headers
from robotdraw import RobotDrawer


def clean_json(json_str):
    """
    Removes single-line comments from a JSON string.
    """
    # find the first { and the last } and return only that and that content between it
    start = json_str.find("{")
    end = json_str.find("}")
    return json_str[start : end + 1]


def get_line_segments(user_input, agent_id, user_id, session_id):
    url = f"{BASE_URL_V2}/chat/"
    payload = {
        "user_id": user_id,
        "agent_id": agent_id,
        "message": user_input,
        "session_id": session_id,
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        chat_response = response.json()
        agent_reply = clean_json(chat_response.get("response", "{}"))
        print(agent_reply)
        try:
            data = eval(agent_reply)
            line_segments = data.get("line_segments")
            return line_segments
        except json.JSONDecodeError:
            print("Agent response is not valid JSON.")
            return None
    else:
        print(f"Error during chat: {response.status_code} - {response.text}")
        return None


def main():
    print(
        "\n\n\n\n\n\n\n#########################################\n welcome to Dum-E command interface, powered by lyzr.\n\n\n\n"
    )
    # Step 1: Create User
    user_id = create_user()
    if not user_id:
        return

    # Step 2: Create Session
    session_id = create_session(user_id)
    if not session_id:
        return

    # Initialize the RobotDrawer
    robot_drawer = RobotDrawer()

    # Agent ID that converts input to line segments
    agent_id = "6723984161f92e3cfee9e1ab"  # Replace with the correct agent ID

    print(
        "\nYou can start giving drawing instructions to the robot. Type 'exit' to quit."
    )
    while True:
        user_input = input("Your drawing instructions: ")
        if user_input.lower() == "exit":
            break
        line_segments = get_line_segments(user_input, agent_id, user_id, session_id)
        if line_segments:
            robot_drawer.draw(line_segments)
        else:
            print("Failed to get line segments from agent.")

    # End connection with the robot
    robot_drawer.end_connection()


if __name__ == "__main__":
    main()
