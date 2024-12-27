from model_response import respond
from models import model
import time
from variable_initialize import should_run, tasks, listeningToTask, askingAQuestion

def perform_command(command):
    global tasks
    global listeningToTask
    global askingAQuestion
    global should_run
    
    if command:
        print("Command: ", command)
        respond("Thinking...")  # Notify the user you're processing the question
            
        print("User command: ", command)
        output = model.generate(command, max_tokens=500)
            
        if output:  # Check if the model produced output
            print("Output: ", output)
            respond(output)  # Respond with the generated output only once
        
        if "exit" in command:
            should_run = False
            print(should_run)
    
    # Add a short delay to prevent quick re-triggering of the same command
    time.sleep(1)  # You can adjust this based on your requirements