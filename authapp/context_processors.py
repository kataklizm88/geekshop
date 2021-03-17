from basket.models import Basket

def user_status(request):
    user = request.user
    if user.is_authenticated:
        status = "авторизован"
    else:
        status = "Не авторизован"
    return {'status':status}


