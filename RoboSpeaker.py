import pyttsx3

if __name__ == '__main__':
    print("Welcome to ROBOSPEAKER created by ALFAIZ SHEIKH")
    while True:
        x = input("Enter anything you want to hear: ")
        if x == "q":
            break
        engin = pyttsx3.init()
        engin.say(x)
        engin.runAndWait()