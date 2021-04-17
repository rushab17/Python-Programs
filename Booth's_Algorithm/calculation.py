# Problem Statement: Write a program to display the operations carried out in the process of
# multiplication of signed numbers using the Booth's Algorithm.

# Booth's Algorithm:
# Registers -
# Multiplicand : BR
# Multiplier : QR
# Accumulator : AC -> 0
# Serial Counter : SC -> Number of bits of QR
# Extra Bit : Qn+1 -> 0

# Explanation of Booth's Algorithm: https://www.geeksforgeeks.org/computer-organization-booths-algorithm/
#Refer the site for detailed explanation of the working.

#Solution: Provide a dedicated code design to display a table in command-line interface.

def Twos_compliment(value):
	'''
	This function calculate the 2's compliments of the binary number
	Input: Binary number
	Output: 2nd compliment of the number
	'''
	# To perform 1's compliment
	# by changin 0 to 1
	value = value.replace('0','x')
	value = value.replace('1','0')
	value = value.replace('x','1')

	# Two compliment by adding 1 to the last bit
	temp = ""
	for i in range(len(value)-1,-1,-1):
		if (value[i]=='1'):
			temp = temp + "0"
		else:
			temp = value[0:i] + "1" + temp
			break;
	return temp

def initial_values(BR,QR):
	'''
This function performs intilization steps like
1. padding 0 to multiplicand or multiplier to make the length of two binary number equal
2. Initialize Accumulator (AC) with binary number equivalent to integer 0, but having bit length equal to QR
3. Initialize Serial Counter (SC) to number of bits in QR.
4. Initialize Qn+1 bit to 0

Input: BR and QR
Output: converted BR and QR, initialized AR,SC,Qn+1
	'''

	diff = len(BR)-len(QR)
	if (diff>0):
		QR = '0' * diff + QR
	else:
		BR = '0' * abs(diff) + BR

	AC = '0' * len(QR)
	SC = len(QR)
	Qn_plus1 = '0'
	return (BR,QR,AC,SC,Qn_plus1)

def Arithmetic_shift_right(AC,QR,Qn_plus1):
	'''
This function performs the Arithmetic Shift Right operation
Input: AC,QR,Qn+1
Output: Shifted AC,QR,Qn+1
	'''

	# Qn+1 becomes the last bit of QR
	Qn_plus1 = QR[-1]

	# Right Shift each bit of QR with
	# First bit as the last bit of AC
	QR = AC[-1] + QR[0:-1]

	# First bit of AC is placed as it is
	# and then right shift is peformed
	AC = AC[0] + AC[0:-1]

	return AC,QR,Qn_plus1

def Add_BR(AC,BR):
	'''
This function perform additon on AC with BR or 2's compliment of BR
Input: AC and BR
Output: Updated AC
	'''

	carry = 0
	for i in range(len(AC)-1,-1,-1):

		# If the bit of AC and BR is (0,1) or (1,0) and carry = 0
		#then answer is 1 and carry=0
		if (AC[i]!=BR[i] and carry==0):
			AC = AC[0:i] + '1' + AC[i+1:]

		# If the bit of AC and BR is (0,1) or (1,0) and carry = 1
		#then answer is 0 and carry=1
		elif(AC[i]!=BR[i] and carry==1):
			AC = AC[0:i] + '0' + AC[i+1:]

		else:
			
			# If the bit of AC and BR is (1,1) and carry = 1
			#then answer is 1 and carry=1
			if(AC[i]=='1' and carry==1):
				AC = AC[0:i] + '1' + AC[i+1:]

			# If the bit of AC and BR is (1,1) and carry = 0
			#then answer is 0 and carry=1
			elif(AC[i]=='1' and carry==0):
				AC = AC[0:i] + '0' + AC[i+1:]
				carry = 1

			# If the bit of AC and BR is (0,0) and carry = 1
			#then answer is 1 and carry=0
			elif(AC[i]=='0' and carry==1):
				AC = AC[0:i] + '1' + AC[i+1:]
				carry = 0
	return (AC)

#----------Start of the code--------------

# Take Input of two numbers
a,b = list(map(int,input("Enter two numbers with space between: ").split()))
negative = False;

# Convert the first number to its binary quivalent and Two's compliment
# Using in-built bin() function

# If the number is negative than the bin function assign a negative sign
# and a 0 at the start, so lets remove that
# If the number is postitve than the bin function assign
# a 0 at the start, so lets remove that
  
if(a>=0):
	BR = bin(a).removeprefix("0b")
	BR = '0' + BR
	BR1 = Twos_compliment(BR)
else:
	negative = True;
	BR1 = bin(a).removeprefix("-0b")
	BR1 = '0' + BR1 
	BR = Twos_compliment(BR1)

# Convert the second number to its binary
# and remove the extra 0 or -0
if(b>=0):
	QR = bin(b).removeprefix("0b")
	QR = '0' + QR	
	QR_2 = (QR + '.')[:-1]
else:
	negative = not negative;
	temp = bin(b).removeprefix("-0b")
	temp = '0' + temp
	QR = Twos_compliment(temp)
	QR_2 = (QR + '.')[:-1]

# Perform a one time initilization to get all neccessary values
BR,QR,AC,SC,Qn_plus1 = initial_values(BR,QR)

# cmd_GUI is another program file provides in this repositiory
# that helps to design a desired GUI template for cmd
import cmd_GUI

# Step number
Stage = 0

# Get the initial lines for display
cmd_GUI.initial_lines(Stage,BR,AC,QR,Qn_plus1,SC)

# Iter through Serial Counter till it becomes 0
for iter in range(SC,0,-1):
	Stage+=1

	# If the last bit of QR and Qn+1 bit are (0,1)
	# perform addition of BR to AC
	if (QR[-1]!=Qn_plus1 and QR[-1]=='0'):
		AC = Add_BR(AC,BR)
		Case = 2

		# Diplay appropriate rows and columns as per the case
		cmd_GUI.display_line1(Stage,Case,AC,QR,Qn_plus1)

	# If the last bit of QR and Qn+1 bit are (1,0)
	# perform addition of 2's comp of BR to AC 
	elif (QR[-1]!=Qn_plus1 and QR[-1]=='1'):
		AC = Add_BR(AC,BR1)
		Case = 3

		# Diplay appropriate rows and columns as per the case
		cmd_GUI.display_line1(Stage,Case,AC,QR,Qn_plus1)
	
	else:
		Case = 1

		# Diplay appropriate rows and columns as per the case
		cmd_GUI.display_line1(Stage,Case,AC,QR,Qn_plus1)

	# At the end of each step we perform Arithmetic Shift Right
	AC,QR,Qn_plus1=Arithmetic_shift_right(AC,QR,Qn_plus1)

	# Display the result after the operation
	cmd_GUI.display_line2(AC,QR,Qn_plus1,iter)

# If the number is negative then perform the 2's compliment to get actual value
# recursive removal of 0 from the starting bits in Accumulator irrespecitve of postive or negative
if (negative):
	length = len(AC)
	Temp = Twos_compliment(AC+QR)
	AC,QR = Temp[0:length],Temp[length:]
	print ("\nTwo's compliment of result: {}{} \n(since the answer is negative)".format(AC,QR))
while(True):
	if(AC and AC[0]=='0'):
		AC = AC[1:]
	else:
		break

# Display the final result
cmd_GUI.final_result(a,b,BR,AC,QR,QR_2,negative)