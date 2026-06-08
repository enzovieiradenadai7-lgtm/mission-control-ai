# MISSION CONTROL AI

missao = "Orion Test Alpha"
equipe = "Equipe Apollo"

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

areas_monitoradas = [
    "Temperatura Interna",
    "Comunicação com a Base",
    "Sistema de Energia",
    "Suporte de Oxigênio",
    "Estabilidade Operacional"
]

# FUNÇÕES DE ANÁLISE

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1
    elif valor <= 30:
        return "NORMAL", 0
    elif valor <= 35:
        return "ATENÇÃO", 1
    else:
        return "CRÍTICO", 2

def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2
    elif valor < 60:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2
    elif valor < 50:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2
    elif valor < 90:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2
    elif valor < 70:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def analisar_tendencia(primeiro, ultimo):
    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável."

def gerar_recomendacao(risco):
    if risco >= 8:
        return "Ativar modo de segurança imediatamente."
    elif risco >= 5:
        return "Monitorar sistemas críticos."
    else:
        return "Manter operação normal."

# PROCESSAMENTO

riscos_ciclos = []
pontuacao_areas = [0, 0, 0, 0, 0]

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)

for i, ciclo in enumerate(dados_missao, start=1):

    temp_status, temp_pts = analisar_temperatura(ciclo[0])
    com_status, com_pts = analisar_comunicacao(ciclo[1])
    bat_status, bat_pts = analisar_bateria(ciclo[2])
    oxi_status, oxi_pts = analisar_oxigenio(ciclo[3])
    est_status, est_pts = analisar_estabilidade(ciclo[4])

    risco_total = (
        temp_pts + com_pts + bat_pts + oxi_pts + est_pts
    )

    riscos_ciclos.append(risco_total)

    pontuacao_areas[0] += temp_pts
    pontuacao_areas[1] += com_pts
    pontuacao_areas[2] += bat_pts
    pontuacao_areas[3] += oxi_pts
    pontuacao_areas[4] += est_pts

    print(f"\nCICLO {i}")
    print("-" * 40)
    print(f"Temperatura: {ciclo[0]}°C - {temp_status}")
    print(f"Comunicação: {ciclo[1]}% - {com_status}")
    print(f"Bateria: {ciclo[2]}% - {bat_status}")
    print(f"Oxigênio: {ciclo[3]}% - {oxi_status}")
    print(f"Estabilidade: {ciclo[4]}% - {est_status}")
    print(f"Risco do ciclo: {risco_total}")
    print(f"Classificação: {classificar_ciclo(risco_total)}")
    print(f"Recomendação: {gerar_recomendacao(risco_total)}")

# RELATÓRIO FINAL

media_temp = sum(l[0] for l in dados_missao) / len(dados_missao)
media_com = sum(l[1] for l in dados_missao) / len(dados_missao)
media_bat = sum(l[2] for l in dados_missao) / len(dados_missao)
media_oxi = sum(l[3] for l in dados_missao) / len(dados_missao)
media_est = sum(l[4] for l in dados_missao) / len(dados_missao)

ciclo_critico = riscos_ciclos.index(max(riscos_ciclos)) + 1

area_mais_afetada = areas_monitoradas[
    pontuacao_areas.index(max(pontuacao_areas))
]

print("\n" + "=" * 60)
print("RELATÓRIO FINAL")
print("=" * 60)

print(f"Missão: {missao}")
print(f"Equipe: {equipe}")
print(f"Ciclos analisados: {len(dados_missao)}")

print(f"\nMédia Temperatura: {media_temp:.2f}°C")
print(f"Média Comunicação: {media_com:.2f}%")
print(f"Média Bateria: {media_bat:.2f}%")
print(f"Média Oxigênio: {media_oxi:.2f}%")
print(f"Média Estabilidade: {media_est:.2f}%")

print(f"\nCiclo mais crítico: {ciclo_critico}")
print(f"Maior risco: {max(riscos_ciclos)}")

print("\nTendência da missão:")
print(analisar_tendencia(
    riscos_ciclos[0],
    riscos_ciclos[-1]
))

print("\nPontuação por área:")
for area, pontos in zip(areas_monitoradas, pontuacao_areas):
    print(f"{area}: {pontos} pontos")

print(f"\nÁrea mais afetada: {area_mais_afetada}")

risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)
print(f"Risco médio da missão: {risco_medio:.2f}")

print("\nFim da análise.")
