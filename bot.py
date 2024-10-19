import pyautogui as pag
from time import sleep
import keyboard as kb
from tkinter import messagebox

# getting button coordinate
messagebox.showinfo(title='Pegando coordenadas', message="Posicione o mouse em cima do botão de concluir aula e depois aperte 'p'")
position = None
while True:  
    if kb.is_pressed('p'):
        position = pag.position()
        if messagebox.askyesno(title="Continuar", message=f"Deseja continuar com essas posições? {position}"):
            print(position)
            break

# marking classes as completed
messagebox.showwarning(title='Aviso', message="Não mexa na tela em quanto o programa esta rodando, para parar e só encerrar o programa")
while True:
    pag.click(x=position[0], y=position[1])
    sleep(5)

