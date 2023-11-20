from utils.cores import *

# Biblioteca


def portugues():
    title = f"{g}Português{rt}"
    lista = {
        f"{g}Gramática Básica{rt}": gramaticaBasica,
        f"{b}Interpretação de Texto{rt}": interpretacaoTexto,
        f"{r}Redação{rt}": "redacao",
        f"{m}Literatura{rt}": "literatura",
    }
    return title, lista


# Assuntos
def gramaticaBasica():
    title = f"{g}Gramática Básica{rt}"
    texto = [
        f"{g}C: Conjugação verbal (ajuste do verbo de acordo com o sujeito)\n{c}A: Acentuação (uso correto de acentos gráficos)\n{r}S: Substantivos (classes e flexões dos substantivos)\n{m}O: Ortografia (regras de escrita correta)\n{m}P: Pontuação (uso adequado dos sinais de pontuação){rt}\n",
        f"Macetes para Ortografia\nRegras Mnemônicas: Utilize frases ou palavras que ajudem a lembrar de regras ortográficas específicas, como 'Muito Antes Pouco Depois' para lembrar da ordem correta das letras 'M', 'A', 'P', e 'D' em algumas palavras.",
    ]

    return title, texto


def interpretacaoTexto():
    title = f"{b}Interpretação de Texto{rt}"
    texto = [
        f"{b}Interpretação de Texto{rt} é a habilidade de entender e extrair significado de um texto. Algumas dicas para aprimorar essa habilidade incluem:\n\n{r}1. Leia atentamente{rt}: Leia o texto cuidadosamente para compreender os detalhes.\n{r}2. Identifique o propósito{rt}: Determine se o texto é informativo, persuasivo, narrativo, etc.\n{r}3. Analise o contexto{rt}: Considere o contexto do texto para interpretar corretamente.\n{r}4. Destaque informações chave{rt}: Identifique as informações mais importantes para a compreensão global do texto.\n{r}5. Faça perguntas{rt}: Formule perguntas sobre o texto para guiar sua compreensão.",
    ]

    return title, texto
