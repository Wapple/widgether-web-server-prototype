from urllib.parse import urlparse, urljoin
from flask import request, redirect, url_for

def is_safe_url(target):
    ref = urlparse(request.host_url)
    test = urlparse(urljoin(request.host_url, target))
    return test.scheme in ('http', 'https') and ref.netloc == test.netloc

def get_redirect_target():
    target = request.values.get('next')
    if is_safe_url(target):
        return target
    else:
        return None

def redirect_back(endpoint, **args):
    target = get_redirect_target()
    if not target:
        target = url_for(endpoint, **args)
    return redirect(target)