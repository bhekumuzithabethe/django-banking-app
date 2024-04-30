from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect

#Resticting users from accessing pages they shouldn't

class LoginCheckMiddleware(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename = view_func.__module__
        user = request.user
        if user.is_authenticated:
            #Admin can only access adminpage and cannot access leaner nor staff pages this can be done by this function
            if user.user_type == '1':
                if modulename == 'bank_mananger.views':
                    pass
                elif modulename == 'core.views':
                    pass
                else:
                    return redirect(reverse('adminpage'))

            elif user.user_type == '2':
                if modulename == 'consultant.views':
                    pass
                elif modulename == 'core.views':
                    pass
                else:
                    return redirect(reverse('consultant'))
                    
            elif user.user_type == '3':
                if modulename == 'client.views':
                    pass
                elif modulename == 'core.views':
                    pass 
                else:
                    return redirect(reverse('client'))
        else:
            if request.path == reverse('dologin') or modulename == 'django.contrib.auth.views' or modulename == 'core.views':
                pass
            else:
                return redirect(reverse('dologin'))
        