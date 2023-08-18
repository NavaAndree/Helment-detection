"""""
Description: This script extracts frames from a video.
Author: Andree Nava 
Date: 17/08/2023
"""""
from datetime import timedelta
import cv2, os
import numpy as np 

SAVING_FRANES_PER_SECOND = 4   # Number of frames to save per second
os.system('cls')               # Clear the terminal
print('Extracting frames from the videos...')

#============================================FUNCTIONS==================================================#
############################## FUNCTIONS FOR EXTRACT DATA FROM A VIDEO ##################################

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
    s = []                             # initialize list to store the durations
    # get the clip duration by dividing number of frames by the number of frames per second
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT)/cap.get(cv2.CAP_PROP_FPS)
    # use np.arange() to make floating-point steps
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s

def counter():
    if not hasattr(counter, 'counter'):
        counter.counter = 0 # Counter for the number of images with faces detected
    counter.counter += 1
    return counter.counter 

def get_frames(cont):
    os.chdir(r'/Users/navan/OneDrive/Escritorio/database/sc')  # Change the current working directory
    # Open the video file
    name_video = names_video(cont)[1]
    cap = cv2.VideoCapture('C:\\Users\\navan\\OneDrive\\Escritorio\\database\\unclassified\\' + name_video) 
    fps = cap.get(cv2.CAP_PROP_FPS)        # Get the frames per second
    saving_frames_per_second = min(fps, SAVING_FRANES_PER_SECOND) # Get the saving frames per second
    # Get the saving frames durations
    saving_frames_durations = get_saving_frames_durations(cap, saving_frames_per_second) 
    # Start the loop
    count = 0

    while True:
        is_read, frame = cap.read()       # Read the frame
        
        if not is_read:
            break                         # If the frame is not read, break the loop
        frame_duration = count / fps      # Calculate the frame duration

        try:
            # Get the earliest duration to save
            closest_duration = saving_frames_durations[0]
        except IndexError:
            break                        # If there are no more durations to save, break the loop

        if frame_duration >= closest_duration:
            # if closest duration is less tha or equals the fame duration,
            # then save the frame
            frame_duration_formatted = format_timedelta(timedelta(seconds=frame_duration))
            name = name_video[:-4] + '_sc_' + str(frame_duration_formatted) + '.jpg'
            ## MODIFIED CODE ##
            n_frame = counter()
            print(f"Accumulated frames: {n_frame}", end="\r")
            ## END MODIFIED CODE ##
            cv2.imwrite(name, frame)    # Save the frame
            # Remove the saved duration from the list
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass

        count += 1                     # Increase the counter
    
    cap.release()                      # Release the video capture
    cv2.destroyAllWindows()            # Destroy all the windows

############################## FUNCTION FOR EXTRACT DATA FROM A FOLDER ##################################

def names_video(cont):
    path = 'C:/Users/navan/OneDrive/Escritorio/database/unclassified'  # Folder where the videos are located
    files_names = os.listdir(path)         # List of the names of the videos
    name = path + '/' + files_names[cont]  # Complete name of the video
    short_name = files_names[cont]         # Short name of the video
    length = len(files_names)              # Number of videos in the folder
    return name, short_name, length

#===========================================MAIN=FUNCTION===============================================#

def main():
    cont_vid = 0                       # Initialize the counter for the elements on the list of videos

    while True:
        get_frames(cont_vid)           # Get the frames from the video
        cont_vid += 1
        print('Video number: ', cont_vid, 'done!')

#========================================CALL=MAIN=FUNCTION=============================================#

if __name__ == '__main__': # 
    main()