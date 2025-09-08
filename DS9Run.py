# THis is the main script to run the application
import sys
import time


class player_Selct_Job:
    def Player_Job():
        jobs = {
            "1": "Command Prof.",
            "2": "Engineering Prof.",
            "3": "Medical Prof.",
            "4": "Science Prof.",
            "5": "Security Prof."
        }
        print(jobs)

        job_choice = input("Enter the number of your profession ")
        if job_choice in jobs:
            print(f"You have selected: {jobs[job_choice]}")
        else:
            print("Invalid choice. Please select a valid profession.")
            player_Selct_Job.Player_Job()      
        

class MainApp:
    def loading_Bar(Length):
        for i in range(Length):
            sys.stdout.write("\r")
            sys.stdout.write("Loading: [{:<{}}] {:.0f}%".format('=' * i, Length, (i / Length) * 100))
            sys.stdout.flush()
            time.sleep(0.1)
        print()
    def run():
        print("Running DS9 SIM Application ...")



if __name__ == "__main__":
    MainApp.loading_Bar(30)
    print("Game Started")
    print("Welcome to the DS9 SIM Application")
    player_Selct_Job.Player_Job()


    
    
    
