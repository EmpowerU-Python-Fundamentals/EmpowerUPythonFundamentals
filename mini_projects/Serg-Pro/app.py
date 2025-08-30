import os
import av
import threading
import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
from audio_handling import AudioFrameHandler
from bird_detection import VideoFrameHandler


# Define the rtc config
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

# Define the audio file to use.
alarm_file_path = os.path.join("audio", "craw3.wav")

st.title("Local Area Smart Scarecrow")

with st.container():
    c1, c2 = st.columns(spec=[1, 1])
    with c1:
        # The amount of time (in seconds) to wait before sounding the alarm.
        WAIT_TIME = st.sidebar.slider("Seconds to wait before sounding alarm:", 0.0, 5.0, 1.0, 0.25)

    with c2:
        CONF_THRESHOLD = st.sidebar.slider("Select Model Confidence", 0.0, 1.0, 0.4, 0.05)

thresholds = {
    "CONF_THRESHOLD": CONF_THRESHOLD,
    "WAIT_TIME": WAIT_TIME,
}

# For streamlit-webrtc
video_handler = VideoFrameHandler()
audio_handler = AudioFrameHandler(sound_file_path=alarm_file_path)

lock = threading.Lock()  # For thread-safe access & to prevent race-condition.
shared_state = {"play_alarm": False}

def video_frame_callback(frame: av.VideoFrame):
    frame = frame.to_ndarray(format="bgr24")  # Decode and convert frame to RGB

    frame, play_alarm = video_handler.process(frame, thresholds)  # Process frame

    with lock:
        shared_state["play_alarm"] = play_alarm  # Update shared state
    return av.VideoFrame.from_ndarray(frame, format="bgr24")  # Encode and return BGR frame


def audio_frame_callback(frame: av.AudioFrame):
    with lock:  # Access the current “play_alarm” state
        play_alarm = shared_state["play_alarm"]

    new_frame: av.AudioFrame = audio_handler.process(frame, play_sound=play_alarm)
    return new_frame


webrtc_ctx = webrtc_streamer(
    key="bird_detection",
    video_frame_callback=video_frame_callback,
    audio_frame_callback=audio_frame_callback,
    rtc_configuration=RTC_CONFIGURATION,  # Add this to config for cloud deployment.
    # media_stream_constraints={"video": {"height": {"ideal": 640}}, "audio": True},
)
