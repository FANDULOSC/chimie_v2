from tkinter import*
masse_nucléon=1.67*10**-27
masse_éléctron=9.109*10**-31
def hy(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    symbol = 'H'
    atome = 'Hydrogène'
    Z = 1
    A = 1
    Z1 = 1
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 1
    lewis = "H ."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu=Tk()
    feu.title(atome)
    texte1= Label(feu,text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/hydrogene.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu,text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A-Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def li(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    atome = 'Lithium'
    symbol = 'Li'
    Z = 3
    A = 7
    Z1 = 3
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 1
    lewis = "Li ."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/lithium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def so(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    symbol = "Na"
    atome = 'Sodium'
    A = 23
    Z = 11
    Z1 = 11
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 1
    lewis = 'Na .'
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/sodium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def po(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 39
    Z = 19
    Z1 = 19
    atome = 'Potassium'
    symbol = 'K'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 1
    lewis = 'K .'
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/potassium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ru(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 85
    Z = 37
    Z1 = 37
    atome = ' Rubidium'
    symbol = 'Rb'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 1
    lewis = 'Rb .'
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/rubidium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ce(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 133
    Z = 55
    Z1 = 55
    atome = ' Césium'
    symbol = 'Cs'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 1
    lewis = 'Cs .'
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/cesium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def fr(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 223
    Z = 87
    Z1 = 87
    atome = ' Francium'
    symbol = 'Fr'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 1
    lewis = "Fr ."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/francium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def be(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    symbol = 'Be'
    atome = ' Béryllium'
    A = 9
    Z = 4
    Z1 = 4
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 2
    lewis = "Be .."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/beryllium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ma(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 24
    Z = 12
    Z1 = 12
    atome = ' Magnésium'
    symbol = 'Mg'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 2
    lewis = 'Mg ..'
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/magnesium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ca(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 40
    Z = 20
    Z1 = 20
    atome = ' Calcium'
    symbol = 'Ca'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 2
    lewis = 'Ca ..'
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/calcium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def st(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 88
    Z = 38
    Z1 = 38
    atome = ' Strontium'
    symbol = 'Sr'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 2
    lewis = 'Sr ..'
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/strontium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ba(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 138
    Z = 56
    Z1 = 56
    atome = ' Baryum'
    symbol = 'Ba'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 2
    lewis = 'Ba ..'
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/baryum.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ra(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 226
    Z = 88
    Z1 = 88
    atome = ' Radium'
    symbol = 'Ra'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 2
    lewis = 'Ra ..'
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/radium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def sc(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    symbol = 'Sc'
    A = 45
    Z = 21
    Z1 = 21
    atome = ' Scandium'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 3
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/scandium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def yt(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 89
    Z = 39
    Z1 = 39
    symbol = 'Y'
    atome = ' Ytterium'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 3
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/yttrium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ti(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 48
    Z = 22
    Z1 = 22
    atome = ' Titane'
    symbol = 'Ti'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 4
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/titane.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def zi(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 90
    Z = 40
    Z1 = 40
    atome = ' Zirconium'
    symbol = 'Zr'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 4
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/zirconium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ha(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 180
    Z = 72
    Z1 = 72
    atome = ' Hafnium'
    symbol = 'Hf'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 4
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/hafnium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ruth(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 261
    Z = 104
    Z1 = 104
    symbol = 'Rf'
    atome = ' Rutherfordium'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 4
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/rutherfordium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def va(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 51
    Z = 23
    Z1 = 23
    symbol = 'V'
    atome = ' Vanadium'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 5
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/vanadium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ni(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 93
    Z = 41
    Z1 = 41
    atome = ' Nionium'
    symbol = 'Nb'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 5
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/niobium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ta(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 181
    Z = 73
    Z1 = 73
    symbol = 'Ta'
    atome = ' Tantale'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 5
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/tantale.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def du(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 262
    Z = 105
    Z1 = 105
    atome = 'Dubnium'
    symbol = 'Db'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 5
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/dubnium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ch(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 52
    Z = 24
    Z1 = 24
    atome = ' Chrome'
    symbol = 'Cr'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 6
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/chrome.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def mo(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 98
    Z = 42
    Z1 = 42
    atome = ' Molybdène'
    symbol = 'Mo'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 6
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/molybdene.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def tu(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 184
    Z = 74
    Z1 = 74
    atome = ' Tungstène'
    symbol = 'W'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 6
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/tungstene.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def se(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 266
    Z = 106
    Z1 = 106
    atome = ' Seaborgium'
    symbol = 'Sg'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 6
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/seaborgium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def mang(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 55
    Z = 25
    Z1 = 25
    symbol = 'Mn'
    atome = 'Manganèse'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 7
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/manganese.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def te(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    Z = 43
    A = 98
    Z1 = 43
    atome = 'Technétium'
    symbol = 'Tc'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 7
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/technetium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def rh(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 187
    Z = 75
    Z1 = 75
    atome = 'Rhénium'
    symbol = 'Re'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 7
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/rhenium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def bh(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 264
    Z = 107
    Z1 = 107
    atome = 'Borhium'
    symbol = 'Bh'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 7
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/bohrium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def fe(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 56
    Z = 26
    Z1 = 26
    symbol = 'Fe'
    atome = 'Fer'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 8
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/fer.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ruthen(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 102
    Z = 44
    Z1 = 44
    symbol = 'Ru'
    atome = 'Ruthénium'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 8
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/ruthenium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def os(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 192
    Z = 76
    Z1 = 76
    atome = 'Osmium'
    symbol = 'Os'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 8
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/osmium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def hass(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 277
    Z = 108
    Z1 = 108
    atome = 'Hassium'
    symbol = 'Hs'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 8
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/hassium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def co(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 59
    Z = 27
    Z1 = 27
    atome = 'Cobalt'
    symbol = 'Co'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 9
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/cobalt.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def rhod(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 103
    Z = 45
    Z1 = 45
    atome = 'Rhodium'
    symbol = 'Rh'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 9
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/rhodium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ir(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 193
    Z = 77
    Z1 = 77
    symbol = 'Ir'
    atome = 'Iridium'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 9
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/iridium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def me(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 268
    Z = 109
    Z1 = 109
    symbol = 'Mt'
    atome = 'Méitenerium'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 9
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/meitnerium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def nick(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 58
    Z = 28
    Z1 = 28
    atome = 'Nickel'
    symbol = 'Ni'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f',
              '6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 10
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/nickel.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def pa(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 106
    Z = 46
    Z1 = 46
    atome = 'Palladium'
    symbol = 'Pd'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 10
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/palladium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def plat(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 195
    Z = 78
    Z1 = 78
    atome = 'Platine'
    symbol = 'Pt'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 10
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/platine.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def da(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 271
    Z = 110
    Z1 = 110
    atome = 'Darmstadium'
    symbol = 'Ds'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 10
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/darmstadtium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def cu(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 63
    Z = 29
    Z1 = 29
    atome = 'Cuivre'
    symbol = 'Cu'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 11
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/cuivre.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ar(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 107
    Z = 47
    Z1 = 47
    symbol = 'Ag'
    atome = 'Argent'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 11
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/argent.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def orpn(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 197
    Z = 79
    Z1 = 79
    symbol = 'Au'
    atome = 'Or'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 11
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/or.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ro(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 272
    Z = 111
    Z1 = 111
    symbol = 'Rg'
    atome = 'Roentgénium'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 11
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/roentgenium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def zinc(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 64
    Z = 30
    Z1 = 30
    symbol = 'Zn'
    atome = 'Zinc'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 12
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/zinc.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def cadm(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 114
    Z = 48
    Z1 = 48
    atome = 'Cadmium'
    symbol = 'Cd'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 12
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/cadmium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def merc(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 202
    Z = 80
    Z1 = 80
    atome = 'Mercure'
    symbol = 'Hg'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 12
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/mercure.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def cope(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 285
    Z = 112
    Z1 = 112
    atome = 'Copernicium'
    symbol = 'Cn'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 12
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/copernicium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def bo(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 11
    Z = 5
    Z1 = 5
    atome = 'Bore'
    symbol = 'B'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 3
    lewis = "B ..."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/bore.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def al(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 27
    Z = 13
    Z1 = 13
    atome = 'Aluminium'
    symbol = 'Al'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 3
    lewis = "Al ..."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/aluminium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ga(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 69
    Z = 31
    Z1 = 31
    symbol = 'Ga'
    atome = 'Gallium'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 3
    lewis = "Ga ..."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/gallium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def indi(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 115
    Z = 49
    Z1 = 49
    atome = 'Indium'
    symbol = 'In'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 3
    lewis = "In ..."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/indium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def th(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 205
    Z = 81
    Z1 = 81
    atome = 'Thallium'
    symbol = 'Tl'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 3
    lewis = "Tl ..."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/thallium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def niho(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 284
    Z = 113
    Z1 = 113
    atome = 'Nihonium'
    symbol = 'Nh'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 3
    lewis = "Nh ..."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/nihonium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def carb(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    Z = 6
    A = 12
    Z1 = 6
    atome = 'Carbone'
    symbol = 'C'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 4
    lewis = "C ...."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/carbone.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def si(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 28
    Z = 14
    Z1 = 14
    atome = 'Sillicium'
    symbol = 'Si'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 4
    lewis = "Si ...."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/silicium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ge(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 74
    Z = 32
    Z1 = 32
    symbol = 'Ge'
    atome = 'Germanium'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 4
    lewis = "Ge ...."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/germanium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def et(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 120
    Z = 50
    Z1 = 50
    atome = 'Etain'
    symbol = 'Sn'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 4
    lewis = "Sn ...."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/etain.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def plom(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 208
    Z = 82
    Z1 = 82
    atome = 'Plomb'
    symbol = 'Pb'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 4
    lewis = "Pb ...."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/plomb.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def fl(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 289
    Z = 114
    Z1 = 114
    atome = 'Flévorium'
    symbol = 'Fl'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 4
    lewis = "Fl ...."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/flerovium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def az(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 14
    Z = 7
    Z1 = 7
    atome = 'Azote'
    symbol = 'N'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 5
    lewis = "N :..."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/azote.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ph(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 31
    Z = 15
    Z1 = 15
    atome = 'Phosphore'
    symbol = 'P'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 5
    lewis = 'P :...'
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/phosphore.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def arse(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 75
    Z = 33
    Z1 = 33
    atome = 'Arsenic'
    symbol = 'As'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 5
    lewis = "As :..."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/arsenic.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def an(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 121
    Z = 51
    Z1 = 51
    atome = 'Antimoine'
    symbol = 'Sb'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 5
    lewis = "Sb :..."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/antimoine.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def bi(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 209
    Z = 83
    Z1 = 83
    atome = 'Bismuth'
    symbol = 'Bi'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 5
    lewis = "Bi :..."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/bismuth.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def mosc(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    symbol = 'Mc'
    A = 288
    Z = 115
    Z1 = 115
    atome = 'Moscovium'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 5
    lewis = "MC :..."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/moscovium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ox(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 16
    Z = 8
    Z1 = 8
    atome = 'Oxygène'
    symbol = 'O'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 2, 6, 2, 2, 6, 2, 2, 2, 6, 2, 2, 2]
    config = ""
    i = 0
    while Z1 > 0:
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 6
    lewis = "O ::.."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/oxygene.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def souf(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 32
    Z = 16
    Z1 = 16
    atome = 'Soufre'
    symbol = 'S'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 6
    lewis = "S ::.."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/soufre.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def sele(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 80
    Z = 34
    Z1 = 34
    atome = 'Sélénium'
    symbol = 'Se'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 6
    lewis = "Se ::.."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/selenium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def tell(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 130
    Z = 52
    Z1 = 52
    atome = 'Tellure'
    symbol = 'Te'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 6
    lewis = "Te ::.."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/tellure.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def polo(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 210
    Z = 84
    Z1 = 84
    atome = 'Polonium'
    symbol = 'Po'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 6
    lewis = "Po ::.."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/polonium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def live(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 292
    Z = 116
    Z1 = 116
    symbol = 'Lv'
    atome = 'Livermorium'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 6
    lewis = "Lv ::.."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/livermorium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def fluo(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 19
    Z = 9
    Z1 = 9
    symbol = 'F'
    atome = 'Fluor'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 7
    lewis = "F :::."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/fluor.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def chlo(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 35
    Z = 17
    Z1 = 17
    atome = 'Chlore'
    symbol = 'Cl'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 7
    lewis = "Cl :::."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/chlore.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def br(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 79
    Z = 35
    Z1 = 35
    atome = 'Brome'
    symbol = 'Br'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 7
    lewis = "Br :::."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/brome.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def iode(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 127
    Z = 53
    Z1 = 53
    atome = 'Iode'
    symbol = 'I'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 7
    lewis = "I :::."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/iode.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def asta(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 210
    Z = 85
    Z1 = 85
    atome = 'Astate'
    symbol = 'At'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 7
    lewis = "At :::."
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/astate.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def tenn(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 292
    Z = 117
    Z1 = 117
    atome = 'Tennesse'
    symbol = 'Ts'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 7
    lewis = 'Ts :::.'
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/tennesse.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def he(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 4
    Z = 2
    Z1 = 2
    atome = 'Hélium'
    symbol = 'He'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 2
    lewis = "He :"
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/helium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ne(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 20
    Z = 10
    Z1 = 10
    atome = 'Néon'
    symbol = 'Ne'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 8
    lewis = "Ne ::::"
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/neon.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def argon(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 40
    Z = 18
    Z1 = 18
    atome = 'Argon'
    symbol = 'Ar'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 8
    lewis = "Ar ::::"
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/argon.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def kr(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 84
    Z = 36
    Z1 = 36
    atome = 'Krypton'
    symbol = 'Kr'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 8
    lewis = "Kr ::::"
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/krypton.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def xe(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 129
    Z = 54
    Z1 = 54
    symbol = 'Xe'
    atome = 'Xénon'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 8
    lewis = "Xe ::::"
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/xenon.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def radon(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 222
    Z = 86
    Z1 = 86
    atome = 'Radon'
    symbol = 'Rn'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 8
    lewis = "Rn ::::"
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/radon.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def orga(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 294
    Z = 118
    Z1 = 118
    atome = 'Organesson'
    symbol = 'Og'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 8
    lewis = "Og ::::"
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/organesson.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Le schéma de lewis de l'atome est:{lewis}""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def lant(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 139
    Z = 57
    Z1 = 57
    atome = 'Lanthane'
    symbol = 'La'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 3
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/lanthane.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def acti(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 227
    Z = 89
    Z1 = 89
    symbol = 'Ac'
    atome = 'Actinium'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 3
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/actinium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ceri(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 139
    Z = 58
    Z1 = 58
    atome = 'Cérium'
    symbol = 'Ce'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 4
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/cerium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def thor(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 232
    Z = 90
    Z1 = 90
    atome = 'Thorium'
    symbol = 'Th'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 4
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/thorium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def pr(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 141
    Z = 59
    Z1 = 59
    symbol = 'Pr'
    atome = 'Prasédodyme'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 5
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/praseodyme.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def prot(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 231
    Z = 91
    Z1 = 91
    symbol = 'Pa'
    atome = 'Protactinium'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 5
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/protactinium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def neody(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 142
    Z = 60
    Z1 = 60
    atome = 'Néodyme'
    symbol = 'Nd'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 6
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/neodyme.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ur(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 238
    Z = 92
    Z1 = 92
    atome = 'Uranium'
    symbol = 'U'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 6
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/uranium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def prome(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 146
    Z = 61
    Z1 = 61
    atome = 'Prométhium'
    symbol = 'Pm'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 7
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/promethium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def nept(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 237
    Z = 93
    Z1 = 93
    atome = 'Neptunium'
    symbol = 'Np'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 7
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/neptunium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def sa(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 152
    Z = 62
    Z1 = 62
    atome = 'Samarium'
    symbol = 'Sm'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 8
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/samarium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def pl(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 244
    Z = 94
    Z1 = 94
    atome = 'Plutonium'
    symbol = 'Pu'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 8
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/plutonium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def eu(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 153
    Z = 63
    Z1 = 63
    atome = 'Europium'
    symbol = 'Eu'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 9
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/europium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def am(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 243
    Z = 95
    Z1 = 95
    atome = 'Américium'
    symbol = 'Am'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 9
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/americium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def gado(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 158
    Z = 64
    Z1 = 64
    atome = 'Gadolinium'
    symbol = 'Gd'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 10
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/gadolinium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def curi(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 247
    Z = 96
    Z1 = 96
    symbol = 'Cm'
    atome = 'Curium'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 10
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/curium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def terb(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 159
    Z = 65
    Z1 = 65
    atome = 'Terbium'
    symbol = 'Tb'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 11
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/terbium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def berke(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 247
    Z = 97
    Z1 = 97
    atome = 'Berkélium'
    symbol = 'Bk'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 11
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/berkélium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def dy(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 164
    Z = 66
    Z1 = 66
    atome = 'Dysprosium'
    symbol = 'Dy'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 12
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/dysprosium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def cali(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 251
    Z = 98
    Z1 = 98
    atome = 'Californium'
    symbol = 'Cf'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 12
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/californium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ho(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 165
    Z = 67
    Z1 = 67
    atome = 'Holmium'
    symbol = 'Ho'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 13
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/holmium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ei(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 254
    Z = 99
    Z1 = 99
    atome = 'Einsteinium'
    symbol = 'Es'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 13
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/einsteinium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def er(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A=166
    Z = 68
    Z1 = 68
    atome = 'Erbium'
    symbol = 'Er'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 14
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/erbium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def fermi(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 257
    Z = 100
    Z1 = 100
    atome = 'Fermium'
    symbol = 'Fm'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 14
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/fermium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def thul(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 169
    Z = 69
    Z1 = 69
    atome = 'Thulium'
    symbol = 'Tm'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 15
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/thulium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def mend(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 258
    Z = 101
    Z1 = 101
    atome = 'Mendélinium'
    symbol = 'Md'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 15
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/mendelevium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def ytter(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 174
    Z = 70
    Z1 = 70
    atome = 'Ytterbium'
    symbol = 'Yb'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 16
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/ytterbium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def no(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 259
    Z = 102
    Z1 = 102
    atome = 'Nobélium'
    symbol = 'No'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 16
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/nobelium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def lu(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 175
    Z = 71
    Z1 = 71
    atome = 'Lutétium'
    symbol = 'Lu'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 17
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets/lutécium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
def lawr(event):
    global feu
    global masse_nucléon
    global masse_éléctron
    A = 260
    Z = 103
    Z1 = 103
    atome = 'Lawrencium'
    symbol = 'Lr'
    levels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f','6d', '7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence = 17
    masse_noyau = A * masse_nucléon
    masse = Z * masse_éléctron + masse_noyau
    feu = Tk()
    feu.title(atome)
    texte1 = Label(feu, text=f"atome:{atome}")
    texte2 = Label(feu, text="INSTA:lopysc7")
    img = PhotoImage(file='assets1/lawrencium.PNG', master=feu)
    label1 = Label(feu, image=img, )
    texte3 = Label(feu, text=f"""
Le symbol de cette atome est:{symbol}
Le nombre de protons est:{Z}
Le nombre de neutrons est:{A - Z}
Le nombres d'éléctrons est:{Z}
Le nombres de nucléons est:{A}
La masse du noyau de {atome} est: {masse_noyau}kg
La masse de {atome} est: {masse}kg
L'atome a pour configuration électronique:{config}
L'atome posséde {valence} électrons de valence
Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible""")
    texte1.pack()
    texte2.pack()
    label1.pack()
    texte3.pack()
    feu.mainloop()
tab = Tk()
tab.title("tableau periodique")
width = tab.winfo_screenwidth()
height = tab.winfo_screenheight()
canvas = Canvas(tab, width=width, height=height)
hyd = PhotoImage(file="assets/hydrogene.PNG")
lit = PhotoImage(file="assets/lithium.PNG")
sod = PhotoImage(file="assets/sodium.PNG")
pot = PhotoImage(file="assets/potassium.PNG")
rub = PhotoImage(file="assets/rubidium.PNG")
ces = PhotoImage(file="assets/cesium.PNG")
fra = PhotoImage(file="assets/francium.PNG")
ber = PhotoImage(file="assets/beryllium.PNG")
mag = PhotoImage(file="assets/magnesium.PNG")
cal = PhotoImage(file="assets/calcium.PNG")
sto = PhotoImage(file="assets/strontium.PNG")
bar = PhotoImage(file="assets/baryum.PNG")
rad = PhotoImage(file="assets/radium.PNG")
sca = PhotoImage(file="assets/scandium.PNG")
ytt = PhotoImage(file="assets/yttrium.PNG")
la = PhotoImage(file="assets1/la.PNG")
tit = PhotoImage(file="assets/titane.PNG")
zir = PhotoImage(file="assets/zirconium.PNG")
haf = PhotoImage(file="assets/hafnium.PNG")
rut = PhotoImage(file="assets1/rutherfordium.PNG")
van = PhotoImage(file="assets/vanadium.PNG")
nio = PhotoImage(file="assets/niobium.PNG")
tan = PhotoImage(file="assets/tantale.PNG")
dub = PhotoImage(file="assets1/dubnium.PNG")
chr = PhotoImage(file="assets/chrome.PNG")
mol = PhotoImage(file="assets/molybdene.PNG")
tun = PhotoImage(file="assets/tungstene.PNG")
sea = PhotoImage(file="assets1/seaborgium.PNG")
man = PhotoImage(file="assets/manganese.PNG")
tec = PhotoImage(file="assets/technetium.PNG")
rhe = PhotoImage(file="assets/rhenium.PNG")
boh = PhotoImage(file="assets1/bohrium.PNG")
fer = PhotoImage(file="assets/fer.PNG")
ruthe = PhotoImage(file="assets/ruthenium.PNG")
osm = PhotoImage(file="assets/osmium.PNG")
has = PhotoImage(file="assets1/hassium.PNG")
cob = PhotoImage(file="assets/cobalt.PNG")
rho = PhotoImage(file="assets/rhodium.PNG")
iri = PhotoImage(file="assets/iridium.PNG")
mei = PhotoImage(file="assets1/meitnerium.PNG")
nic = PhotoImage(file="assets/nickel.PNG")
pal = PhotoImage(file="assets/palladium.PNG")
pla = PhotoImage(file="assets/platine.PNG")
dar = PhotoImage(file="assets1/darmstadtium.PNG")
cui = PhotoImage(file="assets/cuivre.PNG")
arg = PhotoImage(file="assets/argent.PNG")
orp = PhotoImage(file="assets/or.PNG")
roe = PhotoImage(file="assets1/roentgenium.PNG")
zin = PhotoImage(file="assets/zinc.PNG")
cad = PhotoImage(file="assets/cadmium.PNG")
mer = PhotoImage(file="assets/mercure.PNG")
cop = PhotoImage(file="assets1/copernicium.PNG")
bor = PhotoImage(file="assets/bore.PNG")
alu = PhotoImage(file="assets/aluminium.PNG")
gal = PhotoImage(file="assets/gallium.PNG")
ind = PhotoImage(file="assets/indium.PNG")
tha = PhotoImage(file="assets/thallium.PNG")
nih = PhotoImage(file="assets1/nihonium.PNG")
car = PhotoImage(file="assets/carbone.PNG")
sil = PhotoImage(file="assets/silicium.PNG")
ger = PhotoImage(file="assets/germanium.PNG")
eta = PhotoImage(file="assets/etain.PNG")
plo = PhotoImage(file="assets/plomb.PNG")
fle = PhotoImage(file="assets1/flerovium.PNG")
azo = PhotoImage(file="assets/azote.PNG")
pho = PhotoImage(file="assets/phosphore.PNG")
ars = PhotoImage(file="assets/arsenic.PNG")
ant = PhotoImage(file="assets/antimoine.PNG")
bis = PhotoImage(file="assets/bismuth.PNG")
mos = PhotoImage(file="assets1/moscovium.PNG")
oxy = PhotoImage(file="assets/oxygene.PNG")
sou = PhotoImage(file="assets/soufre.PNG")
sel = PhotoImage(file="assets/selenium.PNG")
tel = PhotoImage(file="assets/tellure.PNG")
pol = PhotoImage(file="assets/polonium.PNG")
liv = PhotoImage(file="assets1/livermorium.PNG")
flu = PhotoImage(file="assets/fluor.PNG")
chl = PhotoImage(file="assets/chlore.PNG")
bro = PhotoImage(file="assets/brome.PNG")
iod = PhotoImage(file="assets/iode.PNG")
ast = PhotoImage(file="assets/astate.PNG")
ten = PhotoImage(file="assets1/tennesse.PNG")
hel = PhotoImage(file="assets/helium.PNG")
neo = PhotoImage(file="assets/neon.PNG")
argo = PhotoImage(file="assets/argon.PNG")
kry = PhotoImage(file="assets/krypton.PNG")
xen = PhotoImage(file="assets/xenon.PNG")
rado = PhotoImage(file="assets/radon.PNG")
org = PhotoImage(file="assets1/organesson.PNG")
lan = PhotoImage(file="assets/lanthane.PNG")
act = PhotoImage(file="assets/actinium.PNG")
cer = PhotoImage(file="assets/cerium.PNG")
tho = PhotoImage(file="assets/thorium.PNG")
pra = PhotoImage(file="assets/praseodyme.PNG")
pro = PhotoImage(file="assets/protactinium.PNG")
neod = PhotoImage(file="assets/neodyme.PNG")
ura = PhotoImage(file="assets/uranium.PNG")
prom = PhotoImage(file="assets/promethium.PNG")
nep = PhotoImage(file="assets/neptunium.PNG")
sam = PhotoImage(file="assets/samarium.PNG")
plu = PhotoImage(file="assets/plutonium.PNG")
eur = PhotoImage(file="assets/europium.PNG")
ame = PhotoImage(file="assets/americium.PNG")
gad = PhotoImage(file="assets/gadolinium.PNG")
cur = PhotoImage(file="assets/curium.PNG")
ter = PhotoImage(file="assets/terbium.PNG")
berk = PhotoImage(file="assets/berkélium.PNG")
dys = PhotoImage(file="assets/dysprosium.PNG")
calif = PhotoImage(file="assets/californium.PNG")
hol = PhotoImage(file="assets/holmium.PNG")
ein = PhotoImage(file="assets/einsteinium.PNG")
erb = PhotoImage(file="assets/erbium.PNG")
ferm = PhotoImage(file="assets1/fermium.PNG")
thu = PhotoImage(file="assets/thulium.PNG")
men = PhotoImage(file="assets1/mendelevium.PNG")
ytte = PhotoImage(file="assets/ytterbium.PNG")
nob = PhotoImage(file="assets1/nobelium.PNG")
lut = PhotoImage(file="assets/lutécium.PNG")
law = PhotoImage(file="assets1/lawrencium.PNG")
leg = PhotoImage(file="assets1/legende.PNG")
hyd_id = canvas.create_image(200, 60, image=hyd)
lit_id = canvas.create_image(200, 140, image=lit)
sod_id = canvas.create_image(200, 220, image=sod)
pot_id = canvas.create_image(200, 300, image=pot)
rub_id = canvas.create_image(200, 380, image=rub)
ces_id = canvas.create_image(200, 460, image=ces)
fra_id = canvas.create_image(200, 540, image=fra)
ber_id = canvas.create_image(280, 140, image=ber)
mag_id = canvas.create_image(280, 220, image=mag)
cal_id = canvas.create_image(280, 300, image=cal)
sto_id = canvas.create_image(280, 380, image=sto)
bar_id = canvas.create_image(280, 460, image=bar)
rad_id = canvas.create_image(280, 540, image=rad)
sca_id = canvas.create_image(400, 300, image=sca)
ytt_id = canvas.create_image(400, 380, image=ytt)
la_id=canvas.create_image(380,615,image=la)
tit_id = canvas.create_image(480, 300, image=tit)
zir_id = canvas.create_image(480, 380, image=zir)
haf_id = canvas.create_image(480, 460, image=haf)
rut_id = canvas.create_image(480, 540, image=rut)
van_id = canvas.create_image(560, 300, image=van)
nio_id = canvas.create_image(560, 380, image=nio)
tan_id = canvas.create_image(560, 460, image=tan)
dub_id = canvas.create_image(560, 540, image=dub)
chr_id = canvas.create_image(640, 300, image=chr)
mol_id = canvas.create_image(640, 380, image=mol)
tun_id = canvas.create_image(640, 460, image=tun)
sea_id = canvas.create_image(640, 540, image=sea)
man_id = canvas.create_image(720, 300, image=man)
tec_id = canvas.create_image(720, 380, image=tec)
rhe_id = canvas.create_image(720, 460, image=rhe)
boh_id = canvas.create_image(720, 540, image=boh)
fer_id = canvas.create_image(800, 300, image=fer)
ruthe_id = canvas.create_image(800, 380, image=ruthe)
osm_id = canvas.create_image(800, 460, image=osm)
has_id = canvas.create_image(800, 540, image=has)
cob_id = canvas.create_image(880, 300, image=cob)
rho_id = canvas.create_image(880, 380, image=rho)
iri_id = canvas.create_image(880, 460, image=iri)
mei_id = canvas.create_image(880, 540, image=mei)
nic_id = canvas.create_image(960, 300, image=nic)
pal_id = canvas.create_image(960, 380, image=pal)
pla_id = canvas.create_image(960, 460, image=pla)
dar_id = canvas.create_image(960, 540, image=dar)
cui_id = canvas.create_image(1040, 300, image=cui)
arg_id = canvas.create_image(1040, 380, image=arg)
orp_id = canvas.create_image(1040, 460, image=orp)
roe_id = canvas.create_image(1040, 540, image=roe)
zin_id = canvas.create_image(1120, 300, image=zin)
cad_id = canvas.create_image(1120, 380, image=cad)
mer_id = canvas.create_image(1120, 460, image=mer)
cop_id = canvas.create_image(1120, 540, image=cop)
bor_id = canvas.create_image(1200, 140, image=bor)
alu_id = canvas.create_image(1200, 220, image=alu)
gal_id = canvas.create_image(1200, 300, image=gal)
ind_id = canvas.create_image(1200, 380, image=ind)
tha_id = canvas.create_image(1200, 460, image=tha)
nih_id = canvas.create_image(1200, 540, image=nih)
car_id = canvas.create_image(1280, 140, image=car)
sil_id = canvas.create_image(1280, 220, image=sil)
ger_id = canvas.create_image(1280, 300, image=ger)
eta_id = canvas.create_image(1280, 380, image=eta)
plo_id = canvas.create_image(1280, 460, image=plo)
fle_id = canvas.create_image(1280, 540, image=fle)
azo_id = canvas.create_image(1360, 140, image=azo)
pho_id = canvas.create_image(1360, 220, image=pho)
ars_id = canvas.create_image(1360, 300, image=ars)
ant_id = canvas.create_image(1360, 380, image=ant)
bis_id = canvas.create_image(1360, 460, image=bis)
mos_id = canvas.create_image(1360, 540, image=mos)
oxy_id = canvas.create_image(1440, 140, image=oxy)
sou_id = canvas.create_image(1440, 220, image=sou)
sel_id = canvas.create_image(1440, 300, image=sel)
tel_id = canvas.create_image(1440, 380, image=tel)
pol_id = canvas.create_image(1440, 460, image=pol)
liv_id = canvas.create_image(1440, 540, image=liv)
flu_id = canvas.create_image(1520, 140, image=flu)
chl_id = canvas.create_image(1520, 220, image=chl)
bro_id = canvas.create_image(1520, 300, image=bro)
iod_id = canvas.create_image(1520, 380, image=iod)
ast_id = canvas.create_image(1520, 460, image=ast)
ten_id = canvas.create_image(1520, 540, image=ten)
hel_id = canvas.create_image(1600, 60, image=hel)
neo_id = canvas.create_image(1600, 140, image=neo)
argo_id = canvas.create_image(1600, 220, image=argo)
kry_id = canvas.create_image(1600, 300, image=kry)
xen_id = canvas.create_image(1600, 380, image=xen)
rado_id = canvas.create_image(1600, 460, image=rado)
org_id = canvas.create_image(1600, 540, image=org)
lan_id = canvas.create_image(480, 690, image=lan)
act_id = canvas.create_image(480, 790, image=act)
cer_id = canvas.create_image(560, 690, image=cer)
tho_id = canvas.create_image(560, 790, image=tho)
pra_id = canvas.create_image(640, 690, image=pra)
pro_id = canvas.create_image(640, 790, image=pro)
neod_id = canvas.create_image(720, 690, image=neod)
ura_id = canvas.create_image(720, 790, image=ura)
prom_id = canvas.create_image(800, 690, image=prom)
nep_id = canvas.create_image(800, 790, image=nep)
sam_id = canvas.create_image(880, 690, image=sam)
plu_id = canvas.create_image(880, 790, image=plu)
eur_id = canvas.create_image(960, 690, image=eur)
ame_id = canvas.create_image(960, 790, image=ame)
gad_id = canvas.create_image(1040, 690, image=gad)
cur_id = canvas.create_image(1040, 790, image=cur)
ter_id = canvas.create_image(1120, 690, image=ter)
berk_id = canvas.create_image(1120, 790, image=berk)
dys_id = canvas.create_image(1200, 690, image=dys)
calif_id = canvas.create_image(1200, 790, image=calif)
hol_id = canvas.create_image(1280, 690, image=hol)
ein_id = canvas.create_image(1280, 790, image=ein)
erb_id = canvas.create_image(1360, 690, image=erb)
ferm_id = canvas.create_image(1360, 790, image=ferm)
thu_id = canvas.create_image(1440, 690, image=thu)
men_id = canvas.create_image(1440, 790, image=men)
ytte_id = canvas.create_image(1520, 690, image=ytte)
nob_id = canvas.create_image(1520, 790, image=nob)
lut_id = canvas.create_image(1600, 690, image=lut)
law_id = canvas.create_image(1600, 790, image=law)
leg_id = canvas.create_image(1040, 890, image=leg)
title_label = Label(tab, text="Tableau périodique des éléments chimiques")
insta_label = Label(tab, text="INSTA: lopysc7")
insta_label.config(font=("Arial", 18))
title_label.config(font=("Arial", 18))
canvas.tag_bind(hyd_id, "<Button-1>", hy)
canvas.tag_bind(lit_id, "<Button-1>", li)
canvas.tag_bind(sod_id, "<Button-1>", so)
canvas.tag_bind(pot_id, "<Button-1>", po)
canvas.tag_bind(rub_id, "<Button-1>", ru)
canvas.tag_bind(ces_id, "<Button-1>", ce)
canvas.tag_bind(fra_id, "<Button-1>", fr)
canvas.tag_bind(ber_id, "<Button-1>", be)
canvas.tag_bind(mag_id, "<Button-1>", ma)
canvas.tag_bind(cal_id, "<Button-1>", ca)
canvas.tag_bind(sto_id, "<Button-1>", st)
canvas.tag_bind(bar_id, "<Button-1>", ba)
canvas.tag_bind(rad_id, "<Button-1>", ra)
canvas.tag_bind(sca_id, "<Button-1>", sc)
canvas.tag_bind(ytt_id, "<Button-1>", yt)
canvas.tag_bind(tit_id, "<Button-1>", ti)
canvas.tag_bind(zir_id, "<Button-1>", zi)
canvas.tag_bind(haf_id, "<Button-1>", ha)
canvas.tag_bind(rut_id, "<Button-1>", ruth)
canvas.tag_bind(van_id, "<Button-1>", va)
canvas.tag_bind(nio_id, "<Button-1>", ni)
canvas.tag_bind(tan_id, "<Button-1>", ta)
canvas.tag_bind(dub_id, "<Button-1>", du)
canvas.tag_bind(chr_id, "<Button-1>", ch)
canvas.tag_bind(mol_id, "<Button-1>", mo)
canvas.tag_bind(tun_id, "<Button-1>", tu)
canvas.tag_bind(sea_id, "<Button-1>", se)
canvas.tag_bind(man_id, "<Button-1>", mang)
canvas.tag_bind(tec_id, "<Button-1>", te)
canvas.tag_bind(rhe_id, "<Button-1>", rh)
canvas.tag_bind(boh_id, "<Button-1>", bh)
canvas.tag_bind(fer_id, "<Button-1>", fe)
canvas.tag_bind(ruthe_id, "<Button-1>", ruthen)
canvas.tag_bind(osm_id, "<Button-1>", os)
canvas.tag_bind(has_id, "<Button-1>", hass)
canvas.tag_bind(cob_id, "<Button-1>", co)
canvas.tag_bind(rho_id, "<Button-1>", rhod)
canvas.tag_bind(iri_id, "<Button-1>", ir)
canvas.tag_bind(mei_id, "<Button-1>", me)
canvas.tag_bind(nic_id, "<Button-1>", nick)
canvas.tag_bind(pal_id, "<Button-1>", pa)
canvas.tag_bind(pla_id, "<Button-1>", plat)
canvas.tag_bind(dar_id, "<Button-1>", da)
canvas.tag_bind(cui_id, "<Button-1>", cu)
canvas.tag_bind(arg_id, "<Button-1>", ar)
canvas.tag_bind(orp_id, "<Button-1>", orpn)
canvas.tag_bind(roe_id, "<Button-1>", ro)
canvas.tag_bind(zin_id, "<Button-1>", zinc)
canvas.tag_bind(cad_id, "<Button-1>", cadm)
canvas.tag_bind(mer_id, "<Button-1>", merc)
canvas.tag_bind(cop_id, "<Button-1>", cope)
canvas.tag_bind(bor_id, "<Button-1>", bo)
canvas.tag_bind(alu_id, "<Button-1>", al)
canvas.tag_bind(gal_id, "<Button-1>", ga)
canvas.tag_bind(ind_id, "<Button-1>", indi)
canvas.tag_bind(tha_id, "<Button-1>", th)
canvas.tag_bind(nih_id, "<Button-1>", niho)
canvas.tag_bind(car_id, "<Button-1>", carb)
canvas.tag_bind(sil_id, "<Button-1>", si)
canvas.tag_bind(ger_id, "<Button-1>", ge)
canvas.tag_bind(eta_id, "<Button-1>", et)
canvas.tag_bind(plo_id, "<Button-1>", plom)
canvas.tag_bind(fle_id, "<Button-1>", fl)
canvas.tag_bind(azo_id, "<Button-1>", az)
canvas.tag_bind(pho_id, "<Button-1>", ph)
canvas.tag_bind(ars_id, "<Button-1>", arse)
canvas.tag_bind(ant_id, "<Button-1>", an)
canvas.tag_bind(bis_id, "<Button-1>", bi)
canvas.tag_bind(mos_id, "<Button-1>", mosc)
canvas.tag_bind(oxy_id, "<Button-1>", ox)
canvas.tag_bind(sou_id, "<Button-1>", souf)
canvas.tag_bind(sel_id, "<Button-1>", sele)
canvas.tag_bind(tel_id, "<Button-1>", tell)
canvas.tag_bind(pol_id, "<Button-1>", polo)
canvas.tag_bind(liv_id, "<Button-1>", live)
canvas.tag_bind(flu_id, "<Button-1>", fluo)
canvas.tag_bind(chl_id, "<Button-1>", chlo)
canvas.tag_bind(bro_id, "<Button-1>", br)
canvas.tag_bind(iod_id, "<Button-1>", iode)
canvas.tag_bind(ast_id, "<Button-1>", asta)
canvas.tag_bind(ten_id, "<Button-1>", tenn)
canvas.tag_bind(hel_id, "<Button-1>", he)
canvas.tag_bind(neo_id, "<Button-1>", ne)
canvas.tag_bind(argo_id, "<Button-1>", argon)
canvas.tag_bind(kry_id, "<Button-1>", kr)
canvas.tag_bind(xen_id, "<Button-1>", xe)
canvas.tag_bind(rado_id, "<Button-1>", radon)
canvas.tag_bind(org_id, "<Button-1>", orga)
canvas.tag_bind(lan_id, "<Button-1>", lant)
canvas.tag_bind(act_id, "<Button-1>", acti)
canvas.tag_bind(cer_id, "<Button-1>", ceri)
canvas.tag_bind(tho_id, "<Button-1>", thor)
canvas.tag_bind(pra_id, "<Button-1>", pr)
canvas.tag_bind(pro_id, "<Button-1>", prot)
canvas.tag_bind(neod_id, "<Button-1>", neody)
canvas.tag_bind(ura_id, "<Button-1>", ur)
canvas.tag_bind(prom_id, "<Button-1>", prome)
canvas.tag_bind(nep_id, "<Button-1>", nept)
canvas.tag_bind(sam_id, "<Button-1>", sa)
canvas.tag_bind(plu_id, "<Button-1>", pl)
canvas.tag_bind(eur_id, "<Button-1>", eu)
canvas.tag_bind(ame_id, "<Button-1>", am)
canvas.tag_bind(gad_id, "<Button-1>", gado)
canvas.tag_bind(cur_id, "<Button-1>", curi)
canvas.tag_bind(ter_id, "<Button-1>", terb)
canvas.tag_bind(berk_id, "<Button-1>", berke)
canvas.tag_bind(dys_id, "<Button-1>", dy)
canvas.tag_bind(calif_id, "<Button-1>", cali)
canvas.tag_bind(hol_id, "<Button-1>", ho)
canvas.tag_bind(ein_id, "<Button-1>", ei)
canvas.tag_bind(erb_id, "<Button-1>", er)
canvas.tag_bind(ferm_id, "<Button-1>", fermi)
canvas.tag_bind(thu_id, "<Button-1>", thul)
canvas.tag_bind(men_id, "<Button-1>", mend)
canvas.tag_bind(ytte_id, "<Button-1>", ytter)
canvas.tag_bind(nob_id, "<Button-1>", no)
canvas.tag_bind(lut_id, "<Button-1>", lu)
canvas.tag_bind(law_id, "<Button-1>", lawr)
title_label.pack()
insta_label.pack()
canvas.pack()
tab.mainloop()