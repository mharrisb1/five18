from five18 import __version__, PyProjectToml


def test_version():
    assert __version__ == "0.1.0"


def test_find_pyproject_toml_file():
    PyProjectToml()


def test_get_data_from_pyproject_toml_file():
    pytoml = PyProjectToml()
    assert pytoml.tool_table.poetry.version == __version__
