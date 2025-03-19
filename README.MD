<div align="center">
    <img src="static/icon.ico" alt="Logo" width="80" height="80">

  <h3 align="center">SwitchAudioDevice (System Icon Tray)</h3>

  <p align="center">
    Easily switch between your current audio devices
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

This is a project which its only purpose is to simplify the switching of audio devices, as a more of a convenient way than it is currently. It has been built using Python.

## Getting Started

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/OrionFlame1/switchAudioDevice
   ```
2. Change into the directory
   ```sh
   cd switchAudioDevice
   ```
3. Install requirements (optional)
   ```sh
   pip install -r requirements.txt
   ```
4. Run directly as a script, but mandatory install the requirements as in previous step
   ```sh
   python main.py
   ```
5. Compile the project as executable (for Windows only)
   ```sh
   python build.py
   ```

6. For the compiling step, you can as well use the preset building command:
   ```sh
   pyinstaller --noconsole --clean --onefile --name "switchAudioDevice" --icon=static\icon.ico --add-binary "AudioDLL.dll;." --add-data "audioUtil;audioUtil" --add-data "static;static" --hidden-import=all main.py
   ```

## Usage

Simply right click on the newly appeared icon tray and select your preferred audio device at any time.

## Roadmap

- [ ] Functionality to also change input device
- [ ] Port for linux
- [ ] Functionality to set keybinds for few actions like:
    - [ ] cycle between devices
    - [ ] set a specific device
    
## Acknowledgments

Huge thanks to [@KillerBOSS2019](https://github.com/KillerBOSS2019) for the DLL and the library needed to make this possible.