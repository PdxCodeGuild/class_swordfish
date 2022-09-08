meters = {                                      # Created a dictionary of all the different meter conversions.
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yard': 0.9144,
    'in': 0.0254
}

distance = float(input('Please input desired distance: ')) # Request input from user for distance and converted to a float.

in_unit = input('Please enter unit you wish to start with: ') # Requests user to input unit they want to start with.
input_unit = meters[in_unit]                    # Pulls the value from the unit inputed.

out_unit = input('Please enter desired output unit: ')  # Requests the output unit they wish to end with.

m_conversion = distance * input_unit            # Does the conversion math to meter.

if out_unit == 'ft':                            # Conversion output to feet.
    conversion = m_conversion / meters['ft']

elif out_unit == 'mi':                          # Conversion output to miles.
    conversion = m_conversion / meters['mi']

elif out_unit == 'm':                           # Conversion output to meters.
    conversion = m_conversion / meters['m']

elif out_unit == 'km':                          # Conversion output to kilometers.
    conversion = m_conversion / meters['km']

elif out_unit == 'yard':                        # Conversion output to yards.
    conversion = m_conversion / meters['yard']

elif out_unit == 'in':                        # Conversion output to inches.
    conversion = m_conversion / meters['in']

print(conversion)                               # Print out the converted number.