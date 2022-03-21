import logging

from app.carinsurance_model.config.core import PACKAGE_ROOT, config

# It is strongly advised to not add any handlers other than
# NullHandler to library’s loggers. This is because the configuration
# of handlers is the prerogative of the application developer who uses the
# library. The application developer knows their target audience and what
# handlers are most appropriate for their application:
logging.getLogger(config.app_config.package_name).addHandler(logging.NullHandler())


with open(PACKAGE_ROOT / "VERSION") as version_file:
    __version__ = version_file.read().strip()
