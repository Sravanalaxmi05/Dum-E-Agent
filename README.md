# Dum-E powered by Lyzr agents

## Overview

The **Dum-E powered by Lyzr agents** is an interactive system that allows users to input text or drawing instructions via a chat interface. These instructions are then converted into precise line segments optimized for tracing by a robotic arm. The system leverages an API agent to interpret user inputs and commands a Niryo robotic arm to execute the drawings.

## Features

- **Interactive Chat Interface**: Seamlessly communicate drawing instructions.
- **API Integration**: Convert user inputs into actionable line segments using an API agent.
- **Robotic Arm Control**: Directly interface with a Niryo robotic arm to perform drawings.
- **Error Handling**: Robust parsing and error management for seamless operation.

## Prerequisites

- **Operating System**: Windows
- **Python Version**: 3.8 or higher
- **Robot**: [Niryo Robotic Arm](https://www.niryo.com/)

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/robotic-drawing-chat.git
    cd robotic-drawing-chat
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    - **Windows**

        ```bash
        venv\Scripts\activate
        ```

    - **Unix or MacOS**

        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **API Setup**

    - Open `base.py` and replace the placeholder API key with your actual API key.

        ```python
        API_KEY = "your-actual-api-key"
        ```

2. **Robot Configuration**

    - Open `robotdraw.py` and set the correct IP address for your Niryo robot.

        ```python
        ROBOT_IP_ADDRESS = "192.168.0.110"  # Replace with your robot's IP address
        ```

3. **Agent Configuration**

    - Ensure that the `agent_id` in `base.py` matches the ID of the agent responsible for converting user inputs to line segments.

        ```python
        agent_id = "your-agent-id"  # Replace with the correct agent ID
        ```

## Usage

1. **Run the Application**

    ```bash
    python lyzr.py
    ```

2. **Interact with the Chat Interface**

    - Upon running, the application will prompt you to enter drawing instructions.
    - Enter the desired text or drawing commands.
    - The system will process your input, generate the corresponding line segments, and command the robotic arm to draw.
    - To exit the application, type `exit`.

## Project Structure

- **base.py**: Core application that handles user input, communicates with the API agent, and manages the drawing session.
- **robotdraw.py**: Interfaces with the Niryo robotic arm to execute drawing commands.
- **requirements.txt**: Lists all Python dependencies required for the project.
- **README.md**: This documentation file.

## Troubleshooting

- **Invalid JSON Responses**

    - The API agent may sometimes include comments within JSON responses, which are not standard. The system includes a function to clean such responses by removing comments before parsing.

- **Robot Connection Issues**

    - Ensure that the Niryo robot is connected to the same network as your machine.
    - Verify the IP address in `robotdraw.py`.
    - Check that the robot is powered on and properly calibrated.

- **API Communication Errors**

    - Verify that the API key in `base.py` is correct.
    - Ensure that the API endpoint URLs are accessible.
    - Check network connectivity.


## Dependencies

The project relies on the following Python packages:
