from setuptools import setup, find_packages

setup(
    name='django-reporting',
    version='0.2.0',
    description='An interactive table-based reporting application for Django.',
    long_description=open('README.rst').read(),
    author='Garcia Marc',
    author_email='garcia.marc@gmail.com',
    url='http://github.com/jtrain/django-reporting',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    package_data = {
        'attachments': [
            'templates/reporting/*.html',
        ]
    },
    zip_safe=False,
)
