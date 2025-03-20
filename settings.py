DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sql_server.pyodbc',
        'NAME': 'GKBPRODUCTION',
        'USER': 'sa',
        'PASSWORD': 'Sql123',
        'HOST': 'GKB',
        'PORT': '1433',  # Default is 1433
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'TrustServerCertificate': 'yes',
        },
    }
}
