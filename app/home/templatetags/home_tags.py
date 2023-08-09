import logging
from django import template
from django.conf import settings
from django.templatetags.static import static

logger = logging.getLogger('app')
register = template.Library()


@register.simple_tag(name='get_config')
def get_config(value):
    # get django setting value or return none
    return getattr(settings, value, None)


@register.filter(name='avatar_url')
def avatar_url(user):
    # return discord avatar url from user model
    if user.avatar_hash:
        return f'https://cdn.discordapp.com/avatars/' \
               f'{ user.username }/{ user.avatar_hash }.png'
    else:
        return static('images/assets/default.png')


@register.filter(name='single_type')
def single_type(mime_type):
    # returns the absolute_url from the absolute_uri
    return str(mime_type.split('/', 1)[0]).lower()


@register.filter(name='bytes_human')
def bytes_human(num):
    # TODO: Update JSON to Include this...
    suffix = 'B'
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


# @register.filter(name='stats_process')
# def stats_process(data, name):
#     shorts = ShortURLs.objects.get_request(request)
#     # stats = FileStats.objects.filter(user_id=2)
#     stats = FileStats.objects.get_request(request)
#     log.debug('stats: %s', stats)
#     days, files, size = [], [], []
#     # {"types": {}, "size": 0, "count": 0, "human_size": "0.0 B"}
#     # TODO: Move to Template Tag for Template Fragment Caching
#     for stat in reversed(stats):
#         days.append(f'{stat.created_at.month}/{stat.created_at.day}')
#         files.append(stat.stats['count'])
#         size.append(stat.stats['size'])
#     context = {'stats': stats, 'days': days, 'files': files, 'size': size, 'shorts': shorts}
#     log.debug('context: %s', context)
#     return render(request, 'stats.html', context=context)
