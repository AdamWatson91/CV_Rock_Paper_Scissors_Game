import cv2
from keras.models import load_model
import numpy as np
import random
import time
play_until = 3
all_choice = ['Paper','Rock','Scissors','None']
player_score = 0
computer_score = 0
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0) # object to control the video input
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) # DOES THIS CREATE A EMPTY ARRAYconverts image to an array 1 = one image per iteration, 224 = Width in pixels, 224 = height in pixels, 3 = channel that converts image into RGB values
started = False
elasped = 0
player_choice = ""
result = ""
computer_choice = ""
while player_score < play_until and computer_score < play_until: # This means it runs forever
    ret, frame = cap.read() # ret is boolean variable that returns true if the frame is available from the capture. frame (length is 480 but why) is the image array vector captured based on the default frames per second defined explicitly or implicitly
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA) # resizes the image capture in the iteration to match that of the array data
    image_np = np.array(resized_frame) # converts the resized frame into an array
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image # WHAT IS THIS DOING
    prediction = model.predict(data) # Captures the prediction from the model and stores it in the prediction variable
    cv2.putText(frame,
            str(round(elasped,2)),
            (35, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, 
            (0, 255, 255), 
            2, 
            cv2.LINE_4)
    cv2.putText(frame,
            "You "+str(player_score)+" - "+str(computer_score)+" Computer",
            (160, 460), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, 
            (0, 255, 255), 
            2, 
            cv2.LINE_4)
    cv2.putText(frame,
            player_choice,
            (20, 230), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, 
            (0, 255, 255), 
            2, 
            cv2.LINE_4)
    cv2.putText(frame,
            result,
            (150, 250), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, 
            (0, 255, 255), 
            2, 
            cv2.LINE_4)
    cv2.putText(frame,
            computer_choice,
            (480, 230), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, 
            (0, 255, 255), 
            2, 
            cv2.LINE_4)
    cv2.imshow('frame', frame) # This just displays the video capture to the user - note that the model still works without this!
    player_choice = all_choice[np.argmax(prediction)] # This is the user choice
    computer_choice = random.choice(all_choice) #this is the computer choice
    #here i want to establish a user input to start each round
    #if cv2.waitKey(100000000) & 0xFF == ord('a'):
        #started == True
        #if started == True:

    # if started == False:
    #     start_time = time.time()
    #     started = True
    # elasped = time.time() - start_time
    if cv2.waitKey(1) & 0xFF == ord('a'):
        started = True
    
    # if elasped > 5:
    if started == True:
        print(player_choice)
        if  player_choice == computer_choice:
            print(f"Both players selected {player_choice}. This round is a draw.")
        elif  player_choice == "None":
            print("No choice recognised try again.")
        elif player_choice == "Rock":
            if computer_choice == "Scissors":
                print("Rock smashes scissors! You win this round.")
                player_score += 1
            else:
                print("Paper covers Rock! You lose this round.")
                computer_score += 1
        elif player_choice == "Paper":
            if computer_choice == "Rock":
                print("Paper covers Rock! You win this round.")
                player_score += 1
            else:
                print("Scissors cuts paper! You lose this round.")
                computer_score += 1
        elif player_choice == "Scissors":
            if computer_choice == "Paper":
                print("Scissors cuts paper! You win this round.")
                player_score += 1
            else:
                print("Rock smashes scissors! You lose this round.")
                computer_score += 1
                #Show score to keep track of progress
        print("The current score is: You "+str(player_score)+" - "+str(computer_score)+" Computer")
        started = False
        computer_choice = ""
    if cv2.waitKey(1) & 0xFF == ord('q'): # This is the logic that enables cancelling the program when q is pressed on keyboard
        break # Gets out of the loop if above condition is met
    #When game ends confirm outcome of the game`
if player_score == play_until:
    result = "Congratulations you win the game"
else:
    result = "Unfortunately you lost the game"
print(result)           
# After the loop release the cap object
cap.release()
#Destroy all the windows
cv2.destroyAllWindows()

#ENHANCEMENTS:
#DISPLAY THE COMPUTER CHOICE AT POINT OF
#IMPROVE MODEL ACCURACY
#TAKE A APPROCH THAT REVIEWS THE PROBABILITY OF THE PAST FEW PREDICTIONS TO SURE UP FURTHER HOWVER I THINK IMPROVING THE MEODEL IF BETTER
#USER PUSHES WHEN THEY WANT TO PLAY EACH ROUND
#PRINT THE RESULT OF EACH ROUND UNTIL THE NEW ROUND IS STARTED
#PRINT THE FINAL RESULT ON THE SCREEN - START THE TIMER, STOP THE PREDICTION TEXT
#USER CHOOSE TO EXIT THE GAME OR START AGAIN ONCE FINISHED RATHER THAN IT CLOSING SUDDENLY



