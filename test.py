import os
from lxml import html, etree
import sys
from PySide2 import QtCore, QtGui, QtQml
import re

# import pypandoc

__author__ = "Sylvia Onwukwe"
__version__ = "1.0"
__all__ = []

# Base Language is XHTML
#This Script converts between the CML and two selected markup languages

base_file = 'index.html'

# def base_md():
#     """Converts CML to Markdown for browser rendering
#     :param none
#     :returns: converted html file
#     :rtype: unicode
#     :raises ModuleNotFoundError: if the needed dependency is not installed
#     """
#     try:
#         new_file = pypandoc.convert_file(base_file, 'markdown')
#     except ModuleNotFoundError:
#         print("Please Install Pypandoc")
#     print(new_file)
#     f= open("new_file.md","w+")
#     f.write(new_file)
#     return new_file

# def md_base():
#     base_md()
#     md_file = 'new_file.md'
#     try:
#         new_file = pypandoc.convert_file(md_file, 'html')
#     except ModuleNotFoundError:
#         print("Please Install Pypandoc")
#     print(new_file)


def base_html():
    """Converts CML to HTML for older-browser rendering
    :param none
    :returns: converted html file
    :rtype: unicode
    :raises ModuleNotFoundError: if the needed dependency is not installed
    """
    try:
        new_file = html.fromstring(open(base_file).read())
    except FileNotFoundError:
        print("Base File doesn't exist")
    output = open('./Tests/test_file.html', 'wb')
    output.write(b"<!DOCTYPE html>\n")
    output.write(etree.tostring(new_file))
    return new_file

def html_base():
    """Converts HTML back to xHTML
    :param none
    :returns: converted xhtml file
    :rtype: unicode
    :raises ModuleNotFoundError: if the needed dependency is not installed
    """
    base_html()
    html_file = './Tests/test_file.html'
    try:
        new_file = html.fromstring(open(html_file).read())
    except FileNotFoundError:
        print("Base File doesn't exist")
    output = open('./Tests/test_file.xhtml', 'rb+')
    output.write(b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n')
    output.write(etree.tostring(new_file))
    return output

# base_html()
# html_base()

# base_md()
# md_base()
# write index.qml file

def base_qml():
    with open(base_file, 'r') as file:
        data = file.read().replace('"', "'")
        new_file = open('./Tests/index.qml', 'w')
        new_file.write("import QtQuick 2.12\nimport QtQuick.Controls 2.12\nimport QtWebEngine 1.0")
        new_file.write("\nApplicationWindow {\nid: window\nvisible: true\nwidth:640\nheight:480\nWebEngineView {\nid: webEngineView\nanchors.fill: parent\n}")
        new_file.write("Component.onCompleted: {\nvar html="+'"' +data +'"'+"\nwebEngineView.loadHtml(html)\n}\n}")
    if __name__ == '__main__':

        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        app = QtGui.QGuiApplication(sys.argv)

        engine = QtQml.QQmlApplicationEngine()

        url = QtCore.QUrl.fromLocalFile('Tests/index.qml')
        engine.load(url)
        if not engine.rootObjects():
            
            sys.exit(-1)

        sys.exit(app.exec_())
      

def qml_base():
     with open('./Test/base_qml.qml', 'r') as file:
        data = file.read()
        f = re.findall("<html>(.*?)</html>", data, re.DOTALL)
        new_file = open('./Test/qml_html.xhtml', 'w')
        new_file.write("<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.01 Transitional//EN'>\n")
        new_file.write(str(f[0]))
    # line = open(, 'rb')
    # f = re.findall('<html>(.*?)</html>', line)
        print(type(str(f)))
    #take qml file and find the html content
    
qml_base()
"""

try lxml to onvert html to xml for first test
md tshoul dbe the last testqml to html to spin off server and copy the html code
html to qml should generate strings for qml file and use web engine to view

save a screenshot of the view from qml in the read me file
push to git and use the picture for presentation
Kindly complete adapter and test.py tommor
confirm if QC creator is running to view the padding
Else complete the readme.md

Wednesday: docker build and git
Confirm qml Qt creator
"""