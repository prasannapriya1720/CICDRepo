import getpass
import re
import subprocess
from pathlib import Path
import os

import win32api
import win32net
from docxtpl import DocxTemplate
import docx
import platform
#import win32api
#import win32net
import getpass
import sys



class commonMethods():
    def get_project_root(self):
        return str(Path(__file__).parent.parent)

    """
    Below code is when microsoft word is not install, we can use python-docx-template to create one
    Make user the template.docx is pointed to the word document template object
    """

    def create_docx_file_withoutMS(self):
        doc = DocxTemplate(os.path.join("template.docx"))
        context = {
            "name": "Vincent",
            "company": "WinWire Technologies",
            "location": "Bangalore"
        }

        doc.render(context)
        filename = os.path.join(os.environ["TEMP"], "test.docx")
        doc.save(filename)
        print(f"File saved to :{filename}")
        return filename

    def create_docx_file(self):
        filename = ""
        try:

            # Create a new word document object
            doc = docx.Document()

            # Adding text to document
            doc.add_paragraph("Hello, World!")
            doc.add_paragraph("This is a test document.")

            # save the document to the %temp% folder with the filename "test.docx"
            filename = os.path.join(os.environ["TEMP"], "test.docx")
            doc.save(filename)
            print(f"File save to :{filename}")
        except Exception as e:
            print(f"Error in create_docx_file -> {e}")
        return filename

    def eTMF_docx_file(self):
        base_filename = "TestAutomation"
        extension = ".docx"
        try:
            # Create a new Word document object
            doc = docx.Document()

            # Adding text to the document
            doc.add_paragraph("Hello, World!")
            doc.add_paragraph("This is a test document.")

            # Determine the full path to the temp directory
            temp_dir = os.environ["TEMP"]

            # Initialize the counter and construct the filename
            counter = 1
            while True:
                filename = os.path.join(temp_dir, f"{base_filename}{counter}{extension}")
                if not os.path.exists(filename):
                    break
                counter += 1

            # Save the document with the appropriate filename
            doc.save(filename)
            print(f"File saved to: {filename}")
        except Exception as e:
            print(f"Error in eTMF_docx_file -> {e}")
        return filename

    def error_message(self, message):
        lines = []
        try:
            # lines = message.split('{')
            # splitting the message with { or ( or )
            lines = re.split("[{(|)]", message)
        except Exception as e:
            print(f"Error in error_message -> {e}")
        if lines == "":
            lines[0] = message
        return lines[0]

    def getusername(self):
        full_name = ""
        try:
            # Check the current platform
            if platform.system() == 'Windows':
                # Get the current username
                # username = getpass.getuser()
                username = win32api.GetUserName()

                # get information about the current user
                user_info = win32net.NetUserGetInfo(None, username, 2)

                # get the full name of the current user
                full_name = user_info['full_name']
            else:
                # Get the current username
                username = getpass.getuser()

                # Get the current user's full name
                try:
                    import pwd
                    full_name = pwd.getpwnam(username).pw_gecos.split(',')[0]
                except ImportError:
                    full_name = ""

            if full_name == "":
                full_name = os.getlogin()
        except Exception as e:
            print("CommonMethods -> getusername -> \n" + str(e))
            if full_name == "":
                full_name = os.getlogin()
        return full_name

    def getOS(self):
        try:
            print()
            os = sys.platform
            if os == "linux":
                return "linux"
            elif os == "darwin":
                return "mac"
            elif os == "win32":
                return "windows"
            else:
                raise Exception("OS not supported")
        except Exception as e:
            print("CommonMethods -> getOS -> \n " + str(e))

    def get_os_details(self):
        # Initialize an empty string to store OS details
        os_details = ""

        # Check the operating system
        os_name = platform.system()
        # Windows
        if os_name == "Windows":
            windows_version = platform.release()
            windows_version_map = {
                "10": "Windows 10",
                "11": "Windows 11",
                "8": "Windows 8",
                "8.1": "Windows 8.1",
                "7": "Windows 7",
            }
            windows_full_version = platform.version()
            windows_name = windows_version_map.get(windows_version, "Windows")
            return f"{windows_name} {windows_full_version}"
        # macOS (Darwin) and Unix-like systems
        elif os_name == "Darwin" or os_name == "Linux":
            os_version = platform.release()
            os_version_full = platform.version()
            machine = platform.machine()
            processor = platform.processor()
            mac_version = subprocess.run(["sw_vers","-productVersion"], capture_output=True, text=True).stdout.strip()
            # Get more detailed information on Unix-based systems
            if hasattr(os, 'uname'):
                # os_info = os.uname()
                # os_details = (
                #     f"Operating System: {os_info.sysname}\n"
                #     f"Node Name: {os_info.nodename}\n"
                #     f"OS Version: {os_info.release}\n"
                #     f"Version: {os_info.version}\n"
                #     f"Machine: {os_info.machine}\n"
                #     f"Processor: {processor}\n"
                # )
                #os_details = ("macOS " + mac_version)

                # Create a dictionary mapping versions to macOS names
                macos_version_map = {
                    "14": "macOS Sonoma",  # Example for future releases
                    "13": "macOS Ventura",
                    "12": "macOS Monterey",
                    "11": "macOS Big Sur",
                    "10.15": "macOS Catalina",
                    "10.14": "macOS Mojave",
                    # Add more versions as needed
                }

                # Extract the major version (e.g., 13, 12, etc.)
                major_version = mac_version.split('.')[0]

                # Get the macOS name from the map, default to "macOS" if unknown
                mac_name = macos_version_map.get(major_version, "macOS")

                # Return formatted output like "macOS Ventura 13.6.4"
                return f"{mac_name} {mac_version}"
            else:
                os_details = (
                    f"Operating System: {os_name}\n"
                    f"OS Version: {os_version}\n"
                    f"Full OS Version: {os_version_full}\n"
                    f"Machine Type: {machine}\n"
                    f"Processor: {processor}\n"
                )

        # For other operating systems (Fallback)
        else:
            os_details = "Operating system details not available."

        # Return the OS details as a string
        return os_details