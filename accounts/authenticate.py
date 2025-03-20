# app_name/authenticate.py
from django.contrib.auth.models import User

class CustomAuthBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            # Raw SQL query execution
            from django.db import connection
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT userid, passwd FROM Master#Login WHERE userid = %s AND passwd = %s", 
                    [username, password]
                )
                row = cursor.fetchone()
                
            if row:
                return User(username=username)  # Return simple user object
        except Exception as e:
            print("Error:", e)
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None