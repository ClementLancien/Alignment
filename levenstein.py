def levenstein (x,y) :

    seq1 = ""
    seq2= ""
    d = 0
    (i,k,i1,k1,i2,k2,i3,k3) = ("","","","","","","","")
   
   
    if len(x) == 0:

        d = len(y)
        seq1 = seq1 + "-" * d
        seq2 = y
        return (d,seq1, seq2)
    
       
    elif len(y) == 0:

        d = len (x)
        seq2 = seq2 + "-" * d
        seq1 = x
        return (d,seq1, seq2)
      
   
    elif x[0] == y [0]:

        c = y[0]
        (d, i, k) =levenstein(x[1:], y[1:])
        seq1 = c + i
        seq2 = c + k
        return (d,seq1, seq2)
       
    else:

        (distance1, i1, k1) = levenstein(x[1:], y[1:])
        (distance2, i2, k2) = levenstein(x[1:], y[0:])
        (distance3, i3, k3) = levenstein(x[0:], y[1:])
       
        mdistance= min(distance1, distance2, distance3)
       
        if (mdistance == distance1):
            seq1 = x[0] + i1
            seq2 = y[0] + k1 
        elif(mdistance == distance2):
            seq1= x[0] + i2 
            seq2 = "-" + k2
        else:
            seq1 = "-" + i3
            seq2 = y[0] + k3
           
        d= mdistance + 1  
           
        return (d,seq1, seq2)
