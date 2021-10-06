import argparse
import sys

sys.argv = ["analog_keyboard_resistor_calcultor.py", '--Resistor=1500', '--n=11']
int_resistor=0
int_n=0
int_resistors_values = []

#
# Configure Args Parser
#
parser = argparse.ArgumentParser()
parser.add_argument('--Resistor', type=int, choices=range(1,10000), default=1500, help='Resistor R value in Ohms')
parser.add_argument('--n', type=int, choices=range(2,101), default=3, help='Number of the keys.')
args = parser.parse_args()


int_resistor=args.Resistor
int_n = args.n

#
# Calculates resistors values
#
for index in range(1,int_n+1):
    int_resistors_values.append(int(((int_n+1)*int_resistor)/((int_n-index+2)*(int_n-index+1))+0.5))

#
# Prints calcualted values to the stdout
#
print(int_resistor)
for str_line in int_resistors_values:
    print(str_line)
    


