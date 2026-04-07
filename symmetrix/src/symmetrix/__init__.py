__version__ = "0.0.1"

# TODO: very hacky, to import underscored names
import importlib  # noqa: E402

_sym = importlib.import_module(".symmetrix", __name__)
_sym.__all__ = [n for n in vars(_sym) if not (n.startswith("__") and n.endswith("__"))]
from .symmetrix import *  # noqa: F403
from .calculator import Symmetrix  # noqa: F401
