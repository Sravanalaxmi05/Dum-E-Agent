import time

import numpy as np
from pyniryo2 import *

# Robot IP address
ROBOT_IP_ADDRESS = "192.168.0.110"

# Constants
Z_CONSTANT = 0.125


class CoordinateTransformer:
    def __init__(self, R, T):
        self.R = R
        self.T = T

    def local_to_robot(self, x_local, y_local):
        local_coords = np.array([x_local, y_local])
        robot_coords = self.R @ local_coords + self.T
        return robot_coords[0], robot_coords[1]


class RobotDrawer:
    def __init__(self):
        # Connect to the robot and calibrate
        # self.robot = NiryoRobot(ROBOT_IP_ADDRESS)
        # self.robot.arm.calibrate_auto()

        # Define the rectangle corner points in robot coordinates
        p1 = np.array([0.052, 0.212])
        p2 = np.array([-0.101, 0.224])
        p3 = np.array([-0.095, 0.359])
        p4 = np.array([0.07, 0.365])

        # Define local axes based on rectangle edges
        vec_x = p2 - p1
        vec_y = p4 - p1

        # Normalize the axis vectors to unit vectors
        unit_x = vec_x / np.linalg.norm(vec_x)
        unit_y = vec_y / np.linalg.norm(vec_y)

        # Create rotation matrix R and translation vector T
        R = np.column_stack((unit_x, unit_y))
        T = p1

        # Initialize the coordinate transformer
        self.transformer = CoordinateTransformer(R, T)

    def draw(self, line_segments):
        try:
            for segment in line_segments:
                start_local, end_local = segment

                # Transform start and end points to robot coordinates
                start_robot = self.transformer.local_to_robot(*start_local)
                end_robot = self.transformer.local_to_robot(*end_local)

                # Move to the start point (above the point)
                # self.robot.arm.move_pose(
                #     PoseObject(
                #         start_robot[0],
                #         start_robot[1],
                #         Z_CONSTANT + 0.02,
                #         0.0,
                #         1.57,
                #         0.0,
                #     )
                # )
                print("Moving to start point....\n\n\n")
                time.sleep(2)
                # Move down to the start point at drawing height
                # self.robot.arm.move_linear_pose(
                #     PoseObject(
                #         start_robot[0], start_robot[1], Z_CONSTANT, 0.0, 1.57, 0.0
                #     )
                # )
                print("Moving arm to draw height....\n\n\n")
                time.sleep(2)
                # Draw the line to the end point
                # self.robot.arm.move_linear_pose(
                #     PoseObject(end_robot[0], end_robot[1], Z_CONSTANT, 0.0, 1.57, 0.0)
                # )
                print("Drawing Segment....\n\n\n")
                time.sleep(2)
                # Lift the pen after drawing
                # self.robot.arm.move_linear_pose(
                #     PoseObject(
                #         end_robot[0], end_robot[1], Z_CONSTANT + 0.02, 0.0, 1.57, 0.0
                #     )
                # )
                print("Lift arm to stall height....\n\n\n")
                time.sleep(2)
                print(
                    f"Drew line from ({start_robot[0]:.3f}, {start_robot[1]:.3f}) "
                    f"to ({end_robot[0]:.3f}, {end_robot[1]:.3f})\n\n\n"
                )
        except Exception as e:
            print("An error occurred while moving the robot:", e)

    def end_connection(self):
        # self.robot.end()
        pass
