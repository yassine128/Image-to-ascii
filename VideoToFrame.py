# This file will create multiple txt file for each frame of a video

import cv2
import os

def VideoToFramw(Video_Path: str, Video_name: str) -> None:
	"""
	:param Video_Path: Path de la video
	:param Video_name: Nom de la video dans le path
	:return: None
	"""
	capture = cv2.VideoCapture(f"{Video_Path}/{Video_name}")
	i = 0
	while capture.isOpened():
		ret, frame = capture.read()
		if not ret:
			break
		cv2.imwrite(f"AllFrames/frame{i}.jpg", frame)
		i += 1
	
	capture.release()
	cv2.destroyAllWindows()

VideoToFramw("C:/Users/Yassine/Documents/video", "testVideo.mp4")