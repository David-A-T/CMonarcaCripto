# Importar: Librerías
import customtkinter

# Inicializar: Interfaz
app = customtkinter.CTk()
app.title("Encriptación de Base de Datos")
app.geometry("720x780")

# Pestañas
tab = customtkinter.CTkTabview(app, width=620, height=680)
tab.grid(row=0,column=0,sticky="w",padx=50,pady=20)

tab1 = tab.add("Registro General")
tab2 = tab.add("Registro Legal")
tab3 = tab.add("Registro Psicosocial")
tab4 = tab.add("Registro Humanitario")

# Pestaña: Registro General
def getGText(): # Obtener Registros
    entries = [surPGEntry, surMGEntry, namesGEntry, ageGEntry, genderGEntry, nationalityGEntry]
    return [entry.get(0.0, "end-1c") for entry in entries]

namesGLabel = customtkinter.CTkLabel(tab1, text = "Nombre(s):  ", fg_color = "transparent") # Nombre(s)
namesGLabel.grid(row = 0, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
namesGEntry = customtkinter.CTkTextbox(tab1, width = 300, height = 10)
namesGEntry.grid(row = 0, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "e")

surPGLabel = customtkinter.CTkLabel(tab1, text = "Apellido Paterno: ", fg_color = "transparent") # Apellido Paterno
surPGLabel.grid(row = 1, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
surPGEntry = customtkinter.CTkTextbox(tab1, width = 300, height = 10)
surPGEntry.grid(row = 1, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")

surMGLabel = customtkinter.CTkLabel(tab1, text = "Apellido Materno: ", fg_color = "transparent") # Apellida Materno
surMGLabel.grid(row = 2, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
surMGEntry = customtkinter.CTkTextbox(tab1, width = 300, height = 10)
surMGEntry.grid(row = 2, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")

ageGLabel = customtkinter.CTkLabel(tab1, text = "Edad:  ", fg_color = "transparent") # Edad
ageGLabel.grid(row = 3, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
ageGEntry = customtkinter.CTkTextbox(tab1, width = 300, height = 10)
ageGEntry.grid(row=3, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "e")

genderGLabel = customtkinter.CTkLabel(tab1, text="Género:  ", fg_color="transparent") # Género
genderGLabel.grid(row=4, column = 0, padx=1,pady=5,ipady=0,sticky="e")
genderGEntry = customtkinter.CTkOptionMenu(tab1, values=["Hombre", "Hombre", "Hombre LGBTTTIQ+", "Mujer LGBTTTIQ+"])
genderGEntry.grid(row=4, column = 1, padx=1,pady=5,ipady=0,sticky="e")

nationalityGLabel = customtkinter.CTkLabel(tab1, text="Nacionalidad:  ", fg_color="transparent")
nationalityGLabel.grid(row=5, column = 0, padx=1,pady=5,ipady=0,sticky="e")
nationalityGEntry = customtkinter.CTkTextbox(tab1, width = 300, height = 10)
nationalityGEntry.grid(row=5, column = 1, padx=1,pady=5,ipady=0,sticky="e")

#submitGBtn = customtkinter.CTkButton(tab1, text="Registrar", width=50, command = lambda: General.new_entry(workbook, getGText(), app))
#submitGBtn.grid(row = 7, column = 0, padx=1,pady=5,ipady=0,sticky="e")



# Pestaña: Registro Legal
def getLText():
    entries = [nameLEntry, L2Entry, L3Entry, L4Entry, L5Entry, L6Entry, L7Entry, L8Entry, L9Entry, L10Entry, L11Entry, L12Entry, L13Entry]
    return [entry.get(0.0, "end-1c") for entry in entries]

nameLLabel = customtkinter.CTkLabel(tab2, text="Nombre:  ", fg_color="transparent")
nameLLabel.grid(row=0, column = 0, padx=1,pady=5,ipady=0,sticky="e")
nameLEntry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
nameLEntry.grid(row=0, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L2Label = customtkinter.CTkLabel(tab2, text="Orientaciones Legales:  ", fg_color="transparent")
L2Label.grid(row=1, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L2Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L2Entry.grid(row=1, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L3Label = customtkinter.CTkLabel(tab2, text="Asesorías Legales:  ", fg_color="transparent")
L3Label.grid(row=2, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L3Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L3Entry.grid(row=2, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L4Label = customtkinter.CTkLabel(tab2, text="Solicitud de Refugiado:  ", fg_color="transparent")
L4Label.grid(row=3, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L4Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L4Entry.grid(row=3, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L5Label = customtkinter.CTkLabel(tab2, text="Regularización por Razones Humanitarias:  ", fg_color="transparent")
L5Label.grid(row=4, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L5Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L5Entry.grid(row=4, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L6Label = customtkinter.CTkLabel(tab2, text="Regularización por Unidad Familiar:  ", fg_color="transparent")
L6Label.grid(row=5, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L6Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L6Entry.grid(row=5, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L7Label = customtkinter.CTkLabel(tab2, text="Cambio de Condición de Estancia:  ", fg_color="transparent")
L7Label.grid(row=7, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L7Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L7Entry.grid(row=7, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L8Label = customtkinter.CTkLabel(tab2, text="Renovaciones:  ", fg_color="transparent")
L8Label.grid(row=8, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L8Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L8Entry.grid(row=8, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L9Label = customtkinter.CTkLabel(tab2, text="Resposición de Documento Migratorio:  ", fg_color="transparent")
L9Label.grid(row=9, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L9Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L9Entry.grid(row=9, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L10Label = customtkinter.CTkLabel(tab2, text="Notificación de Cambio de Domicilio:  ", fg_color="transparent")
L10Label.grid(row=10, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L10Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L10Entry.grid(row=10, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L11Label = customtkinter.CTkLabel(tab2, text="Notificación de Cambio de Nacionalidad:  ", fg_color="transparent")
L11Label.grid(row=11, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L11Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L11Entry.grid(row=11, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L12Label = customtkinter.CTkLabel(tab2, text="Notificación de Cambio de Lugar de Trabajo:  ", fg_color="transparent")
L12Label.grid(row=12, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L12Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L12Entry.grid(row=12, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L13Label = customtkinter.CTkLabel(tab2, text="Canalización de las Personas Migrantes a \nlos consulados de Honduras, \nGuatemala y el Salvador:  ", fg_color="transparent")
L13Label.grid(row=13, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L13Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L13Entry.grid(row=13, column = 1, padx=1,pady=5,ipady=0,sticky="e")

#submitLBtn = customtkinter.CTkButton(tab2, text="Registrar", width=50, command = lambda: Legal.new_entry(workbook, getLText()))
#submitLBtn.grid(row = 14, column = 0, padx=1,pady=5,ipady=0,sticky="e")

app.mainloop()
