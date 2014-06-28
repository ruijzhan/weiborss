from django.http import HttpResponse
from django.shortcuts import render_to_response
import sys
from authentication import Authentication
from status import Status


def qiudog(request):
    statuses = Status.get_friends_statuses(100)
    for status in statuses:
        for pic in status.pic_urls:
            pic.thumbnail_pic = pic.thumbnail_pic.replace('thumbnail','large')
        if hasattr(status,'retweeted_status'):
            for pic in status.retweeted_status.pic_urls:
                pic.thumbnail_pic = pic.thumbnail_pic.replace('thumbnail','large')
    lastBuildDate = statuses[0].created_at

    return render_to_response('rss.xhtml',locals())
