from setuptools import setup

setup(
    name="FlixWatcher",
    version="1.0.0",
    maintainer="Furkan K. Yıldırım",
    maintainer_email="furkankyildirim@gmail.com",
    packages=['FlixWatcher'],
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"]
)