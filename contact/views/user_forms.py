from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


from contact.forms import RegisterForm, RegisterUpdateForm

def register(request):

    form = RegisterForm()

    #messages.info(request, 'Um texto qualquer')
    #messages.success(request, 'Um texto qualquer')
    #messages.warning(request, 'Um texto qualquer')
    #messages.error(request, 'Um texto qualquer')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:login')


    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

def login_view(request):

    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            user = form.get_user()
            messages.success(request, "Logado com sucesso")
            auth.login(request, user)
            print(user)
            return redirect('contact:index')
        messages.error(request, "Login inválido!") #se retornar, ele nao entra em erro


    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }    
    )

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')


@login_required(login_url='contact:login') # isso redireciona para o login se nao estiver logado
def user_update(request):

    form = RegisterUpdateForm(instance=request.user)


    if request.method != 'POST': #SE nao for POST eu retorno o form
        return render(
            request,
            'contact/register.html',
            {
                'form': form
            }
        )
    
    form = RegisterUpdateForm(data =request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/register.html',
            {
                'form': form
            }
        )
    
    form.save()
    messages.success(request, 'Usuário atualizado com sucesso')