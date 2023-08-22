from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def render_pass_json(path: Path, **kwargs) -> str:
    """Render pass.json files using Jinja2 syntax.
    To render variables pass it as kwargs.

    :param path: path to pass.json file
    :type path: Path
    :param kwargs: variables for jinja2 template
    :type kwargs: dict
    :return: rendered file from provided path
    :rtype: str
    """
    template_dir = path.parent
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(path.name)
    rendered_template = template.render(**kwargs)
    return rendered_template
