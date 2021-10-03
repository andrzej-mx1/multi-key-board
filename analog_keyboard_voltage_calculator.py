import argparse
import sys

int_resistors_values = []
float_voltage_divider_output = []



#sys.argv = ["analog_keyboard_voltage_calcultor.py", '--file=resistors.txt', '--VCC=5']
int_resistor=0
int_n=0
int_resistor_value = []

#
# Configure args parser
#
parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, default='resistors.txt', help='Filename wiht resistors values.')
parser.add_argument('--VCC', type=float, choices=range(0,255), default=5, help='Value of Vcc.')
args = parser.parse_args()
print(args)

float_Vcc=args.VCC

#
# Open file and read resistors values from it.
#
with open(args.file) as f:
    for read_line in f:
        i=int(read_line)
        int_resistors_values.append(i)

print(int_resistors_values)

#
# Calculate voltage values.
#
float_nominator = 0;
float_denominator = 0;
for i in range(0, len(int_resistors_values)):
        float_denominator += int_resistors_values[i]
        float_voltage_divider_output.append(float((float_nominator/float_denominator)*float_Vcc))
        if i<(len(int_resistors_values)-1):
            float_nominator += int_resistors_values[i+1]

print(float_voltage_divider_output)


