from setuptools import setup
setup(
        name='rasaslottypes',
        version='0.1',
        description='Extending classes for slot types',
        url='#',
        author='sysang',
        author_email='daosysang@gmail.com',
        license='MIT',
        packages=['RasaSlotTypes'],
        zip_safe=False,
        package_data={
            "RasaSlotTypes": ["models/*.bin", "models/*.npy"],
        }
    )
