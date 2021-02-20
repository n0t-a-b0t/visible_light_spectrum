from scipy import constants
from tabulate import tabulate

vis_spectrum = [['Color', 'Wavelength (nm) (vacuum)'], ['Ultraviolet', '<380'], ['Violet', '380-450'],
                ['Blue', '450-485'], ['Cyan', '485-500'], ['Green', '500-565'], ['Yellow', '565-590'],
                ['Orange', '590-625'], ['Red', '625-700'], ['Infrared', '700<']]

si_prefix = [['Prefix', 'Index'], ['yotta', 24], ['zetta', 21], ['exa', 18], ['peta', 15], ['tera', 12], ['giga', 9],
             ['mega', 6], ['kilo', 3], ['hecto', 2], ['deca', 1], ['one', 0], ['deci', -1], ['centi', -2],
             ['milli', -3], ['micro', -6], ['nano', -9], ['pico', -12], ['femto', -15], ['atto', -18], ['zepto', -21],
             ['yocto', -24]]

refractive_index = [['Material', 'Value'], ['Vacuum', '1'], ['Air (STP)', '1.000273'],
                    ['Air (0 Celsius, 1 atm)', '1.000293'], ['Carbon dioxide (0 Celsius, 1 atm)', '1.001'],
                    ['Helium (0 Celsius, 1 atm)', '1.000036'], ['Hydrogen (0 Celsius, 1 atm)', '1.000132'],
                    ['Arsenic trisulfide and sulfur in methylene iodide (Liquid -- 20 Celsius)', '1.9'],
                    ['Carbon disulfide (Liquid -- 20 Celsius)', '1.628'], ['Benzene (Liquid -- 20 Celsius)', '1.501'],
                    ['Carbon tetrachloride (Liquid -- 20 Celsius)', '1.161'],
                    ['Silicone oil (nD25) (Liquid -- 20 Celsius)', '1.393-1.403'],
                    ['Kerosene (Liquid -- 20 Celsius)', '1.39'],
                    ['Ethanol (ethyl alcohol) (Liquid -- 20 Celsius)', '1.361'],
                    ['Acetone (Liquid -- 20 Celsius)', '1.36'], ['Water (Liquid -- 20 Celsius)', '1.333'],
                    ['10% Glucose solution in water (Liquid -- 20 Celsius)', '1.3477'],
                    ['20% Glucose solution in water (Liquid -- 20 Celsius)', '1.3635'],
                    ['60% Glucose solution in water (Liquid -- 20 Celsius)', '1.4394'],
                    ['Silicon carbide (Moissanite; 6H form) -- Room Temperature (RT)', '2.65'],
                    ['Titanium dioxide (rutile phase) -- RT', '2.614'], ['Diamond -- RT', '2.417'],
                    ['Strontium titanate -- RT', '2.41'], ['Tantalum Pentoxide -- RT', '2.15'], ['Amber -- RT', '1.55'],
                    ['Sodium chloride -- RT', '1.544'],
                    ['Fused silica (a pure form of glass, also called fused quartz) -- RT', '1.458'],
                    ['Liquid helium', '1.025'], ['Perfluorohexane (Fluorinert FC-72)', '1.251'], ['Water ice', '1.31'],
                    ['TFE/PDD (Teflon AF)', '1.315'], ['Cryolite', '1.338'], ['Cytop', '1.34'],
                    ['Polytetrafluoroethylene (Teflon)', '1.35-1.38'], ['Sugar solution, 25%', '1.3723'],
                    ['Cornea (human)', '1.373/1.380/1.401'], ['Lens (human)', '1.386–1.406'],
                    ['Liver (human)', '1.369'], ['Intestinal mucosa (human)', '1.329-1.338'],
                    ['Ethylene tetrafluoroethylene (ETFE)', '1.403'], ['Sylgard 184 (polydimethylsiloxane)', '1.4118'],
                    ['Sugar solution, 50%', '1.42'], ['Polylactic acid', '1.46'],
                    ['Pyrex (a borosilicate glass)', '1.47'], ['Vegetable oil', '1.47'], ['Glycerol', '1.4729'],
                    ['Sugar solution, 75%', '1.4774'], ['Poly(methyl methacrylate) (PMMA)', '1.4893–1.4899'],
                    ['Halite (rock salt)', '1.516'], ['Plate Glass (window glass)', '1.52'],
                    ['Crown glass (pure)', '1.50–1.54'], ['PETg', '1.57'],
                    ['Polyethylene terephthalate (PET)', '1.575'], ['Polycarbonate', '1.6'],
                    ['Crown glass (impure)', '1.485–1.755'], ['Flint glass (pure)', '1.60-1.62'], ['Bromine', '1.661'],
                    ['Flint glass (impure)', '1.523–1.925'], ['Sapphire', '1.762–1.778'], ['Boron nitride', '2-2.14'],
                    ['Cubic zirconia', '2.15-2.18'], ['Potassium niobate (KNbO3)', '2.28'], ['Zinc oxide', '2.4'],
                    ['Cinnabar (mercury sulfide)', '3.02'], ['Silicon', '3.42–3.48'], ['Gallium(III) phosphide', '3.5'],
                    ['allium(III) arsenide', '3.927'], ['Germanium', '4.05-4.01'], ['Glass (Common Value)', '1.5']]


def cw():
    print(tabulate(vis_spectrum))
    return


def scale():
    print(tabulate(si_prefix))
    return


def ri():
    print(tabulate(refractive_index))
    return


def calculator():
    global E, n, w
    opt1 = input("What do you want to calculate: c, w, f, E, n or speed or wavelength in different medium?: ")
    if opt1 == 'c':
        print("For any unknowns, enter any letter\n")
        try:
            n = float(input("Refractive index: "))
        except ValueError:
            n = 'x'
        if n != 'x':
            cv = constants.c/n
            print("Speed of light in given medium: ", cv, " m/s")
        elif n == 'x':
            try:
                w = float(input("Wavelength (m): "))
            except ValueError:
                print("Too many unknowns")
                return
            try:
                f = float(input("Frequency (Hz): "))
            except ValueError:
                f = 'x'
            if f != 'x':
                cv = w*f
                print("Speed of light in given medium: ", cv, " m/s")
            elif f == 'x':
                try:
                    E = float(input("Enter energy of photon: "))
                except ValueError:
                    print("Too many unknowns")
                r = input("Is energy in electron volts?[y/n]: ")
                if r == 'y':
                    cv = (w*E*constants.electron_volt)/constants.Planck
                    print("Speed of light in given medium: ", cv, " m/s")
                elif r == 'n':
                    cv = (w*E)/constants.Planck
                    print("Speed of light in given medium: ", cv, " m/s")
                else:
                    print("Please select y or n only!!!")
    elif opt1 == 'w':
        print("For any unknowns, enter any letter\n")
        try:
            cv = float(input("Speed of Light in given medium (m/s): "))
        except ValueError:
            cv = 'x'
        if cv == 'x':
            try:
                n = float(input("Refractive index: "))
            except ValueError:
                print("Too many unknowns")
            cv = constants.c/n
            try:
                f = float(input("Enter frequency (Hz): "))
            except ValueError:
                f = 'x'
            if f != 'x':
                w = cv/f
                print("Wavelength of the photon in given medium: ", w, " m")
            elif f == 'x':
                try:
                    E = float(input("Enter energy of photon: "))
                except ValueError:
                    print("Too many unknowns")
                r = input("Is Energy in electron volts?[y/n]: ")
                if r == 'y':
                    w = (cv*constants.Planck)/(E*constants.electron_volt)
                    print("Wavelength of photon in given medium: ", w, " m")
                if r == 'n':
                    w = (cv*constants.Planck)/E
                    print("Wavelength of photon in given medium: ", w, " m")
        if cv != 'x':
            try:
                f = float(input("Enter frequency (Hz): "))
            except ValueError:
                f = 'x'
            if f != 'x':
                w = cv/f
                print("Wavelength of the photon in given medium: ", w, " m")
            elif f == 'x':
                try:
                    E = float(input("Enter energy of photon: "))
                except ValueError:
                    print("Too many unknowns")
                r = input("Is Energy in electron volts?[y/n]: ")
                if r == 'y':
                    w = (cv*constants.Planck)/(E*constants.electron_volt)
                    print("Wavelength of photon in given medium: ", w, " m")
                if r == 'n':
                    w = (cv*constants.Planck)/E
                    print("Wavelength of photon in given medium: ", w, " m")
    elif opt1 == 'f':
        print("For any unknowns, enter any letter\n")
        try:
            E = float(input("Enter energy of photon: "))
        except ValueError:
            E = 'x'
        if E != 'x':
            r = input("Is energy in electron volt?[y/n]: ")
            if r == 'y':
                f = (E*constants.electron_volt)/constants.Planck
                print("Frequency of given wave is: ", f, " Hz")
            elif r == 'n':
                f = E/constants.Planck
                print("Frequency of given wave is: ", f, " Hz")
            else:
                print("Enter only y or n please!!!")
        if E == 'x':
            try:
                w = float(input("Enter wavelength in given medium (m): "))
            except ValueError:
                print("Too many unknowns")
            try:
                cv = float(input("Enter speed of light in given medium (m/s): "))
                f = cv/w
                print("Frequency of given wave is: ", f, " Hz")
            except ValueError:
                try:
                    n = float(input("Enter refractive index: "))
                except ValueError:
                    print("Too many unknowns")
                cv = constants.c/n
                f = cv/w
                print("Frequency of given wave is: ", f, " Hz")
    elif opt1 == 'E':
        try:
            f = float(input("Enter frequency of wave (Hz): "))
            E = constants.Planck*f
            EeV = (constants.Planck*f)/constants.electron_volt
            print("Energy of photon: ", E, " J")
            print("Energy of photon in electron volts: ", EeV, " eV")
        except ValueError:
            try:
                w = float(input("Wavelength in given medium (m): "))
                try:
                    cv = float(input("Speed of light in medium (m/s): "))
                    E = (constants.Planck * cv)/w
                    EeV = (constants.Planck * cv) / (constants.electron_volt * w)
                    print("Energy of photon: ", E, " J")
                    print("Energy of photon in electron volts: ", EeV, " eV")
                except ValueError:
                    try:
                        n = float(input("Refractive index: "))
                        cv = constants.c/n
                        cv = float(input("Speed of light in medium (m/s): "))
                        E = (constants.Planck * cv) / w
                        EeV = (constants.Planck * cv) / (constants.electron_volt * w)
                        print("Energy of photon: ", E, " J")
                        print("Energy of photon in electron volts: ", EeV, " eV")
                    except ValueError:
                        print("Too many unknowns")
            except ValueError:
                print("Too many unknowns")
    elif opt1 == 'n':
        x1 = float("Enter speed or wavelength of wave in medium 1: ")
        try:
            x2 = float("Enter speed or wavelength of wave in medium 2 (Enter 'x' if unknown): ")
            n = x1/x2
            print("Refractive index of wave is: ", n)
        except ValueError:
            try:
                n = float(input("Refractive index: "))
                x2 = x1/n
                print("Speed or Wavelength value in medium 2 for this wave is: ", x2)
            except ValueError:
                print("Too many unknowns")
    else:
        print("Incorrect option!!!")
    return


def wvcmatch():
    w = float(input("Enter wavelength in nanometers: "))
    print("Calculations based on c=3*(10**8) m/s\n")
    if w <= 380:
        print("Ultraviolet range")
    elif 380 < w <= 450:
        print("Violet")
    elif 450 < w <= 485:
        print("Blue")
    elif 380 < w <= 450:
        print("Violet")
    elif 485 < w <= 500:
        print("Cyan")
    elif 500 < w <= 565:
        print("Green")
    elif 565 < w <= 590:
        print("Yellow")
    elif 590 < w <= 625:
        print("Orange")
    elif 625 < w <= 700:
        print("Red")
    elif 700 < w:
        print("Infrared Range")
    f = constants.c/w
    print("Frequency: ", f, " Hz")
    E = constants.Planck*f
    EeV = (constants.Planck*f)/constants.electron_volt
    print("Energy (E): ", E, " J")
    print("Energy in electron volts: ", EeV, " eV")
    return


def main():
    while 1:
        print("\n\n\n1: Color-Wavelength Chart\n2: Scale/Metrics\n3: List of Refractive indices\n4: Calculator\n5: Wavelength to Color Match\n")
        opt = int(input("Enter choice: "))
        if opt == 1:
            cw()
        elif opt == 2:
            scale()
        elif opt == 3:
            ri()
        elif opt == 4:
            calculator()
        elif opt == 5:
            wvcmatch()
    return


main()
