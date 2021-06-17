pyramid = [[95,64],[17,47,82],[18,35,87,10],[20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41,26, 56, 83, 40, 80, 70, 33],[41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

cur = 3
record = 0


for a in range(2):
	#cur += pyramid[0][i]
	for b in range(a, a+2):
		#cur += pyramid[1][z]
		for c in range(b, b+2):
			for d in range(c,c+2):
				for e in range(d,d+2):
					for f in range(e, e+2):
						for g in range(f,f+2):
							for h in range(g,g+2):
								for i in range(h,h+2):
									for j in range(i,i+2):
										for k in range(j,j+2):
											for l in range(k,k+2):
												for m in range(l,l+2):
													for n in range(m,m+2):

														cur = 75+pyramid[0][a] + pyramid[1][b] + pyramid[2][c]+ pyramid[3][d]+ pyramid[4][e]+ pyramid[5][f]+ pyramid[6][g]+ pyramid[7][h]+ pyramid[8][i]+ pyramid[9][j]+ pyramid[10][k]+ pyramid[11][l]+ pyramid[12][m]+ pyramid[13][n]
														if (cur > record):
															record = cur
			#cur += pyramid[2][p]
			
			
			
print(record)

















		



