#Projeto individual 1 
#Lorhan Costa

import pandas as pd


def get_input():
    """
    Solicita ao usuário as notas de um candidato para cada uma das etapas
    do processo seletivo e retorna essas notas em uma string no formato 
    'eX_tX_pX_sX', onde X é a nota para cada etapa.
    """
    nome = input("Digite o nome do candidato: ")
    entrevista = float(input("Nota da entrevista: "))
    teste_teorico = float(input("Nota do teste teórico: "))
    teste_pratico = float(input("Nota do teste prático: "))
    soft_skills = float(input("Nota das soft skills: "))
    return f"e{entrevista:.1f}_t{teste_teorico:.1f}_p{teste_pratico:.1f}_s{soft_skills:.1f}"


def busca(notas_minimas, resultados):
    """
    Recebe as notas mínimas para cada etapa do processo seletivo e a lista 
    de resultados, e retorna um DataFrame com os candidatos que atendem às 
    notas mínimas especificadas.
    """
    selecionados = []
    for nome, notas in resultados:
        notas_validas = [float(nota[1:]) >= notas_minimas[etapa]
                         for etapa, nota in enumerate(notas.split("_"))]
        if all(notas_validas):
            selecionados.append((nome, notas))
    return pd.DataFrame(selecionados, columns=["Candidato", "Resultado"])


def main():
    # Criar uma lista vazia para armazenar os resultados
    resultados = []
    while True:
        # Obter as notas do usuário e armazená-las na lista de resultados
        notas = get_input()
        resultados.append(("João", notas))
        # Perguntar ao usuário se deseja continuar
        resposta = input("Deseja continuar? (S/N) ")
        if resposta.upper() != "S":
            break
    # Especificar as notas mínimas para cada etapa do processo seletivo
    notas_minimas = {"entrevista": 7.0, "teste_teorico": 7.0,
                     "teste_pratico": 7.0, "soft_skills": 7.0}
    # Buscar os candidatos que atendem às notas mínimas especificadas
    selecionados = busca(notas_minimas, resultados)
    print(selecionados)


if __name__ == "__main__":
    main()
