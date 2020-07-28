"""
Módulos Externos

Utilizamos o gerenciado de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em:
https://pypi.org

pip install ftpcli

from ftpcli import FTP

ftp = FTP(server, account, password)

ftp.pwd()
# /

ftp.ls()
# ['index.html', 'css', '.htaccess', 'test']

ftp.cd('css')
ftp.ls()
# ['style.css', 'reset.css', 'main.css']

ftp.pwd()
# /css/

ftp.mkdir('aaaa')
ftp.ls()
# ['style.css', 'reset.css', 'main.css', 'aaaa']

ftp.rm('aaaa')
ftp.ls()
# ['style.css', 'reset.css', 'main.css']

ftp.cd('../')
ftp.download('css')
# download: [Success] /css/style.css
# download: [Success] /css/reset.css
# download: [Success] /css/main.css
"""

import pydf
pdf = pydf.generate_pdf('<h1>Geek University</h1><br/><br/<strong>Progrma&ccedil;&atilde;o em Python: Essencial</strong>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
