import yt_dlp
import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import os
import streamlit as st
from langdetect import detect

# Function to download video using yt-dlp (audio only)
def download_video(url):
    ydl_opts = {
        'format': 'bestaudio/best',  # We only want the audio
        'outtmpl': 'downloaded_video.%(ext)s',  # Output filename template
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Download the audio
        print("Video downloaded successfully")
        return 'downloaded_video.mp4'  # Return the name of the downloaded audio file
    
    except Exception as e:
        raise Exception(f"Error downloading video: {str(e)}")


# Function to convert audio file to WAV format (handle paths and temporary files)
def convert_audio_to_wav(input_audio_file):
    try:
        # Ensure the file exists
        if not os.path.exists(input_audio_file):
            raise FileNotFoundError(f"Audio file not found: {input_audio_file}")
        
        print(f"Converting audio file: {input_audio_file}")
        
        # Set up the path for the output WAV file in a temporary directory
        output_audio_file = input_audio_file.replace('.mp4', '.wav')  # Convert to WAV
        audio = AudioSegment.from_file(input_audio_file)  # Detect format automatically
        audio.export(output_audio_file, format="wav")
        
        return output_audio_file  # Return the path to the converted WAV file
    
    except Exception as e:
        raise Exception(f"Error converting audio: {str(e)}")


# Function to analyze accent from the audio
def analyze_accent(audio_file):
    recognizer = sr.Recognizer()
    
    try:
        # Open and process the audio file
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        
        # Use Google's Speech Recognition to convert audio to text
        text = recognizer.recognize_google(audio)
        
        # Detect the language of the text
        language = detect(text)  # Get the detected language
        
        accent = "Unknown"
        confidence = 0
        
        # If English is detected, set accent as English and give it a confidence score
        if "english" in language.lower():
            accent = "English"
            confidence = 90  # Placeholder confidence (you can improve this with more advanced techniques)
        
        # Simple heuristic for accent detection based on keywords in the text
        if 'color' in text or 'favorite' in text or 'neighbor' in text:
            accent = "American"
            confidence = 95
        elif 'aeroplane' in text or 'lorry' in text:
            accent = "British"
            confidence = 90
        elif 'bungalow' in text or 'lorry' in text:
            accent = "Australian"
            confidence = 85
        
        # Return the accent, confidence, and a summary of the text (first 150 characters)
        return accent, confidence, text[:150]
    
    except sr.UnknownValueError:
        return "Could not understand the audio", 0, ""
    except sr.RequestError as e:
        return f"Error with the Speech Recognition API: {e}", 0, ""
    except Exception as e:
        return f"Error analyzing accent: {str(e)}", 0, ""


# Streamlit UI
def run_app():
    """
    Runs the Streamlit application for accent detection.
    """
    st.title("Accent Detection from Video Audio")
    
    # Reset the cache every time a new video URL is entered
    st.session_state.accent = ""
    st.session_state.confidence = 0
    st.session_state.summary = ""
    
    # Input for video URL
    video_url = st.text_input("Enter the public video URL (e.g., MP4, Loom):")
    
    if video_url:
        st.write("Downloading video and extracting audio...")

        try:
            # Step 1: Download the video and get the audio file path
            video_path = download_video(video_url)
            st.write(f"Video downloaded successfully: {video_path}")
            
            # Step 2: Convert the downloaded audio to WAV format (if it's in MP3 or other formats)
            audio_path = convert_audio_to_wav(video_path)
            st.write(f"Audio extracted and converted to WAV: {audio_path}")
            
            # Step 3: Analyze the accent of the extracted audio
            accent, confidence, summary = analyze_accent(audio_path)
            
            # Step 4: Display the results
            st.session_state.accent = accent
            st.session_state.confidence = confidence
            st.session_state.summary = summary
            
            st.write(f"Accent: {accent}")
            st.write(f"Confidence in English accent: {confidence}%")
            st.write(f"Summary of audio: {summary}")
        
        except Exception as e:
            st.write(f"An error occurred: {str(e)}")


# Run the Streamlit app
if __name__ == "__main__":
    run_app()
