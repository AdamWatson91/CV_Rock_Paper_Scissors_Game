import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0) # object to control the video input
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) # DOES THIS CREATE A EMPTY ARRAYconverts image to an array 1 = one image per iteration, 224 = Width in pixels, 224 = height in pixels, 3 = channel that converts image into RGB values
while True: # This means it runs forever
    ret, frame = cap.read() # ret is boolean variable that returns true if the frame is available from the capture. frame (length is 480 but why) is the image array vector captured based on the default frames per second defined explicitly or implicitly
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA) # resizes the image capture in the iteration to match that of the array data
    image_np = np.array(resized_frame) # converts the resized frame into an array
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image # WHAT IS THIS DOING
    prediction = model.predict(data) # Captures the prediction from the model and stores it in the prediction variable
    cv2.imshow('frame', frame) # This just displays the video capture to the user - note that the model still works without this!
    # Press q to close the window
    print(prediction) # This is printing out the probability prediction for each of the 4 classes for the iteration. each item can be acess with prediction [0][0] (this is the first item)
    if cv2.waitKey(1) & 0xFF == ord('q'): # This is the logic that enables cancelling the program when q is pressed on keyboard
        break # Gets out of the loop if above condition is met
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()