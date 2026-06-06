"""Basic document layout detection
Inspired by dormant document layout analysis tools
"""
import cv2
import numpy as np

def find_text_regions(image, min_width=50, min_height=20):
    """Simple region detection using contours"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    regions = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > min_width and h > min_height:
            regions.append({"x": x, "y": y, "width": w, "height": h})
    return regions