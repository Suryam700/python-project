import os

if __name__ == "__main__":
    print('Welcome to roboSpeaker 1.1, Created by "Suryam Gahoi".')
    print("For intiating robo speaker Enter 'start'.", end=" ")
    allow = input("Enter: ")
    while (allow.lower() == "start" or allow.lower() == "continue"):
        text = input("Enter what you want to speak: ")
        command = f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'
        os.system(command)
        print("For exit the communication. Enter 'exit' otherwise Enter \"continue\" or \"start\"", end=" ")
        allow = input("Enter: ")
    




    