# Accent Detection App

This is a simple Streamlit application that accepts a public video URL (e.g., MP4, YouTube, Loom), extracts the audio from the video, and detects the accent of the speaker. The app outputs:
- The detected accent (e.g., American, British, Australian).
- A confidence score for the detected accent.
- An optional explanation or summary of the accent.

## Features
- **Video URL Input**: Users provide a public video URL.
- **Audio Extraction**: The app extracts audio from the provided video URL.
- **Accent Detection**: The app detects the accent based on the extracted audio.
- **Streamlit UI**: A simple and user-friendly web interface for interaction.

## Setup Instructions

### 1. Clone or Download the Repository
- Download the project files to your local machine.

### 2. Create and Activate a Virtual Environment (Optional but Recommended)
- Open **Command Prompt** or **PowerShell** and run the following commands to set up a virtual environment:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

### 3. Install Dependencies
- Ensure that you have all necessary dependencies installed by running:

    ```bash
    pip install -r requirements.txt
    ```

### 4. Run the App
- Once the dependencies are installed, you can start the app by running:

    ```bash
    streamlit run app.py
    ```

### 5. Using the App
- After running the above command, the app will open in your default web browser.
- Input a valid public video URL (MP4 or YouTube) in the provided field, and the app will extract audio and classify the accent.

## Technologies Used
- **Streamlit**: For building the web UI.
- **MoviePy**: For extracting audio from the video.
- **SpeechBrain / Google Speech API**: For detecting the accent (optional, depends on the implementation).
- **Pytube**: For downloading YouTube videos.

## Troubleshooting

### 1. C++ Build Tools
- If you encounter errors related to building dependencies (e.g., `speechbrain`), make sure you have the **Visual C++ Build Tools** installed from [Microsoft's website](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

### 2. Missing Dependencies
- If any dependencies fail to install, try running:

    ```bash
    pip install --upgrade pip
    pip install sentencepiece
    ```

Let me know if you face any issues during setup or use!

