BEFORE_DJANGO_APPS = (
    'tenant_schemas',
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'djflow.apps.flow',
    'djflow.apps.website',
    'djflow.apps.security',
    'djflow.apps.tenant',
)

THIRD_PARTY_APPS = (
    'solo',
)

TENANT_APPS = (
    'djflow.apps.flow',
    'djflow.apps.website',
    'djflow.apps.security',
)

SHARED_APPS = (
    'tenant_schemas',
    'djflow.apps.tenant',
) + DJANGO_APPS

INSTALLED_APPS = SHARED_APPS + TENANT_APPS + THIRD_PARTY_APPS
