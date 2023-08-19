# Description: This script extracts frames from a video. The intention here is to create a better code than
# the original exfps.py (by Jaime) so we can work with it, and add functions to compare the frames, but that is
# on another code.

from datetime import timedelta
import cv2, os
import numpy as np

SAVING_FRAMES_PER_SECOND = 4    # 4 frames per second
os.system('cls')                # Clear the terminal

def format_timedelta(td):
    """Utility function to format timedelta objects in a cool way (e.g 00:00:20.05) 
    omitting microseconds and retaining milliseconds"""
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return result + ".00".replace(":", "-")
    ms = int(ms)
    ms = round(ms/1e4)
    return f"{result}.{ms:02}".replace(":", "-")

def get_saving_frames_durations(cap, saving_fps):
    """A function that returns the list of durations where to save the frames"""
    s = []
    # get the clip duration by dividing number of frames by the number of frames per second
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT)/cap.get(cv2.CAP_PROP_FPS)
    # use np.arange() to make floating-point steps
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s


def main():  
    #os.chdir(r'C:\\Users\\navan\\Videos\\sc') # cambiar directorio
    os.chdir(r'/Users/navan/OneDrive/Escritorio/database/sc')
    # open the video
    cap = cv2.VideoCapture('C:\\Users\\navan\\OneDrive\\Escritorio\\database\\unclassified\\p1.mp4') 
    fps = cap.get(cv2.CAP_PROP_FPS) # get the frames per second
    # if the SAVING_FRAMES_PER_SECOND is above video FPS, then set it to FPS (as maximum)
    saving_frames_per_second = min(fps,SAVING_FRAMES_PER_SECOND) # get the saving frames per second
    # get the list of duration spots to save
    saving_frames_durations = get_saving_frames_durations(cap,saving_frames_per_second)
    
    count = 0

    while True:
        is_read, frame = cap.read()
	
        if not is_read:
            # break out of the loop if there are no frames to read
            break
        
        frame_duration = count /fps                       # get the duration by dividing the frame count by the FPS
        
        try:
            closest_duration = saving_frames_durations[0] # get the earliest duration to save
        except IndexError:
            # the list is empty, all duration frames were saved
            break
        
        if frame_duration >= closest_duration:
            # if closest duration is less than or equals the frame duration, 
            # then save the frame
            frame_duration_formatted = format_timedelta(timedelta(seconds=frame_duration)) # format the duration
            name= 'p16_sc_'+str(frame_duration_formatted)+'.jpg' # name of the frame
            cv2.imwrite(name, frame)
            # drop the duration spot from the list, since this duration spot is already saved
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass
        
        count += 1 # increment the frame count
    
    cap.release()
    cv2.destroyAllWindows

if __name__ == '__main__':
    main()