from pathlib import Path
from unittest.mock import Mock, mock_open, patch

from src.apple_pass_creator.jinja import render_pass_json


@patch("jinja2.Environment.get_template")
def test_render_template(mock_get_template):
    valid_string = "String to render"
    mock_render = mock_get_template.return_value.render
    mock_render.return_value = valid_string
    valid_filename = "test.json"

    rendered_string = render_pass_json(
        Path("/test/templates/" + valid_filename),
        missing_word="render",
    )

    assert rendered_string == valid_string
    mock_get_template.assert_called_once_with(valid_filename)
    mock_render.assert_called_once_with(missing_word="render")
