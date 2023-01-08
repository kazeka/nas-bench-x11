from setuptools import setup, find_packages

setup(
    name = 'nas_bench_x11',
    version = '1.0',
    author = 'Shen Yan, Colin White',
    author_email = 'yanshen6@msu.edu, crwhite@cs.cmu.edu',
    description = 'benchmark for multi-fidelity NAS algorithms',
    license = 'Apache 2.0',
    keywords = ['AutoML', 'NAS', 'Deep Learning'],
    url = "https://github.com/automl/nas-bench-x11",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    install_requires = [
        'autograd>=1.3',
        'click',
        'Cython',
        'ConfigSpace',
        'ipython',
        'lightgbm>=2.3.1',
        'matplotlib',
        'numpy',
        'pandas',
        'pathvalidate',
        'psutil',
        'Pillow',
        'scikit-image',
        'seaborn',
        'statsmodels',
        'tqdm',
        'xgboost',
    ]
)
