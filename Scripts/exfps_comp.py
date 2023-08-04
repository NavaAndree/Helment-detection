# Description: This program extracts frames from a video and compares them to determine if they 
# are similar or not.

from datetime import timedelta
import cv2, shutil, os, random
import numpy as np 

SAVING_FRANES_PER_SECOND = 4   # Number of frames to save per second
os.system('cls')               # Clear the terminal

#============================================FUNCTIONS==================================================#
########################### FUNCTIONS FOR EXTRACTING FRAMES FROM A VIDEO ################################

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

def get_frames():
    os.chdir(r'C:/Users/navan/Videos/sc')  # Change the current working directory
    # Open the video file
    cap = cv2.VideoCapture('C:\\Users\\navan\\OneDrive\\Documentos\\TESIS\\Desarrollo-Previo\\Code\\videos_sc\\p16.mp4') 
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
            name = 'p1_sc_' + str(frame_duration_formatted) + '.jpg'
            cv2.imwrite(name, frame)    # Save the frame
            # Remove the saved duration from the list
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass

        count += 1                     # Increase the count
    
    cap.release()                      # Release the video capture
    cv2.destroyAllWindows()            # Destroy all the windows

############################### FUNCTIONS FOR THE COMPARISON #############################################

def cal_object_area(imagen_segmentada):
    # Find contours of objects in the segmented image
    contours, _ = cv2.findContours(imagen_segmentada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    object_area = []                    # initialize list to store areas of objects
    for contour in contours:            # Calculate the area of each object and add it to the list
        area = cv2.contourArea(contour)
        object_area.append(area)

    return object_area

def copy_file(origin, destination):
    try:
        shutil.copy(origin, destination)   # Copy the content of source to destination
        #print("File copied successfully.")
    except FileNotFoundError:              # If source and destination are same
        print(f"File {origin} not found.")
    except PermissionError:                # If destination is write protected
        print("Permission denied.")
    except Exception as aa:                # For other errors
        print(f"Error occurred while copying file: {aa}")

def names(cont):
    path = 'C:/Users/navan/Videos/sc'      # Path of the folder where the images are located
    files_names = os.listdir(path)         # List of the names of the images
    name = path + '/' + files_names[cont]  # Complete name of the image
    short_name = files_names[cont]         # Short name of the image
    length = len(files_names)              # Number of images in the folder
    return name, short_name, length


#===========================================MAIN=FUNCTION===============================================#

def main():
    get_frames()                         # Get the frames from the video
    cont=0
    print(names(cont)[2])
    while True:
        # Read two frames
        img1 = cv2.imread(names(cont)[0], cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(names(cont+1)[0], cv2.IMREAD_GRAYSCALE)
        diff = cv2.subtract(img1, img2)   # Difference between images
        result = not np.any(diff)         # Compare the difference between images

        if result is True:
            print('The images are equal')
        else:
            cv2.imwrite('diff.jpg', diff)
            print('The images are different')

        _, thresh = cv2.threshold(diff,80,255,cv2.THRESH_BINARY) # Thresholding, to segment the image
        object_area = cal_object_area(thresh)    # Calculate the area of the objects in the segmented image
        total_areas = sum(object_area)           # Calculate the total of areas by adding all the areas
        
        percentage = (total_areas * 100) / (img1.shape[0] * img1.shape[1]) # Calculate the percentage of similarity
        percentage = 100 - percentage

        if percentage < 99.0:
            # Copy the content of source to destination
            source = names(cont+1)[0]
            destination = "C:/Users/navan/OneDrive/Documentos/TESIS/Scripts/prueba"
            copy_file(source, destination)

        cont += 1

        if cont == names(cont)[2]-1:
            break

        print(f"Total area: {total_areas:.2f} pixels")
        print(f"Similarity: {percentage:.2f}%")
        print(f"Frame: {cont}")

        # cv2.imshow('diff',thresh)
        # cv2.waitKey(0)

#========================================CALL=MAIN=FUNCTION=============================================#

if __name__ == '__main__': # 
    main()
