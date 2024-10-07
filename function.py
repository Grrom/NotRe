from dotenv import load_dotenv

load_dotenv()

def do_something(request):
    print(request.data)