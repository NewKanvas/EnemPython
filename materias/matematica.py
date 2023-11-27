from utils.lines import *
import random
from menus.quiz import *

# Biblioteca


def matematica():
    title = f"{b}Matemática{rt}"
    lista = {
        f"{g}Cálculo Básico{rt}": calculoBasico,
        f"{b}Porcentagem{rt}": porcentagem,
        f"{r}Média{rt}": "media",
        f"{m}Logaritmo{rt}": "logaritmo",
    }
    return title, lista


# Assuntos


def porcentagem():
    title = f"{b}Porcentagem{rt}"
    texto = [
        f"{b}Porcentagem{rt} é uma forma de expressar uma parte de um todo em termos percentuais.\n\n{r}Macete{rt}: Para calcular a porcentagem de um valor, {r}multiplique o valor pela porcentagem{rt} e {g}mova a vírgula duas posições para a frente{rt}.\nPor exemplo, {r}20 alunos{rt},{g}35% são mulheres{rt}. 20 x 35 = 700.\nPortanto, 35% de 20 alunos são 7 alunas.",
        f"Para encontrar a {r}parte complementar{rt} (porcentagem restante),\nsubtraia a porcentagem conhecida de 100%. Por exemplo, se 35% são mulheres,\n\n100% - 35% = 65% são homens.\n20 x 65 = 1300\n\nAssim, em 20 alunos, 65% são homens, o que equivale a 13 alunos.",
        f"{r}Para encontrar o valor original{rt} de um numero com aumento em porcentagem.\n\n{r}[Valor com aumento]{g}/{r}(100+x%){rt}\n\nExemplo:\nSe um trabalhador tivesse {g}7% de aumento{rt} do seu {r}salario atual{rt} receberia {b}R$ 2.675,00{rt}.\n\n2675/(100+7)\n2675/107 = 2500\nValor do salario atual = 2500",
    ]

    x = random.randint(0, 101)
    y = random.randint(0, 101)

    r_correta = (x * y) / 100

    quiz = {
        f"{r}{x}%{rt} de {g}{y}{rt} é?": f"{x} X {y} = {x*y}\n{x*y}/{100} = {(r_correta):.2f}",
        f"{g}{x}{rt} é quanto de {r}{y}%{rt}?": f"{x} X {y} = {x*y}\n{x*y}/{100} = {(r_correta):.2f}",
    }

    return (title, texto, quiz, x, y, r_correta)


####
def calculoBasico():
    title = f"{g}Cálculo Básico{rt}"
    texto = [
        f"{g}P: P{rt}arênteses (resolva as operações dentro dos {g}parênteses{rt} primeiro)\n{c}E: E{rt}xpoente (realize as operações com {c}expoentes{rt})\n{r}M: M{rt}ultiplicação (efetue as {r}multiplicações{rt})\n{r}D: D{rt}ivisão (faça as {r}divisões{rt})\n{m}A: A{rt}dição (realize as {m}adições{rt})\n{m}S: S{rt}ubtração (efetue as {m}subtrações){rt}\n",
        f"Macetes para Frações Decimais\nConverter para Fração: Coloque o número decimal sobre uma potência de 10 apropriada\n(por exemplo, 0,25 = 25/100 = 1/4)",
    ]
    x = random.randint(0, 101)
    y = random.randint(0, 101)

    r_corretaA = x + y
    r_corretaM = x - y
    r_corretaX = x * y
    r_corretaD = x / y

    quiz = {
        f"{r}{x}{rt} + {g}{y}{rt} é?": f"{x} + {y} = {r_corretaA}\n",
        f"{r}{x}{rt} - {g}{y}{rt} é?": f"{x} - {y} = {r_corretaM}\n",
        f"{r}{x}{rt} x {g}{y}{rt} é?": f"{x} x {y} = {r_corretaX}\n",
        f"{r}{x}{rt} / {g}{y}{rt} é?": f"{x} / {y} = {r_corretaX}\n",
    }

    return title, texto, quiz, x, y, r_correta
