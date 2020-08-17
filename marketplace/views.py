from django.shortcuts import render
from django.views import View


class ProfileView(View):
    def get(self: object, request: object) -> object:
        return render(request, template_name='index.html')
