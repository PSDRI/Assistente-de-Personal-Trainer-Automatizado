def gerar_treino(biotipo, dias, tipo_exercicio):
    # Dicionário para armazenar planos de treino com base nos parâmetros fornecidos
    planos_de_treino = {
        "ectomorfo": {
            1: "Full Body focado em força e hipertrofia, com exercícios compostos.",
            3: "Treino ABC para ganho de massa: Dia 1 - Peito e Ombros; Dia 2 - Costas e Bíceps; Dia 3 - Pernas.",
            5: "Treino ABCDE com ênfase em hipertrofia: cada dia foca em um grupo muscular específico."
        },
        "mesomorfo": {
            1: "Full Body equilibrado com séries mistas de força e resistência.",
            3: "Treino ABC: Dia 1 - Peito e Ombros; Dia 2 - Costas e Bíceps; Dia 3 - Pernas e Abdômen.",
            5: "Treino ABCDE para definição: foco diário em um grupo muscular específico."
        },
        "endomorfo": {
            1: "Full Body com ênfase em queima calórica e exercícios de alta intensidade.",
            3: "Treino ABC com HIIT entre séries: Dia 1 - Peito e Ombros; Dia 2 - Costas e Bíceps; Dia 3 - Pernas e Abdômen.",
            5: "Treino ABCDE para queima de gordura com alta intensidade e foco em resistência."
        }
    }
    
    # Sugestões de exercícios com base no tipo preferido
    exercicios_por_tipo = {
        "funcional": "Exercícios funcionais com ênfase em movimentos naturais e flexibilidade.",
        "maquinário": "Exercícios em máquinas para isolamento muscular e controle.",
        "peso livre": "Exercícios com pesos livres, como supino, agachamento e desenvolvimento com halteres.",
        "cardio": "Treinos de resistência cardiovascular, como corrida e ciclismo.",
        "hiit": "Treinos intervalados de alta intensidade para otimizar a queima calórica."
    }
    
    # Verificar se os dados são válidos
    if biotipo.lower() not in planos_de_treino:
        return "Biotipo corporal inválido. Escolha entre 'ectomorfo', 'mesomorfo' ou 'endomorfo'."
    if dias not in planos_de_treino[biotipo.lower()]:
        return "Número de dias inválido. Escolha entre 1, 3 ou 5 dias por semana."
    if tipo_exercicio.lower() not in exercicios_por_tipo:
        return "Tipo de exercício inválido. Escolha entre 'funcional', 'maquinário', 'peso livre', 'cardio' ou 'hiit'."
    
    # Gerar plano de treino
    plano = planos_de_treino[biotipo.lower()][dias]
    exercicio = exercicios_por_tipo[tipo_exercicio.lower()]
    
    return f"Plano de Treino:\n- Biotipo: {biotipo.capitalize()}\n- Dias de Treino: {dias} dias por semana\n- Tipo de Exercício: {exercicio}\n\nTreino Sugerido: {plano}"

# Solicitando informações do usuário
print("Bem-vindo ao Assistente de Personal Trainer!")
biotipo = input("Qual é o seu biotipo corporal (ectomorfo, mesomorfo, endomorfo)? ")
dias = int(input("Quantos dias por semana você pode treinar (1, 3, 5)? "))
tipo_exercicio = input("Qual o tipo de exercício preferido (funcional, maquinário, peso livre, cardio, hiit)? ")

# Gerar e exibir o plano de treino
plano_gerado = gerar_treino(biotipo, dias, tipo_exercicio)
print("\n" + plano_gerado)
