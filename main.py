import os
import sys
from PIL import Image
import customtkinter as ctk
cor_fundo_original = "#F2F0EF"
cor_borda_original = "#BCC6C6"
cor_text_original  = "#8F9292"
label_color_original = "#504F4F"
def caminho_relatorio():


    if getattr(sys, 'frozen', False):
        # exe
        base_path = os.path.dirname(sys.executable)
    else:
        # vs code
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
caixatext = resource_path("imgs/image.png")


janela = ctk.CTk()
cor_fundo = "#121418"
def pagina1():
    
      
      for widget in janela.winfo_children():
          widget.destroy()

      janela.geometry("900x500")   # tamanho da primeira página
      janela.config(bg= "#121418")
      janela.title("Posto Shelw")
     
      janela.resizable(False , False)

      try:
              janela.iconbitmap(emoji1)
      except:
              pass  


      # ABA DE DESIGN
     
      png1 = resource_path("imgs/posto.png")
       
        
      png2 = ctk.CTkImage(
            light_image=Image.open(png1),
            size=(150,150)
      )
      png3 = ctk.CTkLabel(
          janela,
          image = png2 ,
          bg_color= cor_fundo,
          text= None
      )
      texto_titulo1 = ctk.CTkLabel(
          janela,
          text="Shelw",
          font= ("Segoe UI ", 150 ,"bold"),
          text_color= "#B11E1E",
          bg_color= cor_fundo

      )

      texto_titulo2 = ctk.CTkLabel(
          janela,
          text="POSTO",
          font=("Corbel", 150,"bold"),
          text_color= "white",
          bg_color= cor_fundo

      )
      #Botao
      botao1 = ctk.CTkButton(
          janela,
          text = "OPEN",
          font=("Inter", 40 , "bold"),
          text_color= "#F2F0EF",
          bg_color= cor_fundo,
          fg_color= "black",
          hover_color="#333333",
          corner_radius= 30,
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
      png3.place(x = 480, y = 195)


  #=========================== PAGINA 2 ==================================#
      sem_cor = "transparent"
def bloquear_virgula(tecla):
                if "," in tecla:
                    return False
                if tecla.isalpha():
                    return False
                return True

validacao = (janela.register(bloquear_virgula), "%S")  




  

cor_fundo = "#121418"
cor_borda = "#2F3030"
cor_text  = "#AEB1B5"
label_color = "#AEB1B5"

    # Aplicar na janela
    



def pagina2():
    
    try:
        caminho_img = resource_path("imgs/posto.png")
       
        
        emoji = ctk.CTkImage(
            light_image=Image.open(caminho_img),
            size=(120,120)
        )
   
    except Exception as e:
    
        emoji = None
        
        
    for widget in janela.winfo_children():
        widget.destroy()
    janela.resizable(False , False)
    janela.geometry("1250x600")
    janela.configure(fg_color=cor_fundo)
         # / Primeiro false é largura e o outro é altura


    fontes = ("Montserrat", 18)
    fontes1 = ("Montserrat", 15, "bold")
        # Blocos caixas de texto #

    entrada_nome = ctk.CTkEntry(
        janela,
        width=300,
        height=55,
        placeholder_text="Nome completo",
        placeholder_text_color=  cor_text,
        border_width= 2,
        font= fontes,
        fg_color= cor_fundo,
        bg_color= cor_fundo,
        text_color= "white",
        corner_radius= 21,
        border_color= cor_borda
    )
    entrada_placa = ctk.CTkEntry(
        janela,
        width=300,
        height=55,
        placeholder_text="ABC-1234",
        placeholder_text_color=  cor_text,
        border_width= 2,
        font= fontes,
        fg_color= cor_fundo,
        bg_color= cor_fundo,
        text_color= "white",
        corner_radius= 21,
        border_color= cor_borda
    )
    entrada_modelo = ctk.CTkEntry(
        janela,
        width=300,
        height=55,
        placeholder_text="Digite o modelo...",
        placeholder_text_color=  cor_text,
        border_width= 2,
        font= fontes,
        fg_color= cor_fundo,
        bg_color= cor_fundo,
        text_color= "white",
        corner_radius= 21,
        border_color= cor_borda
    )
    entrada_data = ctk.CTkEntry(
        janela,
        width=300,
        height=55,
        placeholder_text="dd/mm/yyyy",
        placeholder_text_color= cor_text,
        border_width= 2,
        font= fontes,
        fg_color= cor_fundo,
        bg_color= cor_fundo,
        text_color= "white",
        corner_radius= 21,
        border_color= cor_borda
    )
   
    precos = {
    "Gasolina Comum": None,
    "Gasolina Aditivada": None,  
    "Etanol": None,
    "Diesel": None,
    "GNV": None
}
    selecionado = ctk.StringVar(value="Gasolina Comum")
            
    
    entrada_valor = ctk.CTkOptionMenu(
    janela,
    values= list(precos.keys()),
    fg_color= "#676767",
    bg_color= cor_fundo,
    button_color="#666666",
    button_hover_color= "#595959",
    text_color= "#FFFFFF",
    font = fontes1,
    width=300,
    height=55,
    corner_radius=10,
    dropdown_font= fontes1,
    variable= selecionado

    )
    
    entrada_volume = ctk.CTkEntry(
        janela,
        width=300,
        height=55,
        placeholder_text="Volume em Litros...",
        placeholder_text_color=  cor_text,
        border_width= 2,
        font= fontes,
        fg_color= cor_fundo,
        bg_color= cor_fundo,
        text_color= "white",
        corner_radius= 21,
        border_color= cor_borda,
        validate = "key",
        validatecommand = validacao
    )
    gas_comum_entrada= ctk.CTkEntry(
        janela,
        width=250,
        height=50,
        placeholder_text="R$",
        placeholder_text_color=  cor_text,
        border_width= 2,
        font= fontes,
        fg_color= cor_fundo,
        bg_color= cor_fundo,
        text_color= "white",
        corner_radius= 21,
        border_color= cor_borda,
        validate = "key",
        validatecommand = validacao
    )
      #==============BCDT===================#
      #Bloco de texto #
    titulo1 = ctk.CTkLabel(
        janela,
          text= " Registrar novo abastecimento",
          font=("Inter", 60, "bold"),
          text_color= cor_text,
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
          font= fontes1,
          text_color= label_color,
          bg_color= cor_fundo
          
          
      )
    placa = ctk.CTkLabel(
          janela,
          text= "PLACA DO CARRO",
          font= fontes1,
          text_color= label_color,
          bg_color= cor_fundo
          
          
      )
        
    modelo_carro = ctk.CTkLabel(
          janela,
          text= "MODELO",
          font= fontes1,
          text_color=label_color,
          bg_color= cor_fundo
          
          
      )
      
    data = ctk.CTkLabel(
          janela,
          text= "DATA",
          font= fontes1,
          text_color= label_color,
          bg_color= cor_fundo
          
          
      )
    combs =  ctk.CTkLabel(
          janela,
          text= "TIPO DE COMBUSTIVEL",
          font= fontes1,
          text_color=label_color,
          bg_color= cor_fundo
          
          
      )
    volume_litros =  ctk.CTkLabel(
          janela,
          text= "VOLUME EM LITROS",
          font= fontes1,
          text_color= label_color,
          bg_color= cor_fundo
          
          
      )
     
    gas_comum =  ctk.CTkLabel(
          janela,
          text= "PREÇO DA GASOLINA:",
          font= fontes1,
          text_color= label_color,
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
                    litros = float(entrada_volume.get())
                    gas = float(gas_comum_entrada.get())
                    total1 = litros * gas
            
                    caminho_relatorio = "relatorio.txt"

                    with open(CAMINHO_RELATORIO, "a", encoding="utf-8") as arquivo:

                        arquivo.write(f"Nome: {nome_completo} | Placa: {placa_car } \n")
                        arquivo.write(f"Modelo: {model} | Data: {data_rel} \n")
                        arquivo.write(f"Tipo: {value} | Qnt : {litros} Litros \n")
                        arquivo.write(f"Valor Total: {total1:.2f} R$\n\n")
                        

        
    def remove_focus(event):
        janela.focus()  

    entrada_nome.bind("<Escape>", remove_focus)
    entrada_data.bind("<Escape>", remove_focus)
    entrada_modelo.bind("<Escape>", remove_focus)
    entrada_placa.bind("<Escape>", remove_focus)
    entrada_valor.bind("<Escape>", remove_focus)
    entrada_volume.bind("<Escape>", remove_focus)
    gas_comum_entrada.bind("<Escape>", remove_focus)

    font_text =  ("Inter", 25 ) 


   


    botao1 = ctk.CTkButton(
          janela,
          width= 250,
          height= 70,
          corner_radius= 20,
          bg_color= cor_fundo,
          fg_color= "#69CA67",
          hover_color="#569958",
          text= " ✓ Enviar",
          text_color= "white",
          command= pasta,
          
          font= font_text,
    )
    botao2 = ctk.CTkButton(
          janela,
          width= 250,
          height= 70,
          corner_radius= 20,
          bg_color= cor_fundo,
          fg_color= "#DAC720",
          hover_color="#CDAD23",
          text= " 🗎 Abrir Relatório",
          text_color= "white",
          command= abrir,
          
          font= font_text,
        )
    botao3 = ctk.CTkButton(
          janela,
          width= 250,
          height= 70,
          corner_radius= 20,
          bg_color= cor_fundo,
          fg_color= "#AF2121",
          hover_color="#511313",
          text= " ↺ Voltar",
          text_color= "white",
          command= voltar,
          
          font= font_text,
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
    combs.place(x = 60, y =330)
    entrada_valor.place(x = 50, y = 360)
        #
    volume_litros.place(x = 400, y = 330)
    entrada_volume.place(x = 390 , y = 360)
        #
    titulo1.place(x = 150, y = 30)
    titulo2.place(x = 30, y = 15)
        #
    botao1.place(x = 50,  y = 430)
    botao2.place(x = 310, y = 430)
    botao3.place(x = 570, y = 430)
    
    
    #
    gas_comum.place(x = 740, y = 130)
    gas_comum_entrada.place(x = 730, y = 160)
 
    
   

    
      
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