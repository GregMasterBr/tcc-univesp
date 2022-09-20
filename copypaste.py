import pyperclip
message="""*Fri, 10 Jun 2022 00:02:16 +0000 | ['Sem categoria']*
                Olá, mundo!
                Boas-vindas ao WordPress. Esse é o seu primeiro post. Edite-o ou exclua-o, e então comece a escrever!

                <https://bairroalerta.gregmaster.com.br/2022/06/09/ola-mundo/>

                Por: *['Gregorio']*"""
pyperclip.copy(message)
#print(message)
print(pyperclip.paste())