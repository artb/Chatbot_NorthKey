import json
import subprocess as s

class Chatbot():
    def __init__(self, nome):
        try:
            memoria = open(nome+'.json','r')
        except FileNotFoundError:
            with open(nome+'.json','w') as memoria:
                memoria.write('[["Will","Alfredo"],{"oi": "Olá, qual o seu nome?","tchau":"tchau"}]')
            memoria = open(nome+'.json','r')
        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)
        memoria.close()
        self.historico = [None,]

    def escuta(self,frase=None):
        if frase == None:
            frase = input('>: ')
        frase = str(frase)
        if 'executa ' in frase:
            return frase
        frase = frase.lower()
        frase = frase.replace('eh','é')
        return frase

    def pensa(self,frase):
        if frase in self.frases:
            return self.frases[frase]
        if frase == 'aprende':
            return 'Digite a frase: '

        # Responde frases que dependem do historico
        ultimaFrase = self.historico[-1]
        if ultimaFrase == 'Olá, qual o seu nome?':
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase
        if ultimaFrase == 'Digite a frase: ':
            self.chave = frase
            return 'Digite a resposta: '
        if ultimaFrase == 'Digite a resposta: ':
            resp = frase
            self.frases[self.chave] = resp
            self.gravaMemoria()
            return 'Aprendido'
        try:
            resp = str(eval(frase))
            return resp
        except:
            pass
        return 'Não entendi o que vc perguntou.\nMe pergunte algo como: \nHorário de funcionamento;\nEstacionamento;\nEntrega de carimbo;\nTempo para entregar carimbo;\nCópia de chave;\nNota fiscal; \nServiços em domicilio; \nValor carimbo; \nPonto de referencia;\nCaso eu não saiba te ajudar, ligue: 3215-2045 ou 99262-1439'
            
    def pegaNome(self,nome):
        if 'o meu nome eh ' in nome:
            nome = nome[14:]

        nome = nome.title()
        return nome

    def respondeNome(self,nome):
        frase2 = '. No que posso lhe ajudar?'
        if nome in self.conhecidos:
            frase = 'Bem vindo, '
        else:
            frase = 'Muito prazer '
            self.conhecidos.append(nome)
            self.gravaMemoria()
        return frase+nome+frase2

    def gravaMemoria(self):
        memoria = open(self.nome+'.json','w')
        json.dump([self.conhecidos,self.frases],memoria)
        memoria.close()

    def fala(self,frase):
        if 'executa ' in frase:
            comando = frase.replace('executa ','')
            try:
                s.Popen(comando)
            except FileNotFoundError:
                s.Popen(['xdg-open',comando])
        else:
            print(frase)
        self.historico.append(frase)
