from .forms import LogInForm, SignUpForm

def logInForm(request):
    return {'logInForm':LogInForm}

def signUpForm(request):
    return {'signUpForm':SignUpForm}