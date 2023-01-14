from django import template
from apps.contact.forms import ContactForm

register = template.Library()


@register.inclusion_tag("contact/form.html")
def contact_form():
    return {"contact_form": ContactForm()}