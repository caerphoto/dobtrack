try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='dobtrack',
    version='0.3.0',
    description='''Simple DOB department item tracker.''',
    author='Andy Farrell',
    author_email='andy.farrell@uk.fujitsu.com',
    url='http://www.caerphoto.com',
    install_requires=[
        "Pylons>=1.0",
        "SQLAlchemy>=0.5",
        "Mako",
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'dobtrack': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'dobtrack': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = dobtrack.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
