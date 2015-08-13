import datetime

from django.http import HttpResponse
from django.utils.timezone import utc

from stories.models import Story


def score(story, timebase=120):
    # ToDo: Confirm Score is Valid
    # His -1 factor generates a complex number which
    # causes the sorting to fail because it expects
    # a float().  To fix this, I just erased the '- 1'
    # which sovled the problem, but I don't KNOW that it
    # still generates a valid score.

    # points = int((story.points - 1)**0.8)
    points = int(story.points**0.8)
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    age = int((now - story.created_at).total_seconds())/60
    return points/(age*timebase)**1.8


def top_stories(top=180, consider=1000):
    latest_stories = Story.objects.all().order_by('-created_at')[:consider]
    print('Latest Stories: %s' % latest_stories)
    print('Score: %s' % score)
    ranked_stories = sorted(latest_stories, key=score, reverse=True)
    return ranked_stories[:top]


def index(request):
    stories = top_stories(top=30)
    response = '''
    <html>
    <head>
        <title>Tuts+ News</title>
    </head>
    <body>
        <ol>
        %s
        </ol>
    </body>
    </html>
    ''' % '\n'.join(['<li>%s</li>' % story.title for story in stories])
    return HttpResponse(response)
