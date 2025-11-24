import os
import sys
from PIL import Image
import customtkinter as ctk
def caminho_relatorio():
    print("==== DEBUG DO CAMINHO ====")

    if getattr(sys, 'frozen', False):
        # quando for EXE → usar a pasta do EXE
        base_path = os.path.dirname(sys.executable)
    else:
        # quando rodar no VS Code → pasta do arquivo .py 
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, "relatorio.txt")

CAMINHO_RELATORIO = caminho_relatorio()
def resource_path(relative_path):
   
    try:
        # Se estiver no .exe
        base_path = sys._MEIPASS
    except Exception:
        # Se estiver rodando normal no Python
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


emoji1 = resource_path("imgs/icone.ico")


janela = ctk.CTk()
janela.config(bg= "#F2F0EF")
cor_fundo = "#F2F0EF"
def pagina1():
      
      
      for widget in janela.winfo_children():
          widget.destroy()

      janela.geometry("900x500")   # tamanho da primeira página
      janela.config(bg= "#F2F0EF")
      janela.title("Posto Shelw")
     
      janela.resizable(False , False)

      try:
              janela.iconbitmap(emoji1)
      except:
              pass  


      # ABA DE DESIGN
      cor_fundo = "#F2F0EF"


      texto_titulo1 = ctk.CTkLabel(
          janela,
          text="Shelw",
          font= ("Segoe UI ", 150 ,"bold"),
          text_color= "#B11E1E",
          bg_color= cor_fundo

      )

      texto_titulo2 = ctk.CTkLabel(
          janela,
          text="Posto",
          font=("Corbel", 150,"bold"),
          text_color= "black",
          bg_color= cor_fundo

      )
      #Botao
      botao1 = ctk.CTkButton(
          janela,
          text = "Open",
          font=("Inter", 40 , "bold"),
          text_color= cor_fundo,
          bg_color= cor_fundo,
          fg_color= "black",
          hover_color="#333333",
          corner_radius= 50,
          width= 200,
          height= 100,
          
          command= pagina2
          )

      linha1 = ctk.CTkFrame(
        janela,
        fg_color= "red",
        height= 20,
        width= 1000,
        bg_color= cor_fundo,
        corner_radius= 0
        )
      linha2 = ctk.CTkFrame(
              janela,
              fg_color= "#562F24",
              height= 20,
              width= 1000,
              bg_color= cor_fundo,
              corner_radius= 0
              )







      #AREA TEXTO


      texto_titulo1.place(x = 40, y = 175)
      texto_titulo2.place(x = 50 , y = 20)
      botao1.place(x = 650 , y = 150)
      linha1.place(x = 0, y = 370)
      linha2.place(x = 0, y = 390)


  #=========================== PAGINA 2 ==================================#
      sem_cor = "transparent"





  









def pagina2():
    
    try:
        caminho_img = resource_path("imgs/posto.png")
        print(f"Tentando abrir: {caminho_img}")
        print(f"Arquivo existe? {os.path.exists(caminho_img)}")
        
        emoji = ctk.CTkImage(
            light_image=Image.open(caminho_img),
            size=(120,120)
        )
        print("Imagem carregada com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar imagem: {e}")
        emoji = None
        
        
        
    for widget in janela.winfo_children():
        widget.destroy()
    janela.resizable(False , False)
    janela.geometry("1250x600")
         # / Primeiro false é largura e o outro é altura



        # Blocos caixas de texto #
    entrada_nome = ctk.CTkEntry(
        janela,
        width=300,
        height=55,
        placeholder_text="Nome completo",
        placeholder_text_color=  "#8F9292",
        border_width= 2,
        font=("Cascadia Code", 18),
        fg_color= cor_fundo,
        bg_color= cor_fundo,
        text_color= "black",
        corner_radius= 21,
        border_color= "#BCC6C6"
    )
    entrada_placa = ctk.CTkEntry(
        janela,
        width=300,
        height=55,
        placeholder_text="ABC-1234",
        placeholder_text_color=  "#8F9292",
        border_width= 2,
        font=("Cascadia Code", 18),
        fg_color= cor_fundo,
        bg_color= cor_fundo,
        text_color= "black",
        corner_radius= 21,
        border_color= "#BCC6C6"
    )
    entrada_modelo = ctk.CTkEntry(
        janela,
        width=300,
        height=55,
        placeholder_text="Digite o modelo...",
        placeholder_text_color=  "#8F9292",
        border_width= 2,
        font=("Cascadia Code", 18),
        fg_color= cor_fundo,
        bg_color= cor_fundo,
        text_color= "black",
        corner_radius= 21,
        border_color= "#BCC6C6"
    )
    entrada_data = ctk.CTkEntry(
        janela,
        width=300,
        height=55,
        placeholder_text="dd/mm/yyyy",
        placeholder_text_color=  "#8F9292",
        border_width= 2,
        font=("Cascadia Code", 18),
        fg_color= cor_fundo,
        bg_color= cor_fundo,
        text_color= "black",
        corner_radius= 21,
        border_color= "#BCC6C6"
    )
    entrada_valor = ctk.CTkEntry(
        janela,
        width=300,
        height=55,
        placeholder_text="Digite o valor em R$",
        placeholder_text_color=  "#8F9292",
        border_width= 2,
        font=("Cascadia Code", 18),
        fg_color= cor_fundo,
        bg_color= cor_fundo,
        text_color= "black",
        corner_radius= 21,
        border_color= "#BCC6C6"
    )
        
    entrada_volume = ctk.CTkEntry(
        janela,
        width=300,
        height=55,
        placeholder_text="Volume em Litros..",
        placeholder_text_color=  "#8F9292",
        border_width= 2,
        font=("Cascadia Code", 18),
        fg_color= cor_fundo,
        bg_color= cor_fundo,
        text_color= "black",
        corner_radius= 21,
        border_color= "#BCC6C6"
    )
      #==============BCDT===================#
      #Bloco de texto #
      
    titulo1 = ctk.CTkLabel(
        janela,
          text= "- Registrar novo abastecimento",
          font=("Inter", 60, "bold"),
          text_color= "#303030",
          bg_color= cor_fundo
        )
    titulo2 = ctk.CTkLabel(
               janela,
               image= emoji,   
               bg_color= cor_fundo  ,
               text= ""        
            )
      
      
    nome = ctk.CTkLabel(
          janela,
          text= "PROPRIETÁRIO RESPONSAVEL",
          font=("Cascadia Code", 15),
          text_color= "#504F4F",
          bg_color= cor_fundo
          
          
      )
    placa = ctk.CTkLabel(
          janela,
          text= "PLACA DO CARRO",
          font=("Cascadia Code", 15),
          text_color= "#504F4F",
          bg_color= cor_fundo
          
          
      )
        
    modelo_carro = ctk.CTkLabel(
          janela,
          text= "MODELO",
          font=("Cascadia Code", 15),
          text_color= "#504F4F",
          bg_color= cor_fundo
          
          
      )
      
    data = ctk.CTkLabel(
          janela,
          text= "DATA",
          font=("Cascadia Code", 15),
          text_color= "#504F4F",
          bg_color= cor_fundo
          
          
      )
    valor =  ctk.CTkLabel(
          janela,
          text= "VALOR EM R$",
          font=("Cascadia Code", 15),
          text_color= "#504F4F",
          bg_color= cor_fundo
          
          
      )
    volume_litros =  ctk.CTkLabel(
          janela,
          text= "VOLUME EM LITROS",
          font=("Cascadia Code", 15),
          text_color= "#504F4F",
          bg_color= cor_fundo
          
          
      )
      
      #===========BDT=======================#
      # Bloco de botão
      
    def pasta():
                print("Salvando em:", CAMINHO_RELATORIO)
                nome_completo = str(entrada_nome.get())
                placa_car = (entrada_placa.get())
                model = (entrada_modelo.get())
                data_rel = (entrada_data.get())
                value = (entrada_valor.get())
                litros = (entrada_volume.get())
                
              
                caminho_relatorio = "relatorio.txt"

                with open(CAMINHO_RELATORIO, "a", encoding="utf-8") as arquivo:

                    arquivo.write(f"Nome: {nome_completo} | Placa: {placa_car } \n")
                    arquivo.write(f"Modelo: {model} | Data: {data_rel} \n")
                    arquivo.write(f"Valor: {value}R$   | Qnt : {litros}L\n\n")
                    

      
      
      
    botao1 = ctk.CTkButton(
          janela,
          width= 200,
          height= 100,
          corner_radius= 20,
          bg_color= cor_fundo,
          fg_color= "#69CA67",
          hover_color="#569958",
          text= "Enviar",
          text_color= "white",
          command= pasta,
          
          font=("Inter", 40 , "bold"),
        )
    botao2 = ctk.CTkButton(
          janela,
          width= 200,
          height= 100,
          corner_radius= 20,
          bg_color= cor_fundo,
          fg_color= "#DAC720",
          hover_color="#CDAD23",
          text= "Abrir Relatorio",
          text_color= "white",
          command= abrir,
          
          font=("Inter", 20 , "bold"),
        )
    botao3 = ctk.CTkButton(
          janela,
          width= 200,
          height= 100,
          corner_radius= 20,
          bg_color= cor_fundo,
          fg_color= "#AF2121",
          hover_color="#511313",
          text= "Voltar",
          text_color= "white",
          command= voltar,
          
          font=("Inter", 40 , "bold"),
        )
    
      
#=======================BDB========================#  
        #posicionamento#
    nome.place(x = 60, y = 130) 
    entrada_nome.place(x=50, y=160)
        #
    placa.place(x = 400, y =130)
    entrada_placa.place(x = 390, y = 160)
        #
    modelo_carro.place(x = 60, y = 230)
    entrada_modelo.place(x = 50, y = 260)
        #
    data.place(x= 400, y =230)
    entrada_data.place (x = 390, y = 260)
        #
    valor.place(x = 60, y =330)
    entrada_valor.place(x = 50, y = 360)
        #
    volume_litros.place(x = 400, y = 330)
    entrada_volume.place(x = 390 , y = 360)
        #
    titulo1.place(x = 150, y = 30)
    titulo2.place(x = 30, y = 15)
        #
    botao1.place(x = 750, y = 160)
    botao2.place(x = 750, y = 275)
    botao3.place(x = 750, y = 390)


   
def abrir():
  print("Abrindo:", CAMINHO_RELATORIO)
  os.startfile(CAMINHO_RELATORIO)
  import subprocess
  subprocess.Popen(['notepad.exe', CAMINHO_RELATORIO])

def voltar():
  pagina1()


pagina1()


#Abrir aplicativo
janela.mainloop()