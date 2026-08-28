from django.conf import settings
from disturbance import helpers
from disturbance.components.main.utils import get_template_group


def disturbance_url(request):
    is_apiary_admin = ''
    TERMS = "/know/online-disturbance-apiary-terms-and-conditions"

    is_officer = False
    is_admin = False

    if request.user.is_authenticated:
        is_apiary_admin = helpers.is_apiary_admin(request)

    return {
        'APIARY_SEARCH': '/external/payment',
        'APIARY_CONTACT': '/contact-us',
        'APIARY_TERMS': TERMS,
        'TEMPLATE_GROUP': get_template_group(request),
        'SYSTEM_NAME': settings.SYSTEM_NAME,
        'IS_OFFICER': is_officer,
        'IS_ADMIN': is_admin,
        'IS_APIARY_ADMIN': is_apiary_admin,
        'PUBLIC_URL': settings.PUBLIC_URL
    }


def template_context(request):
    """Pass extra context variables to every template.
    """
    context = disturbance_url(request)
    return context
