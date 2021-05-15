from setuptools import setup, find_packages

setup(
    name="svm40_exporter",
    version="0.1.0",
    description="Prometheus Exporter for Sensirion SVM40 Evaluation Kit",
    author="Fabian Mettler",
    author_email="fabian@mettler.cc",
    url="https://github.com/maveonair/svm40-exporter",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["sensirion-shdlc-svm40>=0.3.0", "prometheus_client>=0.10.1"],
    scripts=["scripts/svm40-exporter"],
)
