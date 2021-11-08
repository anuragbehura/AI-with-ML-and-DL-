import random
import json
from time import sleep
import torch
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json",'r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#----------------------------------------------------
Name = "Horizon"

from Listen import Listen
from Speak import Say
from Task import InputExecution
from Task import NonInputExecution
from Task import InternetDownSpeed
from Task import InternetUpSpeed
from win10toast import ToastNotifier
from tqdm import trange
import getpass

#---------------------notification--------------------------------------#
toast = ToastNotifier()
toast.show_toast(" Horizon ","Horizon Is Now Activated",duration=10,
icon_path="Horizon.ico")

#---------------------notification--------------------------------------#
#---------------------Username&Password------protected------------------#
username = ("anuragbehura")
password = ("anurag")

inputuser = input("Username: ")
inputpass = getpass.getpass("Password: ")

if inputuser == username:
    print("")
else:
    Say("Invalid Username")
    sleep(5)
    quit()
if inputpass == password:
    Say("Wellcome back, Sir")
    sleep(1)
else:
    Say("Invalid Password")
    sleep(5)
    quit()

Say("--------------------------Let me check all the programs and files--------------------------------")

for i in trange(100):
    sleep(0.2)

Say("Ok, All Good Sir")
#----------------------Username&Password------Protected-------------------#

def Main():

    sentence = Listen()
    result = str(sentence)

    if sentence == "bye":
        exit()

    sentence = tokenize(sentence)
    x = bag_of_words(sentence,all_words)
    x = x.reshape(1,x.shape[0])
    x = torch.from_numpy(x).to(device)

    output = model(x)

    _ , predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])

                if "time" in reply:
                    NonInputExecution(reply)

                elif "date" in reply:
                    NonInputExecution(reply)

                elif "day" in reply:
                    NonInputExecution(reply)

                elif "wikipedia" in reply:
                    InputExecution(reply,result)

                elif "google" in reply:
                    InputExecution(reply,result)

                elif "downloading speed" in reply:
                    InternetDownSpeed(reply)

                elif "uploading speed" in reply:
                    InternetUpSpeed(reply)

                else:
                    Say(reply)

while True:
    Main()

    
