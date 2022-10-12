# -*- coding: utf-8 -*-
# @time    : 18-8-10 下午8:28
# @author  : xugaoxiang
# @email   : xugx.ai@gmail.com
# @website : https://xugaoxiang.com
# @file    : setup.py.py
# @software: PyCharm

# Always prefer setuptools over distutils，导入模块
# from setuptools import setup, find_packages
# from os import path
from distutils.core import setup


setup(name="moudelTest",version="1.0",description="文件统计模块",author="qiumonster",
      py_modules=['moudelTest'])


# 分别读取README.md和requirements.txt的内容
# here = path.abspath(path.dirname(__file__))



# Get the long description from the README file
# with open('README.md', encoding='utf-8') as fp:
#     long_description = fp.read()

# with open('requirements.txt', encoding='utf-8') as fp:
#     install_requires = fp.read()
#
# setup(
#     # 名称
#     name='FacialAttendanceRecord',
#
#     # 版本号
#     version='1.0.1',
#
#     # 基本描述
#     description='Facial Attendance Record',
#
#     # 项目的详细介绍，我这填充的是README.md的内容
#     long_description=long_description,
#
#     # README的格式，支持markdown，应该算是标准了
#     long_description_content_type='text/markdown',
#
#     # 项目的地址
#     url='https://xugaoxiang.com',
#
#     # 项目的作者
#     author='xugaoxiang',
#
#     # 作者的邮箱地址
#     author_email='xugx.ai@gmail.com',
#
#     # Classifiers，
#     classifiers=[  # Optional
#         # How mature is this project? Common values are
#         #   3 - Alpha
#         #   4 - Beta
#         #   5 - Production/Stable
#         'Development Status :: 3 - Beta',
#
#         # Indicate who your project is intended for
#         'Intended Audience :: Developers',
#         'Topic :: Software Development :: Build Tools',
#
#         # Pick your license as you wish
#         'License :: OSI Approved :: GNU GPL v3 License',
#
#         # Specify the Python versions you support here. In particular, ensure
#         # that you indicate whether you support Python 2, Python 3 or both.
#         'Programming Language :: Python :: 3',
#         'Programming Language :: Python :: 3.4',
#         'Programming Language :: Python :: 3.5',
#         'Programming Language :: Python :: 3.6',
#     ],
#
#     # 项目的关键字
#     keywords='facial attendance record',
#
#     # 打包时需要加入的模块，调用find_packages方法实现，简单方便
#     packages=find_packages(exclude=['contrib', 'docs', 'tests', 'build', 'dist'])，
#
#     # 项目的依赖库，读取的requirements.txt内容
#     install_requires=install_requires,
#
#     # 数据文件都写在了MANIFEST.in文件中
#     include_package_data=True,
#
#     # entry_points 指明了工程的入口，在本项目中就是facialattendancerecord模块下的main.py中的main方法
#     # 我这是命令行工具，安装成功后就是执行的这个命令
#
#     entry_points={
#         'console_scripts': [
#             'FacialAttendanceRecord=facialattendancerecord.main:main',
#         ],
#     },
#
# )
