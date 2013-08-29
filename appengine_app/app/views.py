from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.http import Http404
from django.template import RequestContext


def index(request):
    context = {
        "active_menu": "index",
    }

    return render_to_response('pages/index.html', context,
                              context_instance=RequestContext(request))


def agenda(request):
    context = {
        "active_menu": "agenda",
    }

    return render_to_response('pages/agenda.html', context,
                              context_instance=RequestContext(request))


def location(request):
    context = {
        "active_menu": "location",
    }

    return render_to_response('pages/location.html', context,
                              context_instance=RequestContext(request))


def speakers(request):
    context = {
        "active_menu": "speakers",
    }

    return render_to_response('pages/speakers.html', context,
                              context_instance=RequestContext(request))


def photos(request):
    context = {
        "active_menu": "photos",
    }

    return render_to_response('pages/photos.html', context,
                              context_instance=RequestContext(request))
