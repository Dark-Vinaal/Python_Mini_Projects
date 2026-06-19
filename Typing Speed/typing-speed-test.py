import time

sentence = "This is a simple typing test built using python programming language"

print("TYPING SPEED TEST ")
print("---------------------")
print("***** Type The Following Sentence *****")
print(sentence)

input("Press Enter when you are ready...")

start_time = time.time()
typed_text = input("/nStart Typing : ")
end_time = time.time()
time_taken = end_time - start_time

words = len(sentence.split())
speed = (words / time_taken) * 60

print("Time Taken ", round(time_taken, 2), "seconds")
print("Typing Speed ", round(speed, 2), "WPM")

if typed_text == sentence:
    print("Accuracy : 100% ")
else:
    print("Accuracy : Found Some Mistakes ")

print("----- Typing Speed Test Finished ----- ")