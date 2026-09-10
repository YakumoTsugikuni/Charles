# -*- coding: utf-8 -*-
from html import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, PageBreak, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "Q-Scout_Robobloq_25_Aulas_Atividades.pdf"
styles = getSampleStyleSheet()
title = ParagraphStyle("title", parent=styles["Title"], fontSize=24, leading=29, spaceAfter=10)
subtitle = ParagraphStyle("subtitle", parent=styles["Normal"], fontSize=12, leading=16,
                          textColor=colors.HexColor("#2E7D32"), alignment=TA_CENTER)
heading = ParagraphStyle("heading", parent=styles["Heading1"], fontSize=16, leading=20,
                         textColor=colors.HexColor("#1B5E20"), spaceBefore=6, spaceAfter=8)
subheading = ParagraphStyle("subheading", parent=styles["Heading2"], fontSize=11.5,
                            textColor=colors.HexColor("#2E7D32"), spaceBefore=9, spaceAfter=4)
body = ParagraphStyle("body", parent=styles["Normal"], fontSize=9.5, leading=13, spaceAfter=6)
answer = ParagraphStyle("answer", parent=body, backColor=colors.HexColor("#F1F8E9"),
                        borderPadding=6, leftIndent=5, rightIndent=5)
code = ParagraphStyle("code", parent=styles["Code"], fontSize=8.3, leading=11,
                      backColor=colors.HexColor("#F5F5F5"), borderColor=colors.HexColor("#CCCCCC"),
                      borderWidth=.5, borderPadding=7, leftIndent=3, rightIndent=3, spaceAfter=7)

# This is an original educational adaptation of the topics visible in the supplied table of contents.
activities = [
    ("Pensamento computacional", "Decomposição, abstração, reconhecimento de padrões e algoritmo", "Planejar uma tarefa do robô dividindo-a em passos pequenos e ordenados.", "Dado um percurso simples, listar início, movimentos, decisões e fim.", ["início", "defina uma sequência de passos", "execute cada passo na ordem", "pare"], "Um problema fica mais fácil quando é dividido em partes, padrões são identificados e os passos são organizados em algoritmo."),
    ("Introdução à programação", "Eventos, comandos, sequência e repetição", "Criar o primeiro programa de movimento no MyQode.", "Fazer o robô andar, esperar e parar usando blocos.", ["quando iniciar", "motores 70 e 70", "espere 1 segundo", "pare os motores"], "O programa precisa de um evento inicial; os blocos seguintes são executados na sequência em que estão encaixados."),
    ("Aplicativo Robobloq", "Conexão Bluetooth e modos de controle", "Conectar o robô ao aplicativo e experimentar seus modos de operação.", "Testar controle manual, luz, música e movimento.", ["ligue o Q-Scout", "abra o aplicativo", "selecione o robô", "teste mover, luz e som"], "A conexão permite enviar comandos ao robô; antes de programar, é necessário selecionar o dispositivo correto e verificar a comunicação."),
    ("Seguidores de linha", "Sensor infravermelho e correção de trajetória", "Fazer o robô acompanhar uma linha escura.", "Montar um percurso e corrigir a direção conforme a leitura dos sensores.", ["repita para sempre", "se sensor indica esquerda: corrija para esquerda", "senão se indica direita: corrija para direita", "senão: siga reto"], "A lógica compara a leitura dos sensores e ajusta diferencialmente os motores para manter o robô sobre a linha."),
    ("Detector de obstáculo", "Sensor ultrassônico e condição", "Detectar um objeto à frente e evitar colisão.", "Avançar enquanto houver espaço e girar ao encontrar obstáculo.", ["repita para sempre", "se distância > limite: avance", "senão: pare e gire"], "A distância precisa ser comparada com um limite calibrado no ambiente real; o valor exato depende da configuração do robô."),
    ("Desafio: seguidor de linha com detector de obstáculos", "Prioridade entre dois sensores", "Combinar seguimento de linha e desvio de obstáculos.", "Seguir a linha, mas interromper o movimento quando surgir um obstáculo.", ["repita para sempre", "se obstáculo próximo: pare e desvie", "senão: execute a correção da linha"], "A segurança deve ter prioridade: primeiro se verifica o obstáculo e só depois se aplica a lógica de seguir a linha."),
    ("Sinalização de trânsito", "LEDs, cores e estados", "Representar um semáforo com luzes do robô.", "Alternar vermelho, verde e amarelo em ciclos temporizados.", ["repita para sempre", "luz vermelha; espere 3 segundos", "luz verde; espere 3 segundos", "luz amarela; espere 1 segundo"], "Cada cor representa um estado; as esperas controlam a duração e tornam a sequência compreensível."),
    ("Labirintos", "Planejamento espacial e calibração", "Planejar uma rota até a saída de um labirinto.", "Converter corredores e curvas em movimentos programados.", ["avance pelo corredor", "pare", "gire aproximadamente 90 graus", "repita para cada corredor", "pare na saída"], "A rota deve ser testada e calibrada; tempo de movimento e de giro acumulam erro, portanto é importante fazer ensaios."),
    ("Automação de veículos", "Sensores, decisão e estacionamento", "Automatizar uma manobra de estacionamento.", "Detectar espaço, alinhar o robô e parar dentro da vaga.", ["avance devagar", "se espaço detectado: alinhe", "gire para a vaga", "pare quando estiver alinhado"], "Automação combina sensores, regras de decisão e controle dos motores, com tolerâncias definidas para o espaço disponível."),
    ("Desafio: seguidor de linha com semáforo", "Integração de linha e sinalização", "Seguir a linha respeitando as cores do semáforo.", "Parar no vermelho, avançar no verde e aguardar no amarelo.", ["se vermelho: pare", "senão se amarelo: avance devagar", "senão se verde: siga a linha"], "A leitura da cor modifica o comportamento do seguidor de linha; o estado do semáforo deve ser avaliado continuamente."),
    ("Música", "Buzzer, notas e duração", "Criar uma sequência musical no robô.", "Tocar uma melodia curta com notas e pausas.", ["toque nota 60 por 0.5 batida", "toque nota 64 por 0.5 batida", "espere 0.25 segundo", "toque nota 67 por 1 batida"], "A melodia depende da ordem das notas e da duração; pausas ajudam a separar frases musicais."),
    ("Controle remoto", "Comandos sem fio e resposta do robô", "Controlar o Q-Scout remotamente.", "Mapear comandos de direção, velocidade, luz e parada.", ["se comando = frente: avance", "se comando = esquerda: gire", "se comando = direita: gire", "se comando = parar: pare"], "O controle remoto transforma cada entrada em uma ação; o comando de parada deve sempre estar disponível."),
    ("Sistema de segurança", "Alarme, botão e sensor de presença", "Criar um sistema que avise quando detectar acesso.", "Acionar luz e som quando um sensor ou botão for ativado.", ["repita para sempre", "se entrada de segurança ativa: luz vermelha", "toque alerta", "senão: luz desligada"], "Um sistema de segurança precisa monitorar continuamente, sinalizar o evento e voltar ao estado normal quando a condição desaparecer."),
    ("Giroscópio", "Orientação, inclinação e estabilização", "Usar a orientação do robô para tomar decisões.", "Detectar inclinação ou mudança de direção e corrigir o movimento.", ["repita para sempre", "leia orientação", "se inclinação acima do limite: pare", "senão: continue"], "O giroscópio fornece orientação relativa; seus limites precisam ser calibrados e o sensor não substitui um odômetro."),
    ("Desafio: sistema de segurança automotivo", "Integração de presença, giroscópio e alerta", "Construir uma proteção para um veículo robótico.", "Parar e alertar quando houver impacto, inclinação ou aproximação perigosa.", ["repita para sempre", "se obstáculo próximo ou inclinação: pare", "acenda alerta", "toque alarme"], "A solução integra múltiplas condições e adota comportamento seguro quando qualquer uma delas é acionada."),
    ("Corridas", "Velocidade, trajetória e tempo", "Otimizar um percurso sem perder o controle.", "Percorrer uma pista e medir o tempo de cada tentativa.", ["inicie cronômetro", "avance em velocidade segura", "reduza nas curvas", "pare na chegada"], "O melhor resultado não depende apenas da maior velocidade; trajetória, estabilidade e repetibilidade também são importantes."),
    ("Competição: carros", "Corrida com obstáculos", "Disputar uma pista mantendo o carro em movimento.", "Vencer uma corrida desviando de obstáculos.", ["repita até a chegada", "se obstáculo: desvie", "senão: avance", "pare na linha final"], "A estratégia combina rapidez e segurança; uma penalidade por colisão pode tornar a competição mais justa."),
    ("Sumô", "Detecção de borda, adversário e estratégia", "Manter o robô na arena e empurrar o oponente.", "Detectar bordas e aproximar-se do adversário sem sair do ringue.", ["repita para sempre", "se borda detectada: recue e gire", "senão se adversário detectado: avance", "senão: procure"], "A borda tem prioridade sobre o ataque, porque sair da arena encerra a disputa."),
    ("Futebol", "Controle, direção e interação com objeto", "Conduzir uma bola até o gol.", "Localizar, empurrar e direcionar a bola em equipe ou individualmente.", ["procure a bola", "alinhe-se", "avance até tocar", "empurre em direção ao gol"], "O robô precisa alternar busca, alinhamento e condução; velocidade baixa facilita o controle perto da bola."),
    ("Carrões autônomos", "Navegação autônoma e tomada de decisão", "Criar um veículo que complete uma pista sem controle manual.", "Usar sensores para escolher o próximo movimento.", ["repita até chegar", "leia linha e obstáculos", "escolha a ação mais segura", "execute por curto intervalo"], "Autonomia é um ciclo de perceber, decidir e agir; intervalos curtos permitem corrigir o caminho frequentemente."),
    ("Rampas", "Tração, velocidade e inclinação", "Subir e descer uma rampa sem perder estabilidade.", "Ajustar velocidade e direção para atravessar desníveis.", ["reduza antes da rampa", "avance com torque constante", "mantenha direção", "reduza na descida"], "A velocidade deve ser adaptada à inclinação; aceleração excessiva pode causar perda de tração ou saída da pista."),
    ("Indústria 4.0", "Automação, sensores e fluxo de produção", "Simular uma linha automatizada de produção.", "Seguir uma rota, detectar pontos e transportar uma carga.", ["siga a linha", "se estação detectada: pare", "execute a tarefa", "retome a linha"], "A atividade representa um fluxo industrial: sensores identificam etapas e o robô executa ações com pouca intervenção humana."),
    ("Robótica em operações de resgate", "Navegação, segurança e missão", "Planejar o uso do robô em uma área de resgate.", "Percorrer a área, evitar riscos e sinalizar um ponto encontrado.", ["avance com baixa velocidade", "se risco: pare e desvie", "se vítima ou alvo: sinalize", "retorne ou aguarde"], "Em resgate, preservar o robô e comunicar o achado é mais importante que velocidade máxima."),
    ("Checkpoint", "Cores, estados e passagem por pontos", "Completar uma rota passando por checkpoints coloridos.", "Reconhecer cada cor e executar a ação correspondente.", ["siga a linha", "se cor = vermelho: pare", "se cor = azul: toque sinal", "se cor = verde: continue"], "Os checkpoints funcionam como estados de uma missão; a sequência pode ser validada com variáveis ou contadores."),
    ("Triatlo", "Integração de movimento, sensores e controle", "Combinar três modalidades em uma única missão.", "Completar trechos de corrida, linha e obstáculos com regras diferentes.", ["complete trecho 1", "mude para modo seguidor de linha", "complete trecho 2", "mude para desvio", "complete trecho 3", "pare"], "O desafio final exige modularidade: cada trecho tem uma estratégia, mas todos compartilham início, transições e parada segura."),
]


def page_number(canvas, document):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#888888"))
    canvas.drawCentredString(A4[0] / 2, 1.2 * cm, str(document.page))
    canvas.restoreState()


def build_pdf():
    story = [Spacer(1, 3 * cm), Paragraph("Q-Scout (Robobloq)", title),
             Paragraph("Guia didático das 25 aulas e atividades", subtitle), Spacer(1, cm),
             HRFlowable(width="60%", color=colors.HexColor("#4CAF50"), thickness=1.2, hAlign="CENTER"),
             Spacer(1, cm), Paragraph("Adaptação autoral baseada nos temas visíveis no sumário fornecido. Os valores de sensores, portas e tempos devem ser calibrados no robô e no MyQode usados em aula.", body), PageBreak(), Paragraph("Sumário", heading)]
    story.extend(Paragraph(f"Aula {i:02d} — {item[0]}", body) for i, item in enumerate(activities, 1))
    story.append(PageBreak())
    for i, (name, concept, objective, challenge, blocks, solution) in enumerate(activities, 1):
        story += [Paragraph(f"Aula {i:02d} — {name}", heading), Paragraph(objective, body),
                  Paragraph(f"Conceito / componente: {concept}", subheading),
                  Paragraph(f"Atividade proposta: {challenge}", body), Paragraph("Sequência sugerida de blocos", subheading),
                  Paragraph("<br/>".join(escape(block) for block in blocks), code),
                  Paragraph("Orientação / resposta", subheading), Paragraph(solution, answer), PageBreak()]
    SimpleDocTemplate(OUTPUT, pagesize=A4, topMargin=2 * cm, bottomMargin=2 * cm,
                      leftMargin=2 * cm, rightMargin=2 * cm,
                      title="Q-Scout Robobloq - 25 Aulas e Atividades").build(
                          story, onFirstPage=page_number, onLaterPages=page_number)
    print(f"PDF gerado com sucesso: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
