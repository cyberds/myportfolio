from datetime import date
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail

class home(View):
    def get(self, request, *args, **kwargs):
        
        context = {

        }
        return render(request, 'main/index.html', context)
    def post (self, request, *args, **kwargs):
        
        pass

def getAge(request):
    pass
#     age=request.GET.get['date']
#     while True:
#         try:
#             input_age=int(age)
#             current_year=date.today().year
#             convert_str = str(input_age)
#             length_of_input_age = len(convert_str)
#             if length_of_input_age > 4:
#                 message = "Please enter proper year"
#             elif input_age>current_year:
#                 message = "You are not yet born."
#             elif input_age == 0 or input_age < 0:
#                 message =  "Please enter proper age"
#             else:
#                 if length_of_input_age == 4:
#                     hundred_years=input_age+100
#                     actual_born_year = input_age
#                     if actual_born_year < 1900:
#                         message = "Your are seem to be the oldest person to alive."
#                         continue
#                     message = "Your Born year is: ",actual_born_year
#                     message = f"The year when you turned 100 years old will be {hundred_years}"
#                     particular_year = int(input("If you want to know your age at that particular year then enter the year: "))
#                     print(f"Your age at {particular_year} year will be", particular_year - actual_born_year)
#                 else:ddef SendFeedback()
#                     remaining_age=100-input_age
#                     hundred_years_old_age=current_year+remaining_age
#                     actual_born_year = current_year - input_age
#                     if actual_born_year < 1900:
#                         print("Your are seem to be the oldest person to alive.")
#                         continue
#                     print("Your Born year is: ", actual_born_year)
#                     print(f"The year when you turned 100 years old will be {hundred_years_old_age}")
#                     particular_year = int(input("If you want to know your age at that particular year then enter the year: "))
#                     print(f"Your age at {particular_year} year will be", particular_year - actual_born_year)
#         except ValueError:
#             print("Please enter only integer values!!!")
#             return JsonResponse({'age' : age})


def sendFeedBack(request):
    if request.method == 'POST':
        sender = request.POST['name']
        sender_email = request.POST ['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
        subject,
        message+"/n From: "+sender_email,
        sender_email,
        ['dskbagain@gmail.com'],
        fail_silently=False,
        )

        context = {
            'sender': sender,
            'message': message,
        }

        return render (request, 'main/thank_you.html', context)
    else:
        return HttpResponse("invalid please check your message and resend")

def thankyou(request):
    
    return render(request, "main/thank_you.html")