import sys
import os

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the absolute path of the 'action' folder based on the current directory
action_folder_path = os.path.abspath(os.path.join(current_dir, '..', 'actions'))

# Add the 'action' folder to the python module search path
sys.path.insert(0, action_folder_path)

# print("Action folder path: ", action_folder_path)