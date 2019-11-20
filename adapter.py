import sys
from lxml import html, etree
from PySide2 import QtCore, QtGui, QtQml
import re

# Base Language is XHTML
#This Script converts between the CML and two selected markup languages
__author__ = "Sylvia Onwukwe"
__version__ = "1.0"
__all__ = [ 'base_html', 'html_base', 'base_qml', 'qml_base']

def base_html(base_file="./index.xhtml", output="./Test/cml_html.html"):
    """Converts CML to HTML for older-browser rendering
    :param str base_file: Unicode string or bytes(path to the source xhtml file)
    :param str output: output will be written to this specified path in html format
    :returns: converted html file
    :rtype: unicode
    :raises FileNotFoundError: if the base file is not found
    :raises ModuleNotFoundError: if the required dependency is not found
    """
    try:
        new_file = html.fromstring(open(base_file).read())
        content = open(output, 'wb')
        content.write(b"<!DOCTYPE html>\n")
        content.write(etree.tostring(new_file))
        with open(output, 'r') as file:
            new_content = file.read().replace('<html xmlns="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml">', '<html>')
            content.write(bytearray(new_content, 'utf-8'))

    except FileNotFoundError:
        print("Base File or output file does not exist")
    except ModuleNotFoundError:
        print("LXML not installed")
    return output
  

def html_base(base_file="index.xhtml", html_file="./Test/cml_html.html", output="./Test/html_cml.xhtml"):
    """Converts HTML back to xHTML
    :param str base_file: Unicode string or bytes(path to the source xhtml file)
    :param str html_file: Unicode string or bytes(path to the generated html file)
    :param str output: output will be written to this specified path in xhtml format
    :returns: converted xhtml file
    :rtype: unicode
    :raises FileNotFoundError: if the base file is not found
    :raises ModuleNotFoundError: if the required dependency is not found
    """
    base_html(base_file, output)
    try:
        new_file = html.fromstring(open(html_file).read())
        content = open(output, 'rb+')
        content.write(b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n')
        content.write(etree.tostring(new_file))
    except FileNotFoundError:
        print("HTML File or Output File doesn't exist")

def base_qml(base_file="./index.xhtml", output="Test/base_qml.qml"):
    """Generate a Qml file to display base_file
    :param str base_file: Unicode string or bytes(path to the source xhtml file)
    :param str output: output will be written to this specified path in qml format
    :returns: converted xhtml file
    :rtype: unicode
    :raises FileNotFoundError: if the base file is not found
    """

    try:
        with open(base_file, 'r') as file:
            data = file.read().replace('"', "'")
            new_file = open(output, 'w+')
            new_file.write("import QtQuick 2.12\nimport QtQuick.Controls 2.12\nimport QtWebEngine 1.0")
            new_file.write("\nApplicationWindow {\nid: window\nvisible: true\nwidth:640\nheight:480\nWebEngineView {\nid: webEngineView\nanchors.fill: parent\n}")
            new_file.write("\nComponent.onCompleted: {\nvar html="+'"' +data +'"'+"\nwebEngineView.loadHtml(html)\n}\n}")
            new_file.read()
    
        if __name__ == '__main__':

            QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
            app = QtGui.QGuiApplication(sys.argv)

            engine = QtQml.QQmlApplicationEngine()
            url = QtCore.QUrl.fromLocalFile(output)
            engine.load(url)
            if not engine.rootObjects():
                sys.exit(-1)

            sys.exit(app.exec_())
    except FileNotFoundError:
        print("File not Found")
    

def qml_base(base_file="./Test/base_qml.qml", output="Test/qml_base.xhtml"):
    """Generate a xHTML file from the generated QML file
    :param str base_file: Unicode string or bytes(path to the generated qml file)
    :param str output: output will be written to this specified path in xhtml format
    :returns: converted xhtml file
    :rtype: unicode
    :raises FileNotFoundError: if the base file is not found
    """
    try:
        open(base_file, 'r')
    except FileNotFoundError:
        print("Usage: run 'python adapter.py base_qml' and then try again")
    try:
        with open(base_file, 'r') as file:
            data = file.read()
            f = re.findall("<html xmlns='http://www.w3.org/1999/xhtml'>(.*?)</html>", data, re.DOTALL)
            print(f)
            new_file = open(output, 'w')
            new_file.write("<!DOCTYPE html PUBLIC '-//W3C//DTD HTML 4.01 Transitional//EN'>\n")
            
            new_file.write(str(f[0]))
    except FileNotFoundError:
        print("File not Found")

if __name__ == "__main__":
    if sys.argv[1] == "base_html":
        base_html()
    elif sys.argv[1] == "html_base":
        html_base()
    elif sys.argv[1] == "base_qml":
        base_qml()
    elif sys.argv[1] == "qml_base":
        qml_base()
    else:
        raise SystemExit("usage:  python hello.py <name>")