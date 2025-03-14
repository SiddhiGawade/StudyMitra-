from django.http import HttpResponse
from .navbar import get_navbar

def hello_python(request):
    return HttpResponse("Hello Python")

def home(request):
    navbar = get_navbar()
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <title>Home</title>
    </head>
    <body>
        {navbar}
        <div class="container mx-auto mt-4">
            <h1 class="text-3xl font-bold">Welcome to the Home Page</h1>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mt-6">
                <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300">
                    <h2 class="text-xl font-bold mb-2">Past Exam Papers</h2>
                    <p>Access previous exam papers to practice and prepare.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300">
                    <h2 class="text-xl font-bold mb-2">Summarize the content</h2>
                    <p>Get concise summaries of your study materials.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300">
                    <h2 class="text-xl font-bold mb-2">Assessment & Quizzes</h2>
                    <p>Test your knowledge with assessments and quizzes.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300">
                    <h2 class="text-xl font-bold mb-2">Progress Tracking</h2>
                    <p>Track your study progress and performance.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """)
