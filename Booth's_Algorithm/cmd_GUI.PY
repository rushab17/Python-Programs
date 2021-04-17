def initial_lines(Iter,BR,AC,QR,Qn_plus1,SC):
	'''
This function prints Initial Lines such as 
Heading: Booth Algorithm
Column Heading
Stage 0 Row
Input: Iteration value,BR,AC,QR and Qn+1
	'''

	print ("Muliplicand:",BR,"\nMultiplier:",QR)
	print ("\n<---------------------------Booth's Algorithm--------------------------->")
	print ("Stage\t \t AC \t \t QR \t \t Qn+1 \t SC")
	print ("\t\t Accumulator \t Multiplier \t \t Serial Counter\n")
	print ("Stage",Iter,"\t",AC,"\t\t",QR,"\t\t",Qn_plus1,"\t",SC)
	print ("-------------------------------------------------------------------------")

def display_line1(Iter,Case,AC,QR,Qn_plus1):
	'''
This function prints elements in row like
all stages and descrition of case like addition or Right-SHift
Input: Iteration value,Case,AC,QR and Qn+1
	'''

	print("Stage",Iter)
	print (QR[-1],"-->",Qn_plus1)
	if Case==1:
		Temp = 'No Addition'
		print (Temp)
	elif Case==2:
		Temp = 'Add BA'
		print (Temp,"\t\t",AC,"\t\t",QR,"\t\t",Qn_plus1)
	elif Case==3:
		Temp = 'Add BA\''
		print (Temp,"\t",AC,"\t\t",QR,"\t\t",Qn_plus1)

def display_line2(AC,QR,Qn_plus1,SC):
	'''
This function prints values in row
Input: AC,QR,Qn+1 and SC

	'''
	print ("\t\t",AC,"\t\t",QR,"\t\t",Qn_plus1,"\t",SC)
	print ("-------------------------------------------------------------------------")
	if (SC==1):
		print ("End\t\t",AC,"\t\t",QR,"\t\t",Qn_plus1,"\t",SC-1)	

def final_result(a,b,BR,AC,QR,QR_2,negative):
	'''
This function prints final result
Input: Original numbers(a,b), AC,BR,QR,original QR (QR_2) and negative flag
	'''
	if (negative):
		print ("\nFinal Result: -(",AC+QR,")")
		print ("Hence, {} X {} = -( {} )".format(BR,QR_2,AC+QR))
		print ("i.e",a,"X",b,"=",int("-0b"+AC+QR,2))
	else:
		print ("\nFinal Result:",AC+QR)
		print ("Hence,",BR,"X",QR_2,"=",AC+QR)
		print ("i.e",a,"X",b,"=",int("0b"+AC+QR,2))