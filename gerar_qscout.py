# -*- coding: utf-8 -*-
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, PageBreak, Paragraph, SimpleDocTemplate, Spacer


OUTPUT = "Q-Scout_Robobloq_Desafios_Resolvidos.pdf"
styles = getSampleStyleSheet()
title = ParagraphStyle("title", parent=styles["Title"], fontSize=24, leading=29, spaceAfter=10)
subtitle = ParagraphStyle("subtitle", parent=styles["Normal"], fontSize=12, leading=16,
                          textColor=colors.HexColor("#2E7D32"), alignment=TA_CENTER)
heading = ParagraphStyle("heading", parent=styles["Heading1"], fontSize=17, leading=21,
                         textColor=colors.HexColor("#1B5E20"), spaceBefore=6, spaceAfter=9)
subheading = ParagraphStyle("subheading", parent=styles["Heading2"], fontSize=12,
                            textColor=colors.HexColor("#2E7D32"), spaceBefore=10, spaceAfter=5)
body = ParagraphStyle("body", parent=styles["Normal"], fontSize=10, leading=14, spaceAfter=7)
answer = ParagraphStyle("answer", parent=body, backColor=colors.HexColor("#F1F8E9"),
                        borderPadding=6, leftIndent=5, rightIndent=5)
code = ParagraphStyle("code", parent=styles["Code"], fontSize=8.5, leading=12,
                      backColor=colors.HexColor("#F5F5F5"), borderColor=colors.HexColor("#CCCCCC"),
                      borderWidth=.5, borderPadding=7, leftIndent=3, rightIndent=3, spaceAfter=8)


chapters = [
    ("Conhecendo o Q-Scout", "Placa-mãe e módulo de início",
     "Apresenta a placa-mãe, a conexão Bluetooth com o MyQode e a lógica básica de montagem de programas.",
     "Vamos dançar: alternar movimentos, pausas e sons em uma pequena coreografia.",
     ["quando a bandeira verde for clicada", "repita 4 vezes", "  motor esquerdo 80, motor direito -80", "  espere 0.5 segundos", "  toque nota 60 por 0.3 batida", "  motor esquerdo -80, motor direito 80", "  espere 0.5 segundos", "  toque nota 64 por 0.3 batida", "pare os motores"],
     "O bloco de início define o evento que dispara a execução; sem ele, blocos soltos não são executados."),
    ("Pequeno Corredor (Little Racer)", "Motores M1/M2 e velocidade das rodas",
     "Ensina deslocamento em linha reta e curvas controlando independentemente as rodas esquerda e direita.",
     "Percorrer uma pista amarela no menor tempo, combinando trechos retos e curvas cronometradas.",
     ["quando a bandeira verde for clicada", "motor esquerdo 100, motor direito 100", "espere 1.2 segundos", "motor esquerdo 60, motor direito -60", "espere 0.4 segundos", "motor esquerdo 100, motor direito 100", "espere 1.0 segundo", "pare os motores"],
     "Um carro do futuro pode combinar direção autônoma, sensores, motor elétrico e comunicação entre veículos."),
    ("Pequeno Músico (Little Musician)", "Buzzer e LEDs RGB",
     "Explora notas musicais, duração do som e combinação de cores dos LEDs de bordo.",
     "Tocar a melodia de Brilha, Brilha, Estrelinha com blocos de som.",
     ["quando a bandeira verde for clicada", "toque 60 por 0.5 batida (dó)", "toque 60 por 0.5 batida (dó)", "toque 67 por 0.5 batida (sol)", "toque 67 por 0.5 batida (sol)", "toque 69 por 0.5 batida (lá)", "toque 69 por 0.5 batida (lá)", "toque 67 por 1.0 batida (sol)"],
     "O desafio é montar corretamente a sequência de blocos de som antes dos colegas."),
    ("Saindo do Labirinto", "Distância estimada por tempo e velocidade",
     "Ensina a estimar distâncias e ângulos por meio de calibração, já que o robô não possui odômetro.",
     "Seguir um mapa de referência até sair do labirinto usando segmentos retos e curvas.",
     ["quando a bandeira verde for clicada", "motores 80 e 80; espere 1.5 segundos", "motores 70 e -70; espere 0.6 segundo", "motores 80 e 80; espere 1.0 segundo", "motores -70 e 70; espere 0.6 segundo", "motores 80 e 80; espere 1.2 segundos", "pare os motores"],
     "Sim. Calibre tempo por distância e tempo por ângulo, depois traduza cada trecho do novo mapa em blocos."),
    ("Pequeno Entregador (Little Courier)", "Botão personalizado e estruturas de controle",
     "Apresenta condicionais e laços de repetição usando o botão da placa como entrada.",
     "Avançar continuamente e parar, com um sinal sonoro, quando o botão for pressionado.",
     ["quando a bandeira verde for clicada", "repita para sempre", "  motores 90 e 90", "  se botão do topo pressionado", "    pare os motores", "    toque nota 72 por 0.5 batida", "    pare este programa"],
     "Um laço infinito mantém o programa monitorando entradas. O bloco se trata apenas o caso verdadeiro; se... senão trata os dois casos."),
    ("Guarda de Patrulha (Patrol Guard)", "Sensor de linha infravermelho",
     "Usa os quatro estados do sensor de linha para manter o robô sobre uma faixa preta.",
     "Seguir automaticamente uma linha, corrigindo a direção a cada desvio.",
     ["quando a bandeira verde for clicada", "repita para sempre", "  se sensor = 3: motores 70 e 70", "  senão se sensor = 1: motores -40 e 70", "  senão se sensor = 2: motores 70 e -40", "  senão: pare os motores"],
     "A correção contínua baseada nos estados 0, 1, 2 e 3 permite que o robô se autocorrija durante o percurso."),
    ("Guerreiro Ultrassônico (Ultrasonic Warrior)", "Sensor ultrassônico",
     "Mede a distância até obstáculos e implementa desvio automático.",
     "Avançar e girar quando a distância medida ficar abaixo do limite de segurança.",
     ["quando a bandeira verde for clicada", "repita para sempre", "  se distância > 300: motores 80 e 80", "  senão: motores 60 e -60", "  espere 0.3 segundo"],
     "O sensor também pode medir distâncias, disparar alarmes, controlar a velocidade e detectar presença."),
    ("Grande Porteiro (Great Doorman)", "Alarme de proximidade",
     "Reutiliza o ultrassônico para acionar luz e som quando alguém se aproxima.",
     "Acender o LED vermelho e emitir um alerta quando a distância for menor que aproximadamente um metro.",
     ["quando a bandeira verde for clicada", "repita para sempre", "  se distância < 1000: luz vermelha e toque nota 80", "  senão: desligue a luz"],
     "É possível contar aproximações, usar níveis de alerta ou enviar o evento a outro dispositivo via Bluetooth."),
    ("Caça ao Tesouro (Treasure Hunt)", "Combinação de linha e ultrassônico",
     "Combina os dois sensores: o ultrassônico desvia de obstáculos e o sensor de linha encontra o tesouro.",
     "Explorar o ambiente, desviar e parar ao detectar uma marca escura no chão.",
     ["quando a bandeira verde for clicada", "repita para sempre", "  se sensor de linha = 3: pare, toque nota 84 e termine", "  senão se distância < 300: motores 60 e -60", "  senão: motores 80 e 80"],
     "A prioridade deve ser: encontrar o tesouro, desviar de obstáculos e, por último, continuar explorando."),
]


def page_number(canvas, document):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#888888"))
    canvas.drawCentredString(A4[0] / 2, 1.2 * cm, str(document.page))
    canvas.restoreState()


def build_pdf():
    story = [Spacer(1, 4 * cm), Paragraph("Robô Q-Scout (Robobloq)", title),
             Paragraph("Guia de Desafios e Questões Resolvidos — MyQode / Scratch 3.0", subtitle),
             Spacer(1, cm), HRFlowable(width="60%", color=colors.HexColor("#4CAF50"), thickness=1.2, hAlign="CENTER"),
             Spacer(1, cm), Paragraph("Material de apoio com nove capítulos sobre programação, motores, som, sensores e estruturas de controle do Q-Scout.", body), PageBreak(), Paragraph("Sumário", heading)]
    story.extend(Paragraph(f"Capítulo {index} — {chapter[0]}", body) for index, chapter in enumerate(chapters, 1))
    story.append(PageBreak())
    for index, (name, component, intro, challenge, lines, solution) in enumerate(chapters, 1):
        story += [Paragraph(f"Capítulo {index} — {name}", heading), Paragraph(intro, body),
                   Paragraph(f"Componente / conceito: {component}", subheading),
                   Paragraph(f"Desafio prático: {challenge}", body), Paragraph("Código (blocos MyQode / Scratch):", subheading),
                   Paragraph("<br/>".join(line.replace("&", "&amp;") for line in lines), code),
                   Paragraph("Resposta comentada", subheading), Paragraph(solution, answer), PageBreak()]
    SimpleDocTemplate(OUTPUT, pagesize=A4, topMargin=2 * cm, bottomMargin=2 * cm,
                      leftMargin=2 * cm, rightMargin=2 * cm,
                      title="Q-Scout Robobloq - Desafios e Questões Resolvidos").build(
                          story, onFirstPage=page_number, onLaterPages=page_number)
    print(f"PDF gerado com sucesso: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()