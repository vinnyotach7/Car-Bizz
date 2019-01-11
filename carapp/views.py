from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,ImageForm,ProfileForm,EngineForm,UsabilityForm,BodyForm,CommentForm,EditProfileForm,NewsLetterForm
from .models import Profile,Image,Comment,Likes,Location,Rider,Driver,UsabilityRating,EngineRating,BodyRating,NewsLetterRecipients
from django.http import JsonResponse
from .email import send_welcome_email

@login_required(login_url='/accounts/login/')
def home(request):
  if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('home')
  else:
        form = NewsLetterForm()
  current_user = request.user
  images = Image.objects.all()
  comments = Comment.objects.all()
  likes = Likes.objects.all()
  profile = User.objects.all()
  return render(request, 'home.html',locals())


@login_required(login_url='/accounts/login/')
def rate_usability(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    if request.method == 'POST':
        form = UsabilityForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.image = image
            rate.user_name = request.user
            rate.profile = request.user.profile

            rate.save()
        return redirect('image')

    return render(request, 'image.html')

@login_required(login_url='/accounts/login/')
def rate_engine(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    if request.method == 'POST':
        form = EngineForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.image = image
            rate.user_name = request.user
            rate.profile = request.user.profile

            rate.save()
        return redirect('image')
    else:
        form = EngineForm()

    return render(request, 'image.html',locals())


@login_required(login_url='/accounts/login/')
def rate_body(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    if request.method == 'POST':
        form = BodyForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.image = image
            rate.user_name = request.user
            rate.profile = request.user.profile

            rate.save()
        return redirect('image')

    return render(request, 'image.html')

@login_required(login_url='/accounts/login/')
def image(request,image_id):
    form=EngineForm()
    form=UsabilityForm()
    form=BodyForm
    comments = Comment.objects.all()
    likes = Likes.objects.all()
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html",locals())

@login_required(login_url='/accounts/login/')
def upload_image(request):
    profile = Profile.objects.all()
    for profile in profile:
      if request.method == 'POST':
          form = ImageForm(request.POST, request.FILES)
          if form.is_valid():
              add=form.save(commit=False)
              add.profile = profile
              add.user = request.user
              add.save()
              return redirect('home')
      else:
          form = ImageForm()


      return render(request,'upload.html',locals())

@login_required(login_url='/accounts/login/')
def search_results(request):
  if 'image' in request.GET and request.GET["image"]:
    form=EngineForm()
    form=UsabilityForm()
    form=BodyForm()
    name = request.GET.get("image")
    searched_images = Image.search_images(name)
    message = f"{name}"

    return render(request, 'search.html',{"message":message,"images":searched_images,"form":form})

  else:
    message = "You haven't searched for anything"
    return render(request, 'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def profile(request, user_id):
    '''
    Function that enables users see their profile
    '''
    form=EngineForm()
    form=UsabilityForm()
    form=BodyForm()
    title = "Profile"
    images = Image.get_image_by_id(id= user_id).order_by('-posted_on')
    profiles = Profile.objects.get(user_id=user_id)
    users = User.objects.get(id=user_id)

    return render(request, 'profile/profile.html',locals())

    
@login_required(login_url='/accounts/login/')
def edit_profile(request):
    '''
    Function that enables one to edit their profile details
    '''
    current_user = request.user
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('home')
    else:
        form = EditProfileForm()
    return render(request, 'profile/edit_profile.html', locals())

@login_required(login_url='/accounts/login/')
def comment(request, image_id):
    images = get_object_or_404(Image, pk=image_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.image = images
            comment.save()
    return redirect('home')


@login_required(login_url='/accounts/login/')
def like(request, image_id):
    current_user = request.user
    liked_image=Image.objects.get(id=image_id)
    new_like,created= Likes.objects.get_or_create(who_liked=current_user, liked_image=liked_image)
    new_like.save()

    return redirect('home')