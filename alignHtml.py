from alignment import *

def MSimilarite (a, b) :
    return a == b

def html(adn) :
    
    f = open("adn.txt", "r")
    ligne1 = f.readline()
    ligne2 = f.readline()
    seq1 = ligne1[0:len(ligne1) - 1]
    seq2 = ligne2
    
    (score, seq1align, seq2align) = align(seq1, seq2, -2, MSimilarite, "local", "lineaire")
    f.close()
    
    newseq1 = []
    newseq2 = []
    
    for v in range(len(seq1align)) :

        if seq1align[v] == "-" :

            newseq1.append("<font color = \"blue\">" + "-" + "</font>")
            newseq2.append("<font color = \"blue\">" + seq2align[v] + "</font>")

        elif seq2align[v] == "-" :

            newseq1.append("<font color = \"blue\">" + seq1align[v] + "</font>")
            newseq2.append("<font color = \"blue\">" + "-" + "</font>")

        else :

            if seq1align[v] != seq2align[v] :

                newseq1.append("<font color = \"red\">" + seq1align[v] + "</font>")
                newseq2.append("<font color = \"red\">" + seq2align[v] + "</font>")

            else :

                newseq1.append("<font color = \"green\">" + seq1align[v] + "</font>")
                newseq2.append("<font color = \"green\">" + seq2align[v] + "</font>")
            
    a = open("page.html", "w")
    a.write("<!DOCTYPE html> \n")
    a.write("<html>\n")
    a.write("<head>\n")
    a.write("<title>Alignement groupe 17</title>\n")
    a.write("</head>\n")
    a.write("<body>\n")
    a.write("<img src=\"./logo.png\" align=\"right\"/>\n")
    a.write("<p align=\"left\">Clément Lancien</p>\n")
    a.write("<center><h1><u>Alignement d'ADN</u></h1></center><br/>\n")
    a.write("Voici le resultat de l'alignement local lineaire de deux sequences d'ADN.\n")
    a.write("<br/>Le score de cet alignement est : <b>"+str(score)+"</b>.\n")
    a.write("<br/><u>Legende :</u> les <font color=\"green\">similitudes</font> sont affichees en <font color=\"green\">vert</font>, les <font color=\"red\">mutations</font> en <font color=\"red\">rouge</font>, et les <font color=\"blue\">insertions/deletions</font> en <font color=\"blue\">bleu</font>.<br/>\n")
    a.write("<table>\n")
    a.write("<tr><td>Premiere sequence alignee : </td>\n")
    
    for v in newseq1 :

        a.write("<td>" + v + "</td>")

    a.write("</tr><br/>\n")
    a.write("<tr><td>Deuxieme sequence alignee : </td>\n")
    
    for w in newseq2 :

        a.write("<td>" + w + "</td>")

    a.write("</tr><br/>\n")
    a.write("</table>\n")
    a.write("</body>\n")
    a.write("</html>\n")
    a.close()