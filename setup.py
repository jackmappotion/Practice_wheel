from setuptools import setup, find_packages

setup(
    name="jackmappotion-test",  # 패키지 명
    version="1.0.0.3",
    description="Test Package",
    author="jackmappotion",
    author_email="jackmappotion@naver.com",
    url="https://jackmappotion.com/",
    license="MIT",  # MIT에서 정한 표준 라이센스 따른다
    python_requires=">=3",
    install_requires=["numpy"],  # 패키지 사용을 위해 필요한 추가 설치 패키지
    py_modules=["packageTest"],  # 패키지에 포함되는 모듈
    packages=["packageTest"],  # 패키지가 들어있는 폴더들
)
