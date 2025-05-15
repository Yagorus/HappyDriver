import re

def modify_home_page_view(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Add debug prints to the home_page function
    pattern = r'def home_page\(request\):'
    replacement = r'''def home_page(request):
    # Debug information
    print("\n=== HOME PAGE VIEW CALLED ===")
    try:
        from quizzes.models import Quiz
        latest_quiz = Quiz.objects.order_by('-created_at').first()
        print(f"Latest quiz: {latest_quiz}")
        all_quizzes = Quiz.objects.all()
        print(f"All quizzes count: {all_quizzes.count()}")
        for quiz in all_quizzes:
            print(f"  - {quiz.id}: {quiz.title}")
    except Exception as e:
        print(f"Error in debug code: {e}")'''
    
    modified_content = re.sub(pattern, replacement, content)
    
    # Fix the latest_quiz.title reference if it exists
    if 'latest_quiz.title' in modified_content:
        pattern = r'latest_quiz\.title'
        replacement = r'latest_quiz.title if latest_quiz else "No quizzes available"'
        modified_content = re.sub(pattern, replacement, modified_content)
    
    with open(file_path, 'w') as file:
        file.write(modified_content)
    
    print(f"Modified {file_path} to add debugging")

modify_home_page_view('/app/quizzes/views.py')
