#! /usr/bin/python
# encoding: utf-8

from numpy import *

def initGlobal(x, y, A, B, g, gap, coutouverture = 0):
	
	A[0, 0] = 0
	B[0, 0] = (0, 0)

	if gap == "lineaire":
		
		for a in range(1,len(x) + 1):
			
			A[0,a] = a * g
			B[0,a] = (0, a-1)
			
		for b in range(1,len(y) + 1):
			
			A[b,0] = b * g
			B[b,0] = (b-1, 0)

	elif gap == "constant":
		
		for a in range(1,len(x) + 1):
			
			A[0,a] = g
			B[0,a] = (0, 0)
			
		for b in range(1,len(y) + 1):
			
			A[b,0] = g
			B[b,0] = (0, 0)
			
	elif gap == "affine":
		
		for a in range(1,len (x) + 1):
			
			A[0,a] = coutouverture + a * g
			B[0,a] = (0, a - 1)
			
		for b in range(1,len(y) + 1):
				
			A[b,0] = coutouverture + b * g
			B[b,0] = (b - 1, 0)
			
	return (A,B)
	
def initLocal(x, y, B):

	
	for v in range(0, len(x) + 1):
		
		for w in range(0, len(y) + 1):
			
			B[w,v] = (w,v) 
	return (B)

def fillGlobal(x, y, A, B, g, S, gap, coutouverture = 0):
	
	if gap == "lineaire":
		
		for v in range(1, len(x) + 1):
			
			for w in range(1,len(y) + 1):
				
				score = max((A[w - 1, v - 1] + S(x[v - 1], y[w - 1])), 
						  (A[w - 1, v] + g), 
						  (A[w, v - 1] + g))
						  
				A[w,v] = score
				
				if score == A[w - 1, v -1] + S(x[v -1], y[w - 1]):
					
					B[w,v] = (w - 1, v - 1)
				
				elif score == A[w - 1,v] + g:
					
					B[w,v] = (w - 1,v)
				
				else:
					
					B[w,v] = (w,v - 1)
					
	elif gap == "affine":
		
		for v in range(1, len(x)+1):
			
			for w in range(1, len(y)+1) :
				
				gapg = g + coutouverture
				gaph = g + coutouverture
				
				if B[w, v-1] == (w, v-2): 
					
					gapgauche = g
					
				if B[w -1, v] == (w - 2, v): 
					
					gaphaut = g
					
				score = max((A[w-1, v-1] + S(x[v-1], y[w-1])), 
					          (A[w-1, v] + gaph), 
					          (A[w, v-1] +  gapg))
				A[w, v] = score
				
				if score == A[w-1, v-1]+ S(x[v-1], y[w-1]):
					
					B[w, v] = (w-1, v-1)
					
				elif score == A[w-1, v] + gaph:
					
					B[w, v] = (w-1, v)
					
				else :
					
					B[w, v] = (w, v-1)
				
	elif gap == "constant":
		
		for v in range(1,len(x) + 1):
			
			for w in range (1, len(y) + 1):
				
				maxl = A[w,v-1]
				positionmaxl = v - 1
					
				for a in range(v - 1):
					
					if A[w,a] >maxl:
						
						maxl= A[v,a]
						positionmaxl = a
						
				maxc = A[w-1,v]
				positionmaxc = w - 1
				
				for b in range(w - 1):
					
					if A[b,v] > maxc:
						
						maxc = A[b,v]
						positionmaxc = b
				
				score = max((A[w - 1,v - 1] + S(x[v - 1], y[w - 1])),
						  (maxl + g),
						  (maxc + g))
				A[w,v]= score
				
				if score == A[w - 1, v -1] + S(x[v -1], y[w - 1]):
					
					B[w,v] = (w - 1, v - 1)
				
				elif score == maxl + g:
					
					B[w,v] = (w,positionmaxl)
				
				else:
					
					B[w,v] = (positionmaxc,v)
					
	return (A,B)

def fillLocal(x, y, A, B, g, S, gap, coutouverture = 0):
	

	if gap == "lineaire":
		
		for v in range(1, len(x)+1):
			
			for w in range(1, len(y)+1):
				
				score= max((A[w - 1, v - 1] + S(x[v - 1], y[w - 1])),
					         (A[w - 1, v] + g), 
				                 (A[w, v - 1]+g),
				                 0) 
				A[w, v] = score
				
				if score == A[w - 1, v - 1] + S(x[v - 1], y[w - 1]): 
					
					B[w, v] = (w - 1, v - 1)
					
				elif score == A[w - 1, v] + g :
					
					B[w, v] = (w - 1, v)
					
				elif score== A[w, v - 1] + g :
					
					B[w, v] = (w, v - 1)
					
	elif gap == "affine":
	    
		for v in range(1, len(x)+1):
			
			for w in range(1, len(y)+1) :
				
				gapg = g + coutouverture
				gaph = g + coutouverture
				
				if B[w, v - 1] == (w, v - 2):
					
					gapg = g
					
				if B[w - 1, v] == (w - 2, v): 
					
					gaph = g
					
				score = max((A[w - 1, v - 1] + S(x[v-1], y[w-1])), 
						  (A[w - 1, v] + gaph),
						  (A[w, v - 1] + gapg),
						  0)
				
				A[w, v] = score
				
				if score == A[w - 1, v - 1] + S(x[v - 1], y[w - 1]):
					
					B[w, v] = (w - 1, v - 1)
					
				elif score == A[w - 1, v] + gaph:
					
					B[w, v] = (w - 1, v)
					
				elif score == A[w, v - 1] + gapg:
					
					B[w, v] = (w, v - 1)

	elif gap == "constant":
	    
		for v in range(1,len(x) + 1):
		
			for w in range(1, len(y) + 1) :
		    
				maxl= A[w, v - 1] 
				positionmaxl  = v - 1
				
				for a in range(v - 1):
					
					if A[w, a] > maxl:
						
						maxl = A[w, a]
						positionmaxl  = a
				
				maxc = A[w - 1, v]
				positionmaxc = w - 1
				
				for b in range(w - 1):
					
					if A[b, v] > maxc:
						
						maxc = A[b, v]
						positionmaxc = b
						
				score = max((A[w - 1, v - 1] + S(x[v - 1], y[w - 1])),
						  (maxl + g),
						  (maxc + g),
						  0)
				A[w, v] = score
				
				if score == A[w - 1, v - 1] + S(x[v - 1], y[w - 1]) :
					
					B[w, v] = (w - 1, v - 1)
					
				elif res == maxl + g :
					
					B[w,v] = (w,positionmaxl)
					
				elif res == maxc + g :
					
					B[w,v] = (positionmaxc,v)
	return (A,B)


def backtrack(x, y, A, B, p, mode):
    
    xaligne = ""
    yaligne = ""
    (ld, cd) = p
            
    if mode == "global" :
        while (ld, cd) != (0,0) :

            (py, px) = B[ld, cd]

            if (py, px) == (ld - 1, cd - 1) : 

                xaligne = x[cd-1] + xaligne 
                yaligne = y[ld-1] + yaligne 

            elif py== ld : 

                xaligne = x[px:cd] + xaligne
                yaligne = "-" * (cd - px) + yaligne

            elif px == cd: 

                xaligne = "-" * (ld - py) + xaligne
                yaligne = y[py:ld] + yaligne

            ld = py
            cd = px

    else :
        while A[ld, cd] != 0 : 

            (py, px) = B[ld, cd]

            if (py, px) == (ld - 1, cd - 1) : 

                xaligne = x[cd - 1] + xaligne 
                yaligne = y[ld - 1] + yaligne

            elif py == ld: 

                xalign = x[px:cd] + xalign
                yalign = "-" * (cd - px) + yalign

            elif px == cd: 

                xaligne = "-" * (ld - py) + xaligne
                yaligne = y[py:ld] + yaligne

            ld = py
            cd = px

    return (xaligne, yaligne)

def align(x, y, g, S, mode, gap, coutouverture=0):
    
    nx, ny = len(x) + 1, len(y) + 1
    A = zeros( (ny, nx), dtype = float )
    B = empty( (ny, nx), dtype = object) 
    
    if mode == "global" :

        initGlobal(x, y, A, B, g, gap, coutouverture)
        fillGlobal(x, y, A, B, g, S, gap, coutouverture)
        (posy, posx) = (len(y), len(x))
    
    elif mode == "local" :

        initLocal(x, y, B)
        fillLocal(x, y, A, B, g, S, gap, coutouverture)
        posy = 0 
        posx = 0
        max = 0
        for v in range(len(x)+1) :

            for w in range(len(y)+1) :

                if A[w, v] > max :
                    max = A[w, v]
                    posy = w
                    posx = v
    
    elif mode == "semiglobal" :

        initLocal(x, y, B)
        fillGlobal(x, y, A, B, g, S, gap, coutouverture)
        py = 0
        posx = len(x)
        max = 0

        for v in range (len(y) + 1) :

            if A[v, posx] > max :

                max = A[v, posx]
                posy= v
            
    score = A[posy, posx]
    (sequencexalignee, sequenceyalignee) = backtrack(x, y, A, B, (posy, posx), mode)
    
    return(score, sequencexalignee, sequenceyalignee)




if __name__ == "__main__":
    def MSimilarite(a, b):
        return a == b
