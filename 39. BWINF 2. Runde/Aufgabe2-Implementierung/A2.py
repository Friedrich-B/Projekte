# import zur Überprüfung des Pfades
import os


# enthält Obstsorten und die Schalen, aus denen sie entnommen wurden
class Spiess:
    def __init__(self, schalen: list, obst: list):
        self.schalen = schalen
        self.obst = obst


# enthält ein Obst und die Schale/n der/denen es zugewiesen wurde
class Obst:
    def __init__(self, obst: str, schale):
        self.obst = obst
        self.schale = schale


# überprüft den Pfad und sorgt für weiteren Programmablauf
def get_input():
    path = input("gib den pfad der datei an: ")
    # Überprüfung des Pfades auf Richtigkeit
    if os.path.exists(path):
        find_bowls(path)
    else:
        print("Fehler: überprüfe den Pfad und versuche es erneut")
        exit()


# der eigentliche Programmablauf
def find_bowls(path):
    # ------------------------ Einlesen der Daten -------------------------


    # Einlesen der Datei
    file = open(path, "r")
    # anzahl der Obstsorten/Schalen
    alle_sorten = int(file.readline())
    # die gewünschten Früchte
    wuensche = file.readline().split()
    # Anzahl der Spieße
    anzahl = int(file.readline())
    # enthält alle Daten zu den Spießen
    inhalt = []

    # instanziiert "Spiess"-Objekte und fügt diese der Liste "inhalt" hinzu
    for i in range(anzahl):
        schalen = file.readline().split()
        for j in range(len(schalen)):
            schalen[j] = int(schalen[j])
        obst = file.readline().split()
        inhalt.append(Spiess(schalen, obst))


    # -------------------------- Verarbeitung der Daten ----------------------------


    # enthält alle Schalen
    schalen = []
    for i in range(alle_sorten):
        schalen.append(i + 1)

    # enthält alle Schalen, aus denen Obst entnommen wurde
    schalen_genannt = []
    for i in inhalt:
        for j in i.schalen:
            if j not in schalen_genannt:
                schalen_genannt.append(j)

    # enthält alle schalen, aus denen kein Obst entnommen wurde
    schalen_nicht_genannt = []
    for i in schalen:
        if i not in schalen_genannt:
            schalen_nicht_genannt.append(i)

    # das auf den Spießen vorkommende Obst
    obst_genannt = []
    for i in inhalt:
        for j in i.obst:
            if j not in obst_genannt:
                obst_genannt.append(j)

    # alles vorkommende Obst
    obst_alles = []
    for i in obst_genannt:
        obst_alles.append(i)
    for i in wuensche:
        if i not in obst_alles:
            obst_alles.append(i)

    # kommt nicht auf den Spießen vor
    obst_nicht_genannt = []
    for i in wuensche:
        if i not in obst_genannt:
            obst_nicht_genannt.append(i)

    # liste der "Spiess"-Objekte mit gewolltem Obst
    mag_er = []
    # liste der "Spiess"-Objekte mit ungewolltem Obst
    mag_er_nicht = []

    # überprüft, ob die Spieße Obstsorten enthalten, die Donald mag
    for i in inhalt:
        search = True
        for j in i.obst:
            for s in wuensche:
                if j == s:
                    mag_er.append(i)
                    search = False
                    break
            if not search:
                break
        if search:
            mag_er_nicht.append(i)

    # entfernt Schalen und Obst von mag_er welche in mag_er_nicht vorkommen
    for i in mag_er:
        for j in mag_er_nicht:
            for k in range(len(j.obst)):
                frucht = j.obst[k]
                bowl = j.schalen[k]
                if frucht in i.obst:
                    # entfernt ungewolltes Obst
                    i.obst.pop(i.obst.index(frucht))
                if frucht in obst_alles:
                    # entfernt ungewolltes Obst
                    obst_alles.pop(obst_alles.index(frucht))
                if bowl in i.schalen:
                    # entfernt unnötige Schalen
                    i.schalen.pop(i.schalen.index(bowl))
                if bowl in schalen:
                    # entfernt unnötige Schalen
                    schalen.pop(schalen.index(bowl))

    # liste der zugewiesenen Schalen und Obstsorten
    results = []
    # liste der zugewiesenen Schalen und Obstsorten, mit gewolltem Obst
    results_wanted = []
    # liste der zugewiesenen Schalen und Obstsorten, ohne gewolltes Obst
    results_unwanted = []

    # instanziiert nicht auf Spießen vorkommendes Obst als "Obst"-Objekte
    for i in obst_nicht_genannt:
        results.append(Obst(i, schalen_nicht_genannt))
        obst_alles.pop(obst_alles.index(i))

    # Zuweisung von Obst zu Schale/n
    for frucht in range(len(obst_alles)):
        # Spieße, welche "frucht" enthalten
        enthaltenIn = []
        # Spieße, welche "frucht" nicht enthalten
        nichtEnthaltenIn = []
        # Schalen der Spieße, welche "frucht" nicht enthalten
        nichtEnthaltenInSchalen = []
        # mögliche Schalen von "frucht"
        schaleMoeglich = []
        # endgültige Schalen von "frucht"
        schaleErgebnis = []

        # sortiert die Spieße danach, ob "frucht" enthalten ist
        for spiess in range(len(mag_er)):
            if obst_alles[frucht] in mag_er[spiess].obst:
                enthaltenIn.append(mag_er[spiess])
            else:
                nichtEnthaltenIn.append(mag_er[spiess])

        leng = len(enthaltenIn)
        if leng > 1:
            # enthalten alle Spieße, welche "frucht" enthalten, die selbe Schale, wird sie einer neuen Liste hinzugefügt
            for i in enthaltenIn[0].schalen:
                if check_for_bowl(i, enthaltenIn, leng - 1):
                    schaleMoeglich.append(i)
        else:
            schaleMoeglich = enthaltenIn[0].schalen

        # führt Schalen der Spiesse, welche "frucht" nicht enthalten, in einer Liste zusammen
        if len(nichtEnthaltenIn):
            for obj in nichtEnthaltenIn:
                for bowl in obj.schalen:
                    if bowl not in nichtEnthaltenInSchalen:
                        nichtEnthaltenInSchalen.append(bowl)

        # fügt Schalen neuer Liste hinzu, sofern diese nicht auf einem Spiess ohne "frucht" vorkamen
        if len(nichtEnthaltenIn):
            for bowl in schaleMoeglich:
                if bowl not in nichtEnthaltenInSchalen:
                    schaleErgebnis.append(bowl)
        else:
            schaleErgebnis = schaleMoeglich

        # instanziiert das endgültige "Obst"-Objekt
        results.append(Obst(obst_alles[frucht], schaleErgebnis))


    # ------------------------------- Auswertung der Daten ----------------------------------


    # sortiert die "Obst"-Objekte danach, ob sie eine Wunschsorte enthalten
    for res in results:
        if res.obst in wuensche:
            results_wanted.append(res)
        else:
            results_unwanted.append(res)

    # Liste mit "Obst" welches nicht in einer Schale sein kann, in der ein ungewolltes "Obst" sein kann
    eindeutig = []
    # Liste mit "Obst" welches in einer Schale sein kann, in der ein ungewolltes "Obst" sein kann
    nicht_eindeutig = []

    # sortiert gewollets "Obst" danach, ob es die selben Schalen hat, wie ungewolltes "Obst"
    for want in results_wanted:
        eind = True
        for un in results_unwanted:
            if un.schale[0] in want.schale:
                nicht_eindeutig.append([want, un])
                eind = False
        if eind:
            eindeutig.append(want)

    # Ausgabe entsprechend der Sortierung nach Eindeutigkeit
    if len(eindeutig):
        print("\n\nBei diesen Obstsorten besteht kein Risiko, eine ungewollte Obstsorte zu erwischen:")
        for res in eindeutig:
            if len(res.schale) > 1:
                print(f"{res.obst} befindet sich in einer der folgenden Schalen: {res.schale}.")
                continue
            print(f"{res.obst} befindet sich in Schale {int(res.schale[0])}.")

    if len(nicht_eindeutig):
        print(f"\n\nBei diesen Obstsorten besteht das Risiko, eine ungewollte Obstsorte zu erwischen:")
        for res in nicht_eindeutig:
            print(f"{res[0].obst} befindet sich in einer der folgenden Schalen: {res[0].schale}.\n"
                  f"Das ungewollte Obst {res[1].obst} befindet sich auch in einer dieser Schalen.\n")


# überprüft eine Liste von "Spiess"-Objekten, ob alle von ihnen die Schale "bowl" enthalten
def check_for_bowl(bowl, arr, length):
    if bowl in arr[length].schalen:
        if length > 0:
            return check_for_bowl(bowl, arr, length-1)
        else:
            return True
    else:
        return False


# Start des Programms
get_input()
