import webbrowser

def Badland():

    print(
        "1.Gasloine"
        "2.control"
        "3.Hold me down"
        "4.Strange love"
        "5.Ghost"
        "6.Walk on a Line"
        )

    Usr_song = int(input("Please Select the number"))
    

    if Usr_song == 1:
        url = "https://www.youtube.com/watch?v=zRHNi3QfFlE"
        new=0
        webbrowser.open(url,new)

    if Usr_song == 2:
        url ="https://www.youtube.com/watch?v=so8V5dAli-Q"
        new = 0
        webbrowser.open(url,new)

    if Usr_song == 3:
        url ="https://www.youtube.com/watch?v=xKnG2d9tZdU&index=11&list=PL_z2rRJd3xt4pdxj-Poa_lChQXY3yOk05"
        new = 0
        webbrowser.open(url,new)

    if Usr_song == 4:
        url ="https://www.youtube.com/watch?v=x-Jo25SL56A&index=9&list=PL_z2rRJd3xt4pdxj-Poa_lChQXY3yOk05"
        new = 0
        webbrowser.open(url,new)

    if Usr_song == 5:
        url ="https://www.youtube.com/watch?v=ao4o-XRU_KM&index=15&list=PL_z2rRJd3xt4pdxj-Poa_lChQXY3yOk05"
        new = 0
        webbrowser.open(url,new)

    if Usr_song == 6:
        url="https://www.youtube.com/watch?v=8qjl4lysi_s&list=PL_z2rRJd3xt4pdxj-Poa_lChQXY3yOk05&index=7"
        new = 0
        webbrowser.open(url,new)
            
            
Badland()
