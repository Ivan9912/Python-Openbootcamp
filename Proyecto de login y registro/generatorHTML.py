class html:
    def helloWorld (self, nameUser, codName):
        web = r'.\welcome.html'
        URL = 'https://www.youtube.com/watch?v=5ZPnmEeXnRY&list=RD5ZPnmEeXnRY&start_radio=1'
        
        salva1 = '{'
        salva2 = '}'
       
        doc = '<!DOCTYPE html>\n'
        head = f'\n    <head>\n        <meta charset="UTF-8">\n        <meta http-equiv="X-UA-Compatible" content="IE=edge">\n        <meta name="viewport" content="width=device-width, initial-scale=1.0">\n        <title>Hola {nameUser}</title>\n        <style>body{salva1}background-color: beige;display: flex;justify-content:center;flex-direction: column;align-items: center;{salva2}</style>\n    </head>\n    '
        body = f'<body>\n        <h1>¿Vamos a codear {nameUser} #{codName}?</h1>\n        <button id="btn">¿Escuchamos música?</button>\n        <script>const buttonVideo = document.querySelector(\'#btn\');buttonVideo.addEventListener(\'click\', ()=>window.location=\"{URL}\");</script>\n    </body>\n'
        
        with open(web, 'w', encoding='utf-8') as w:
            w.write(f'{doc}<html lang="es-419">{head}{body}</html>')
            w.close()
           