import argparse
import subprocess
import sys

# Function to install missing requirements
def install_requirements():
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    except subprocess.CalledProcessError:
        print("Failed to install required dependencies.", file=sys.stderr)
        sys.exit(1)

default_arguments = [
    ("noconsole", True),
    ("clean", True),
    ("onefile", True),
    ("name", "\"switchAudioDevice\""),
    ("icon", "static\icon.ico"),
    ("add-binary", "\"AudioDLL.dll;.\""),
    ("add-data", "\"audioUtil;audioUtil\""),
    ("add-data", "\"static;static\""),
    ("hidden-import", "all"),
]

def main():
    # install_requirements()

    command = [
        "pyinstaller",
    ]

    for def_arg, val in default_arguments:
        arg = f"--{def_arg}"
        if isinstance(val, bool):
            command.append(arg)
        else:
            if val[0] == '"':
                command.append(f"{arg} {val}")
            else:
                command.append(f"{arg}={val}")

    command.append("main.py")
    
    # Remove empty strings from the command list
    command = [c for c in command if c]
    command = " ".join(command)

    subprocess.run(command, check=True)

if __name__ == "__main__":
    main()
