import setuptools

requirements = ['selenium~=4.6', 'requests~=2.28', 'selenium-interceptor>=1.0.2', 'selenium_profiles==2.2.5.1', 'selenium_stealth==1.0.6', 'undetected-chromedriver==3.2.1']

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='selenium_peacemaker',
    author='Hack Napier',
    author_email='hacknapier@aol.com',
    description='Stealth emulate and automate Chrome using profiles, proxy and selenium.',
    keywords='Selenium, emulation, automation, undetected-chromedriver, webautomation, selenium-stealth, selenium-android, anti-bot-detection',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hacknapier/selenium_peacemaker',
    project_urls={
        'Documentation': 'https://github.com/hacknapier/selenium_peacemaker',
        'Bug Reports':
            'https://github.com/hacknapier/selenium_peacemaker/issues',
        'Source Code': 'https://github.com/hacknapier/selenium_peacemaker',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: Free for non-commercial use',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Framework :: Jupyter',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: Browsers',

    ],
    python_requires='>=3.7',
    install_requires=requirements,
    include_package_data=True,
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
)
