from setuptools import setup, find_packages


setup(
    name='sop-phone',
    version='0.5.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'phonenumbers'
    ],
    description="Manage phone informations of each sites.",
    author = "Soprema NOC team",
    author_email = "noc@soprema.com",
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
    zip_safe=False,
)
