from django.shortcuts import redirect, render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404

# Views are equivalent to controllers in MVC architecture
def index(request):
    return render(request, 'index.html')

# list all tweets
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at') # Get all tweets from DB
    # Render the tweet_list.html template with the tweets
    return render(request, 'tweet_list.html', {'tweets': tweets})

# create a new tweet
def tweet_create(request):
    if request.method == 'POST': # Check request method
        form = TweetForm(request.POST, request.FILES)  # Create a new form with the POST data
        if form.is_valid():
            tweet = form.save(commit=False) # Save the form data to the tweet object
            tweet.user = request.user   # Set the user of the tweet to the current
            tweet.save()    # Save the tweet to the database
            return redirect('tweet_list')
    else:
        form = TweetForm()
    # Render the form on GET request (Initial request)
    return render(request, 'tweet_form.html', {'form': form})

def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)    # user = request.user is added to ensure only valid user can edit tweet
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)   # instance = tweet is used to update the tweet
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    # Render the form on GET request (Initial request)
    return render(request, 'tweet_form.html', {'form': form})

def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)    # user = request.user is added to ensure only valid user can delete tweet
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    # Render the form on GET request (Initial request)
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})