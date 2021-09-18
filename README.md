# Distance-of-Hand
An OpenCV program to find distance of hand from the Camera

Place your Hand at a distance of 30cm from the camera and Configure to recieve distances of next measurements. 
Later the user can hardcode their own values.

Uses trigonometry, compares ratios of, initial and final pixel length from Wrist [0] to Middle_F_MCP [9] (Refer Image), to the configured distance, giving a prediction of the distance the hand.
