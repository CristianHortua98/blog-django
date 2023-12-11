from applications.home.models import Home

#PROCESO PARA RECUPERAR TELEFONO Y CORREO DEL HOME

def home_contact(request):
    
    home = Home.objects.latest('created')

    return {
        'phone': home.phone,
        'correo': home.contact_email
    }