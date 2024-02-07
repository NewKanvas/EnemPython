from utils.lines import *

# Biblioteca


def portugues():
    title = f"{g}Português{rt}"
    data = {
        f"{g}Gramática Básica{rt}": gramaticaBasica,
        f"{b}Interpretação de Texto{rt}": interpretacaoTexto,
        f"{y}Concordância e Regência Verbal{rt}": concordanciaRegenciaVerbal,
        f"{r}Redação{rt}": "redacao",
        f"{m}Literatura{rt}": "literatura",
    }
    return title, data


# Assuntos
def gramaticaBasica():
    title = f"{g}Gramática Básica{rt}"
    texto = [
        f"{g}C: Conjugação verbal (ajuste do verbo de acordo com o sujeito)\n{c}A: Acentuação (uso correto de acentos gráficos)\n{r}S: Substantivos (classes e flexões dos substantivos)\n{m}O: Ortografia (regras de escrita correta)\n{m}P: Pontuação (uso adequado dos sinais de pontuação){rt}\n",
        f"Macetes para Ortografia\nRegras Mnemônicas: Utilize frases ou palavras que ajudem a lembrar de regras ortográficas específicas, como 'Muito Antes Pouco Depois' para lembrar da ordem correta das letras 'M', 'A', 'P', e 'D' em algumas palavras.",
    ]

    q = "_"

    return title, texto


def interpretacaoTexto():
    title = f"{b}Interpretação de Texto{rt}"
    texto = [
        f"{b}Interpretação de Texto{rt} é a habilidade de entender e extrair significado de um texto. Algumas dicas para aprimorar essa habilidade incluem:\n\n{r}1. Leia atentamente{rt}: Leia o texto cuidadosamente para compreender os detalhes.\n{r}2. Identifique o propósito{rt}: Determine se o texto é informativo, persuasivo, narrativo, etc.\n{r}3. Analise o contexto{rt}: Considere o contexto do texto para interpretar corretamente.\n{r}4. Destaque informações chave{rt}: Identifique as informações mais importantes para a compreensão global do texto.\n{r}5. Faça perguntas{rt}: Formule perguntas sobre o texto para guiar sua compreensão.",
    ]

    q = "_"

    return title, texto


def concordanciaRegenciaVerbal():
    title = f"{g}Concordância e Regência Verbal{rt}"
    texto = [
        f"{g}Concordância Verbal:{rt}\n\n"
        f"Concordância verbal se refere à relação entre sujeito e verbo em uma frase. Alguns pontos importantes incluem:\n\n"
        f"• Quando o sujeito é coletivo, o verbo fica sempre no singular.\n"
        f"Exemplo: A multidão ultrapassou o limite.\n\n"
        f"• Se o coletivo estiver especificado, o verbo pode ser conjugado no singular ou no plural.\n"
        f"Exemplo: A multidão de fãs ultrapassou o limite.\n"
        f"A multidão de fãs ultrapassaram o limite.\n\n"
        f"{g}Regência Verbal:{rt}\n\n"
        f"Regência verbal diz respeito à relação entre o verbo e seus complementos. Aqui estão alguns pontos importantes sobre a transitividade verbal:\n\n"
        f"• Verbo Intransitivo: Não precisa de complemento para fazer sentido.\n"
        f"Exemplo: Vovó morreu em pé.\n"
        f"(Em pé só mostra o modo)\n\n"
        f"• Verbo Transitivo Direto (V.T.D): É aquele que o complemento não inicia com preposição.\n"
        f"Exemplo: João comeu brigadeiro.\n"
        f"(Comeu o quê? Brigadeiro [Objeto Direto])\n\n"
        f"• Verbo Transitivo Indireto (V.T.I): É aquele que o complemento inicia com preposição.\n"
        f"Exemplo: João gosta de brigadeiro.\n"
        f"(Gosta do quê? Gosta de brigadeiro [Objeto Indireto])\n\n"
        f"• Verbo Transitivo Direto e Indireto: Apresenta ambos os complementos verbais.\n"
        f"Exemplo: João convidou os alunos para um churrasco.\n"
        f"                       O.D     preposição     O.I\n\n"
        f"{g}Regência Nominal:{rt}\n\n"
        f"Regência nominal diz respeito aos termos que completam o sentido do substantivo, adjetivo ou advérbio. Um ponto importante é conhecer as preposições essenciais, que são: 'a, ante, até, após, com, contra, de, desde, em, entre, para, perante, por, sem, sob, sobre, trás'.\n\n"
    ]

    q = "_"

    return (title, texto, q)


# Quizzes


def quizPort():
    pass
