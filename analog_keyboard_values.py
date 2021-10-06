import argparse
import sys

int_ADC_readings = []
int_ADC_boundaries = []
int_ADC_ranges = []
int_ADC_max_reading = 1024
int_resistors_values = []
float_voltage_values = []
float_voltage_divider_output = []

#
# Configure args parser
#
parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, default='resistors.txt', help='Filename wiht resistors values.')
parser.add_argument('--VCC', type=float, choices=range(0,255), default=5, help='Value of Vcc.')
args = parser.parse_args()

float_Vcc=args.VCC

#
# Open file and read resistors values from it. 
#
with open(args.file) as f:
    for read_line in f:
        i=int(read_line)
        int_resistors_values.append(i)

#
# Calculate voltage values. 
#
float_nominator = 0;
float_denominator = 0;
for i in range(0, len(int_resistors_values)):
        float_denominator += int_resistors_values[i]
        float_voltage_values.append(float((float_nominator/float_denominator)*float_Vcc))
        if i<(len(int_resistors_values)-1):
            float_nominator += int_resistors_values[i+1]
#
# Calculates ADC readings 
#
for float_voltage in float_voltage_values:
  x =  int(int_ADC_max_reading*float_voltage/5+0.5)
  int_ADC_readings.append(x)


#
# Calculate ADC readings ranges boundary 
#
int_ADC_boundaries.append(0);
for index in range(0,len(int_ADC_readings)-1): 
  x =int((int_ADC_readings[index]+int_ADC_readings[index+1])/2+0.5)
  int_ADC_boundaries.append(x)

int_ADC_boundaries.append(int_ADC_max_reading);


#
# Build table of ranges
#
for index in range(0,len(int_ADC_boundaries)-1):
  int_ADC_one_range = []
  l = int_ADC_boundaries[index]
  h = int_ADC_boundaries[index+1]
  int_ADC_one_range.append(l)
  int_ADC_one_range.append(h)
  int_ADC_ranges.append(int_ADC_one_range)
  


#
# Prints to the stdout table with ADC reading ranges, in C/C++ syntax.
#
i=0
str_output = "{"
for range in int_ADC_ranges:
    str_output += "{"
    str_output += str(range[0])
    str_output += ","
    str_output += str(range[1])
    str_output += "}"
    i=i+1
    if i <len(int_ADC_ranges):
        str_output += ","
str_output += "}"

print(str_output)


