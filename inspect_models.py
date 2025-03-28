import os
import django
import inspect

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

def inspect_models():
    print("\n=== INSPECTING MODELS ===")
    
    # Import the models module
    try:
        import quizzes.models
        print("Successfully imported quizzes.models")
        
        # Print all classes defined in the module
        print("\nClasses defined in quizzes.models:")
        for name, obj in inspect.getmembers(quizzes.models):
            if inspect.isclass(obj) and obj.__module__ == 'quizzes.models':
                print(f"  - {name}")
                
                # Print fields for each model
                if hasattr(obj, '_meta'):
                    print(f"    Fields: {[f.name for f in obj._meta.get_fields()]}")
        
        # Check if Quiz model exists and print its instances
        if hasattr(quizzes.models, 'Quiz'):
            Quiz = quizzes.models.Quiz
            quizzes_count = Quiz.objects.count()
            print(f"\nFound {quizzes_count} Quiz instances")
            
            if quizzes_count > 0:
                print("Quiz instances:")
                for quiz in Quiz.objects.all():
                    print(f"  - ID: {quiz.id}, Title: {quiz.title}")
            else:
                print("No Quiz instances found")
                
                # Try to create a quiz
                print("\nAttempting to create a quiz...")
                try:
                    # Get the required fields for Quiz
                    required_fields = {}
                    for field in Quiz._meta.get_fields():
                        if not field.null and not field.blank and not field.auto_created and field.name != 'id':
                            print(f"Required field: {field.name}, type: {field.__class__.__name__}")
                            
                            # Try to provide default values based on field type
                            if field.name == 'title':
                                required_fields[field.name] = 'Sample Quiz'
                            elif field.name == 'description':
                                required_fields[field.name] = 'This is a sample quiz'
                            elif field.name == 'created_at':
                                from django.utils import timezone
                                required_fields[field.name] = timezone.now()
                            elif hasattr(field, 'related_model'):
                                # For foreign keys, try to get or create an instance
                                related_model = field.related_model
                                print(f"  Related model for {field.name}: {related_model.__name__}")
                                
                                # Try to get the first instance or create one
                                try:
                                    instance, created = related_model.objects.get_or_create(
                                        defaults={'name': f'Sample {related_model.__name__}'}
                                    )
                                    required_fields[field.name] = instance
                                    print(f"  {'Created' if created else 'Found'} {related_model.__name__} instance: {instance}")
                                except Exception as e:
                                    print(f"  Error creating {related_model.__name__} instance: {e}")
                    
                    # Create the quiz
                    quiz = Quiz.objects.create(**required_fields)
                    print(f"Created quiz: {quiz.title} (ID: {quiz.id})")
                except Exception as e:
                    print(f"Error creating quiz: {e}")
    except ImportError as e:
        print(f"Error importing quizzes.models: {e}")
    
    # Check the home_page view
    print("\n=== INSPECTING HOME_PAGE VIEW ===")
    try:
        import quizzes.views
        print("Successfully imported quizzes.views")
        
        if hasattr(quizzes.views, 'home_page'):
            print("home_page view exists")
            
            # Print the source code of the home_page view
            import inspect
            print("\nSource code of home_page view:")
            print(inspect.getsource(quizzes.views.home_page))
        else:
            print("home_page view does not exist")
    except ImportError as e:
        print(f"Error importing quizzes.views: {e}")
    
    print("\n=== END INSPECTION ===")

if __name__ == "__main__":
    inspect_models()
