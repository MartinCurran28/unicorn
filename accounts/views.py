from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from .models import Post

# Create your views here.

def index(request):
    """Return the index.html file"""
    return render(request, "index.html")
    
    
@login_required    
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect(reverse('login'))
    
def login(request):
    """return a login page"""
    """login_form = UserLoginForm()"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        """check if a form is being submitted"""
        
        if login_form.is_valid():
            user=auth.authenticate(username=request.POST['username'],
                                   password=request.POST['password'])
            """if the login_form is valid and credentials match, then success!"""
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('services'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})


def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            
            else:
                messages.error(request, "Unable to process your registration at this time.")
                
    else:
        registration_form = UserRegistrationForm()
        
    return render(request, 'registration.html', {"registration_form": registration_form})
    

def user_profile(request):
    """The user's profile page. Get user below:"""
    user = User.objects.get()
    return render(request, "profile.html", {"profile": user})
    



from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

def get_posts(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'blogposts.html' template
    """
    
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})

def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})

def create_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})  