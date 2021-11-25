from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

monthly_challanges = {
    "january": "Eat no meat for the entire month",
    "february": "Wake up at 6 o'clock every day",
    "march": "Learn Django in details",
    "april": "April text",
    "may": "Some Text for may"
}


def monthly_challange_by_number(requests, month):
    months = list(monthly_challanges.keys())
    if month > len(months):
        return HttpResponseNotFound("This month is not supported")
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challanges/" + redirect_month)


def monthly_challange(request, month):
    try:
        challange_text = monthly_challanges[month]
        return HttpResponse(challange_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
