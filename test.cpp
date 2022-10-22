Fastmap(O, d, m): 
	for i = 1 to m 
		A, B := SelectLine(O, d) 
		for each C in O 
			if C == A :				
        x_{C, i} := 0 
			elif C == B : 
				x_{C, i} := distance(A, B, i) else: 
			x_{C, i} := (dist(A, C, i)^2+ dist(A, B, i)^2- dist(B, C, i)^2)/2* dist(A, B, i) 
	return x 

dist(A, B, i): 
	if i ==1: 
		return d_{AB} 
	else : 
		return sqrt(dist(A, B, i-1)^2 - (x_{A, i-1}-x_{B, i-1})^2) 

SelectLine(O, d):
	B := RandomPoint(O) 
  max_dist := 0
  for each C in O :
		if d_{BC} > max_dist			
      A := C 
      max_dist := d_{BC} 
	max_dist := 0 
	for each C in O 
		if d_{AC} > max_dist			
      B := C 
      max_dist := d_{AC} 
	return A, B 