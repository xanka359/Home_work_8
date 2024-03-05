from pathlib import Path
import tests
from tests import resources


def resource_path(file_name):
    return str(Path(tests.__file__).parent.joinpath(f'resources/{file_name}').absolute())

