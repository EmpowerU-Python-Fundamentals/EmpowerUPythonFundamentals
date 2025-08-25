import cv2
import time
import torch
import warnings
import numpy as np
from ultralytics import YOLO
from supervision.tools.detections import Detections, BoxAnnotator
from supervision.draw.color import ColorPalette

# Define GPU or CPU
device = 'cuda' if torch.cuda.is_available() else "cpu"
# print("Using Device: ", device)
warnings.filterwarnings("ignore", message="torch.distributed.reduce_op is deprecated")

# Create a pre-trained YOLO model
model = YOLO("models/yolo_weights/yolov8n.pt")
model.fuse()

# Import the class names    
CLASS_NAMES_DICT = model.model.names

# id for only bird detection
bird_id = 14

# Define the box_annotator
box_annotator = BoxAnnotator(color=ColorPalette(), thickness=3, text_thickness=1, text_scale=0.5)

def plot_text(image, text, origin, color, font=cv2.FONT_HERSHEY_SIMPLEX, fntScale=0.8, thickness=2):
    image = cv2.putText(image, text, origin, font, fntScale, color, thickness)
    return image

class VideoFrameHandler:
    def __init__(self):
        """
        Initialize the necessary constants, mediapipe app
        and tracker variables
        """
        # Used for coloring landmark points.
        self.RED = (0, 0, 255)  # BGR

        # For tracking counters and sharing states in and out of callbacks.
        self.state_tracker = {
            "start_time": time.perf_counter(),
            "DROWSY_TIME": 0.0, 
            "COLOR": self.RED,
            "play_alarm": False,
        }

    def process(self, frame: np.array, thresholds: dict):
        """
        Args:
            frame: (np.array) Input frame matrix.
            thresholds: (dict) Contains the two threshold values
                               WAIT_TIME and CONF_THRESHOLD.

        Returns:
            The processed frame and a boolean flag to
            indicate if the alarm should be played or not.
        """
        # To improve performance,
        # mark the frame as not writeable to pass by reference.
        frame.flags.writeable = False
        frame_h, frame_w, _ = frame.shape

        ALM_txt_pos = (10, int(frame_h // 2 * 1.85))

        results = model(frame, classes=bird_id, conf=thresholds["CONF_THRESHOLD"])

        self.state_tracker["play_alarm"] = False

        for result in results[0]:
            # Setup detections for visualization
            detections = Detections(
                        xyxy=results[0].boxes.xyxy.cpu().numpy(),
                        confidence=results[0].boxes.conf.cpu().numpy(),
                        class_id=results[0].boxes.cls.cpu().numpy().astype(int),
                        )
            
            end_time = time.perf_counter()
            self.state_tracker["DROWSY_TIME"] += end_time - self.state_tracker["start_time"]
            self.state_tracker["start_time"] = end_time

            if self.state_tracker["DROWSY_TIME"] >= thresholds["WAIT_TIME"]:
                labels = []
                for _, confidence, _, _ in detections:
                        self.state_tracker["play_alarm"] = True   
                        # Format custom labels
                        label_text = f"Bird {confidence:0.2f}"
                        labels.append(label_text)
                        # Annotate and display frame
                        frame = box_annotator.annotate(frame=frame, detections=detections, labels=labels)
                        plot_text(frame, "ALARM! ALARM", ALM_txt_pos, self.state_tracker["COLOR"])                            
            else:
                    labels = []
                    for _, confidence, _, _ in detections:
                        # Format custom labels
                        label_text = f"Bird {confidence:0.2f}"
                        labels.append(label_text)
                        # Annotate and display frame
                        frame = box_annotator.annotate(frame=frame, detections=detections, labels=labels)
        
        return frame, self.state_tracker["play_alarm"]
