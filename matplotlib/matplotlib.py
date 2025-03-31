# matplotlib_importacao_configuracao_inicial
import matplotlib.pyplot as plt

# Usando um estilo predefinido
plt.style.use('ggplot')

# Configuração global de parâmetros
plt.rcParams['figure.figsize'] = (10, 5)

# matplotlib_criando_figuras_e_eixos
# Cria uma nova figura
plt.figure()

# Cria múltiplos subplots
fig, axes = plt.subplots(2, 2)  # 2x2 de subplots

# Criação recomendada de figuras e eixos
fig, ax = plt.subplots()

# Adiciona um subplot a uma figura existente
fig.add_subplot(111)  # Um único eixo (1x1 de subplots)

# matplotlib_plots_simples
# Gráfico de linha
plt.plot([1, 2, 3], [4, 5, 6])

# Gráfico de dispersão
plt.scatter([1, 2, 3], [4, 5, 6])

# Gráfico de barras verticais
plt.bar(['A', 'B', 'C'], [3, 4, 5])

# Gráfico de barras horizontais
plt.barh(['A', 'B', 'C'], [3, 4, 5])

# Histograma
plt.hist([1, 2, 2, 3, 3, 3, 3, 4])

# Gráfico de pizza
plt.pie([10, 20, 30])

# Boxplot
plt.boxplot([1, 2, 3, 4, 5])

# Gráfico de violin
plt.violinplot([1, 2, 3])

# Gráfico de haste
plt.stem([1, 2, 3], [3, 2, 1])

# Gráfico de degraus
plt.step([1, 2, 3], [1, 4, 9])

# Área sombreada
plt.fill_between([1, 2, 3], [1, 4, 9])

# Hexbin plot
plt.hexbin([1, 2, 3], [1, 4, 9])

# Contorno
plt.contour([[1, 2], [3, 4]])

# Imagem de uma matriz 2D
plt.imshow([[1, 2], [3, 4]])

# Matriz como imagem
plt.matshow([[1, 2], [3, 4]])

# matplotlib_edicao_de_graficos
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Título do gráfico')
plt.legend(['Linha 1'])
plt.xlim(0, 4)
plt.ylim(3, 7)
plt.xticks([1, 2, 3], ['Um', 'Dois', 'Três'])
plt.grid(True)
plt.text(2, 5, 'Texto no gráfico', fontsize=12)
plt.annotate('Ponto especial', xy=(2, 5), xytext=(3, 6),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

# matplotlib_trabalhando_com_subplots
# Criação padrão de subplots
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])

# Definir rótulos no subplot
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_title('Título do gráfico')

# Subplot manual
fig.add_subplot(111)

# Ajuste automático do espaçamento entre subplots
plt.tight_layout()

# Ajuste manual do espaçamento
fig.subplots_adjust(hspace=0.5)

# matplotlib_cores_estilos_e_transparencia
# Definir colormap
plt.set_cmap('viridis')

# Adicionar barra de cores
plt.colorbar()

# Definir cor de fundo do gráfico
plt.gca().set_facecolor('lightgray')

# Definir transparência de um elemento
plt.plot([1, 2, 3], [4, 5, 6], alpha=0.5)

# matplotlib_salvar_e_mostrar_graficos
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()  # Exibe o gráfico

# Salva o gráfico como uma imagem PNG
plt.savefig('grafico.png')

# Salva o gráfico como PDF
plt.savefig('grafico.pdf')

# Salva o gráfico como SVG
plt.savefig('grafico.svg')

# Fecha a figura ativa
plt.close()

# matplotlib_graficos_tridimensionais
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot3D([1, 2, 3], [4, 5, 6], [7, 8, 9])  # Linha 3D

# Dispersão 3D
ax.scatter3D([1, 2, 3], [4, 5, 6], [7, 8, 9])

# Superfície 3D
ax.plot_surface([1, 2, 3], [4, 5, 6], [7, 8, 9])

# Wireframe 3D
ax.plot_wireframe([1, 2, 3], [4, 5, 6], [7, 8, 9])

# Contornos 3D
ax.contour3D([1, 2, 3], [4, 5, 6], [7, 8, 9])

# matplotlib_animacoes
from matplotlib.animation import FuncAnimation

# Função de animação
def animate(i):
    plt.clf()  # Limpa a figura
    plt.plot([1, 2, 3], [1 * i, 2 * i, 3 * i])

fig = plt.figure()
animation = FuncAnimation(fig, animate, frames=10, interval=1000)
animation.save('animacao.mp4')  # Salva animação como mp4

# matplotlib_extras_e_personalizacoes
# Adicionar barras de erro
plt.errorbar([1, 2, 3], [4, 5, 6], yerr=[0.1, 0.2, 0.3])

# Escala logarítmica no eixo X
plt.semilogx([1, 2, 3], [4, 5, 6])

# Escala logarítmica no eixo Y
plt.semilogy([1, 2, 3], [4, 5, 6])

# Escala log-log
plt.loglog([1, 2, 3], [4, 5, 6])

# Gráfico polar
plt.polar([0, 0.5, 1], [1, 2, 3])

# Eixo Y duplo
plt.twinx()

# Eixo X duplo
plt.twiny()

# Histograma 2D
plt.hist2d([1, 2, 3], [4, 5, 6])
