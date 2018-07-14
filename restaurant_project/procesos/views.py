from django.shortcuts import render
from procesos.forms import PerfilDeUsuarioForm, UsuarioForm 
# Create your views here.

def registro_usuario(request):
    registered = False

    if request.method == 'POST':
        user_form = UsuarioForm(data=request.POST)
        profile_form = PerfilDeUsuarioForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.usuario = user

            if 'foto_de_perfil' in request.FILES:
                profile.foto_de_perfil = request.FILES['foto_de_perfil']
            
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UsuarioForm()
        profile_form = PerfilDeUsuarioForm()

    context_dict = {
        "registered": registered,
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(request, 'procesos/registro_usuario.html', context=context_dict)