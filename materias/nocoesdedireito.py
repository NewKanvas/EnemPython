from utils.lines import *
import random


# Biblioteca


def nocoesdedireito():
    title = f"{g}Noções de Direito{rt}"
    data = {
        f"{y}Princípios da Administração Pública{rt}": limpe,
    }
    return title, data


# Assuntos
def limpe():
    title = f"{g}LIMPE{rt}"
    texto = [
        f"O LIMPE é um acrônimo que representa os cinco princípios fundamentais da Administração Pública no Brasil:\n"
        f"1. {c}Legalidade{rt}: Todas as ações do setor público devem estar de acordo com a legislação vigente, garantindo\n que o Estado opere dentro dos limites legais e em conformidade com as leis estabelecidas.\n"
        f"2. {m}Impessoalidade{rt}: Os serviços públicos devem ser prestados de forma imparcial, sem discriminação ou favorecimento\n a indivíduos ou grupos específicos. A atuação dos servidores públicos deve ser neutra e isenta de influências pessoais ou políticas.\n",
        f"3. {y}Moralidade{rt}: Os agentes públicos devem agir de acordo com os princípios éticos estabelecidos, evitando comportamentos que violem\n a moralidade administrativa e prejudiquem o interesse público. A conduta dos servidores deve ser pautada pela integridade e honestidade.\n"
        f"4. {b}Publicidade{rt}: A administração pública deve ser transparente e acessível à população, fornecendo informações claras e disponibilizando\n dados relevantes para a sociedade. A divulgação de informações é essencial para garantir a prestação de contas e a fiscalização do uso dos recursos públicos.\n"
        f"5. {r}Eficiência{rt}: A gestão pública deve buscar a eficiência na utilização dos recursos e na entrega de serviços de qualidade à população.\n Isso implica em realizar as atividades de forma otimizada, buscando alcançar os melhores resultados com os recursos disponíveis.\n"
        f"\nEsses princípios orientam a atuação dos órgãos públicos em todos os níveis de governo, garantindo uma administração responsável, transparente\n e voltada para o interesse coletivo.",
    ]

    q = quizlimpe

    return (title, texto, q)


def quizlimpe():
    perguntas = {
        f"O que é {c}L{m}I{y}M{b}P{r}E{rt}?": {
            "Legalidade, Impessoalidade, Moralidade, Publicidade, Eficiência": [
                "Legitimidade, Imparcialidade, Modernização, Prestação, Eficácia",
                "Legislação, Integridade, Modernização, Padronização, Eficiência",
                "Lealdade, Inovação, Metodologia, Padronização, Efetividade",
                "Limitação, Irregularidade, Manipulação, Propaganda, Esgotamento",
                "Liberdade, Incompetência, Manipulação, Propaganda, Estagnação",
                "Legalismo, Individualismo, Má-fé, Propaganda, Engano",
            ]
        },
        f"Qual o {g}significado do princípio{rt} da {m}Impessoalidade{rt}?": {
            "Princípio que exige que os serviços públicos sejam prestados de forma imparcial, sem discriminação ou favorecimento.": [
                "Princípio que prevê a realização de concursos públicos para o ingresso em cargos públicos.",
                "Princípio que determina que a administração pública deve ser transparente.",
                "Princípio que garante a priorização de determinados grupos na prestação de serviços públicos.",
                "Princípio que promove a corrupção na administração pública.",
                "Princípio que permite a utilização de critérios pessoais na tomada de decisões.",
            ]
        },
        f"O que é {g}exigido{rt} pelo princípio da {y}Moralidade{rt}?": {
            "Que os agentes públicos ajam de acordo com os princípios éticos estabelecidos, evitando comportamentos que violem a moralidade administrativa.": [
                "Que a administração pública opere de forma transparente, fornecendo informações claras e acessíveis.",
                "Que os atos administrativos sejam realizados de acordo com a lei.",
                "Que os funcionários públicos recebam bonificações por desempenho.",
                "Que a administração pública busque apenas benefícios para determinados grupos.",
                "Que a administração pública ignore completamente as leis estabelecidas.",
            ]
        },
        f"Qual o {g}objetivo do princípio{rt} da {b}Publicidade{rt}?": {
            "Garantir a transparência na administração pública, fornecendo informações claras e disponibilizando dados relevantes para a sociedade.": [
                "Assegurar que os serviços públicos sejam prestados de forma imparcial e neutra.",
                "Assegurar que todos os atos da administração pública estejam de acordo com a lei.",
                "Promover a eficiência na gestão dos recursos públicos.",
                "Proteger os dados pessoais dos funcionários públicos.",
                "Incentivar a corrupção na administração pública.",
            ]
        },
        f"O que {g}significa o princípio{rt} da {r}Eficiência?{rt}": {
            "Buscar a gestão otimizada dos recursos e a entrega de serviços de qualidade à população.": [
                "Assegurar que os serviços públicos sejam prestados de forma imparcial e neutra.",
                "Exigir que todos os atos da administração pública estejam de acordo com a lei.",
                "Promover a burocracia na administração pública.",
                "Incentivar o desperdício de recursos públicos.",
                "Priorizar o atendimento apenas dos interesses de grupos específicos.",
            ]
        },
    }

    perg = random.choice(list(perguntas.keys()))
    resp = list(perguntas[perg].keys())[0]
    falsas = perguntas[perg][resp]

    return (perg, resp, falsas)
