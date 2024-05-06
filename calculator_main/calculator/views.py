from django.shortcuts import render

def home(request):
    return render(request, 'calculator/home.html')

def calculate(request):
    if request.method == 'GET':
        num1 = float(request.GET.get('num1', 0))
        num2 = float(request.GET.get('num2', 0))
        operation = request.GET.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero!"
        else:
            result = "Error: Invalid operation!"

        return render(request, 'calculator/result.html', {'result': result})
    else:
        return render(request, 'calculator/home.html')
