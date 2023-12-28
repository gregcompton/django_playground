from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'cookies/index.html')


def setting_cookie(request):
    company_id = {"company_id": 25}
    response = render(request, 'cookies/set_cookie.html', company_id)
    response.set_cookie('company_id', company_id["company_id"], 30,
                        samesite="LAX", secure=True, httponly=True)  # key, value, expiration in seconds
    return response


def getting_cookie(request):
    company_id = None
    msg = None
    try:
        company_id = request.COOKIES['company_id']
    except Exception as e:
        msg = f'Error retrieving company_id: {e}'
    ctx = {'company_id': company_id, 'msg': msg}
    return render(request, 'cookies/get_cookies.html', ctx)


def updating_cookie(request):
    new_company_id = {"new_company_id": 50}
    response = render(request, 'cookies/update_cookie.html', new_company_id)
    response.set_cookie('company_id', 50, 30,
                        samesite="LAX", secure=True, httponly=True)
    return response


def redirect_update_cookie(request):
    response = redirect('cookies:get_cookie')
    response.set_cookie('company_id', 75, 30,
                        samesite="LAX", secure=True, httponly=True)
    return response


def deleting_cookie(request):
    response = render(request, 'cookies/delete_cookie.html')
    response.delete_cookie('company_id')
    return response
