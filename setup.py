from setuptools import setup, find_packages

setup(name='idc-django-imageprocessor',
        version='0.3',
        description='''Batch image processing for
        Django with presets and cache support''',
        author='Marcin Nowak',
        author_email='marcin.j.nowak@gmail.com',
        url='https://github.com/i-dotcom/django-imageprocessor',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        ],
        )
