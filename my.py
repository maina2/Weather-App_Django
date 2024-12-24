import requests
from django.shortcuts import render

def get_weather(request):
    api_key = "your_openweathermap_api_key"  # Replace with your API key
    weather_data = None

    if 'city' in request.GET:
        city = request.GET['city']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'City not found'}

    return render(request, 'weather/weather.html', {'weather_data': weather_data})
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_weather, name='get_weather'),
]
import random

class QuizGame:
    def __init__(self, questions_file):
        self.questions_file = questions_file
        self.questions = []
        self.score = 0

    def load_questions(self):
        """Load questions from a text file."""
        try:
            with open(self.questions_file, 'r') as file:
                for line in file:
                    question, answer = line.strip().split('|')
                    self.questions.append({'question': question, 'answer': answer})
        except FileNotFoundError:
            print(f"Error: The file '{self.questions_file}' was not found.")
            exit()

    def ask_question(self):
        """Ask a random question from the list."""
        if not self.questions:
            print("No questions available.")
            return
        question = random.choice(self.questions)
        print("\nQuestion:")
        print(question['question'])
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == question['answer'].lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer was: {question['answer']}")

    def start_game(self):
        """Start the quiz game."""
        print("Welcome to the Quiz Game!")
        self.load_questions()
        while True:
            self.ask_question()
            play_again = input("\nDo you want to answer another question? (yes/no): ").strip().lower()
            if play_again != 'yes':
                break
        print(f"\nGame over! Your final score is: {self.score}")

# File: questions.txt
# Sample content for questions.txt:
# What is the capital of France?|Paris
# Who wrote 'To Kill a Mockingbird'?|Harper Lee
# What is the largest planet in our solar system?|Jupiter

if __name__ == "__main__":
    # Create a QuizGame instance and start the game
    game = QuizGame("questions.txt")
    game.start_game()
