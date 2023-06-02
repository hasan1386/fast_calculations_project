from django import template

register = template.Library()


@register.simple_tag
def is_exist(model_name, model, check, *args, **kwargs):
    if model_name == 'is_read':
        model = model.filter(lesson__pk=check).first()
    else:
        model = model.filter(exercise__pk=check).first()
    if model is None:
        return ''
    return 'text-success'
