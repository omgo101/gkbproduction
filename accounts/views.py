from django.shortcuts import render, redirect
from django.db import connection

def login_view(request):
    print("login_view called")  # Debug statement
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        with connection.cursor() as cursor:
            cursor.execute("SELECT userid, passwd FROM Master#Login WHERE userid = %s AND passwd = %s", [username, password])
            user = cursor.fetchone()

        if user:
            request.session["user"] = username  # Store session
            return redirect("home")  # Redirect to home page
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")

def home_view(request):
    print("home_view called")  # Debug statement
    if "user" not in request.session:
        return redirect("login")  # Redirect to login if not authenticated
    return render(request, "home.html", {"username": request.session["user"]})

def search_view(request):
    print("search_view called")  # Debug statement
    results = None
    column_names = None
    if request.method == "POST":  # Add missing colon
        rootcardno = request.POST.get("rootcardno")
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Tran#StageHistoryFBMO WHERE ROOTCARDNO = %s", [rootcardno])
            results = cursor.fetchall()
            column_names = [col[0] for col in cursor.description]

    return render(request, 'search.html', {'results': results, 'column_names': column_names})


