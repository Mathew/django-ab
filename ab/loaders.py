try:
    from django.template.loaders.filesystem import load_template_source as default_template_loader
except ImportError:
    from django.template.loaders.filesystem import Loader
    loader = Loader()
    default_template_loader = loader.load_template_source

from ab.middleware import get_current_request


def load_template_source(template_name, template_dirs=None,
    template_loader=default_template_loader):
    """If an Experiment exists for this template use template_loader to load it."""
    request = get_current_request()
    if request:
        template_name = request.ab.run(template_name)
    return template_loader(template_name, template_dirs=template_dirs)
load_template_source.is_usable = True
