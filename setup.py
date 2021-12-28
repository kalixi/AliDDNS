from setuptools import setup

install_requires = [
    'requests',
    'netifaces',
]
extras_require = {
    # 'extras': [
    #     'netifaces',
    # ]
}

setup(
    name='aliddns2',
    version='0.1.0',
    license='GPL',
    description='Aliyun DDNS client',
    author='rfancn',
    requires=install_requires,
    extras_require=extras_require,
    packages=['aliddns2'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
