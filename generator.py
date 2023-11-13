import random
import math

pressure_list = ["torr", "mm Hg", "kPa", "Pa", "psi", "atm"]
pressure_dict = {"torr":760, "mm Hg":760, "kPa": 101.325, "Pa": 101325, "psi": 14.7, "atm": 1}
volume_list = ["cubic meters", "cubic centimeters", "milliliters", "liters"]
volume_dict = {"cubic meters":0.001, "cubic centimeters": 1000, "milliliters": 1000, "liters":1}
sodas = ["Sprite", "Coca-Cola", "Cream Soda", "Pepsi", "7 Up", "Mountain Dew", "Ginger Ale"]

out_string = ""

number = int(input("Enter desired number generated: "))
type_generated = int(input("Enter type to generate (1-4): "))

if type_generated == 1:
    for i in range(number):
        out_string += "You found a hot air balloon and need to use the gas canister to take off. Each balloon has a specific volume of gas needed for flight. Too little gas will not let you take off and too much will pop the balloon, and each gas canister has a specific amount of gas in a volume Vi, at pressure Pi. You need to pick which gas canister to use so when released into the balloon at atmospheric pressure Pf(1 atm), its volume will not exceed the maximum for the balloon but will be enough for takeoff.\n\n"

        vol = random.randint(200, 1500)
        interval = random.randint(3, 15)/100
        min_vol = vol * (1-interval)
        max_vol = vol * (1+interval)
        good_volume = random.randint(5, 500) / 10
        good_pressure = vol/good_volume
        volumes = []
        pressures = []
        for j in range(3):
            error = interval * random.randint(2, 7)
            error_vol = vol + ((vol * error) * (-1)**random.randint(1,2))
            can_volume = random.randint(5, 500) / 10
            error_pressure = error_vol/can_volume
            volumes.append(error_vol)
            pressures.append(error_pressure)
        # print(f"Volumes: {volumes} and Pressures: {pressures}")

        correct = random.randint(0,3)
        correct_num = correct + 1
        volumes.insert(correct, good_volume)
        pressures.insert(correct, good_pressure)

        out_string += f"Problem:\nBalloon Max Volume: {round(max_vol)} liters\nBalloon Minimum Volume: {round(min_vol)} liters\n\nGas Canisters to Choose From:\n"
        for j in range(4):
            temp_pressure = random.choice(pressure_list)
            temp_volume = random.choice(volume_list)

            out_string += f"{j+1}: {round(volumes[j] * volume_dict[temp_volume], 3)} {temp_volume} at {round((pressures[j] * pressure_dict[temp_pressure]), 1)}{temp_pressure}\n"
        out_string += f"Answer Code: {(correct_num * 5 * round(int(vol)/10))}\n"

elif type_generated == 2:

    for i in range(number):
        out_string += "You begin the race in a submarine, but need to swim to the surface which will take around 10 minutes. To safely do this dive you need to connect an air canister to your scuba gear, that will allow you to have 200 ml of oxygen at a pressure of 1 atm. Choose the canister that will allow you to safely race to the surface. Assume the temperature is constant.\n\n"
        vol_initial = random.randint(5, 50)/100
        vol_final = 0.2
        p_initial = .2/vol_initial
        p_final = 1
        volumes = []
        pressures = []
        for j in range(3):
            error_pressure_final = random.randint(5,50)/10
            can_volume = random.randint(15, 50)/100
            while abs(vol_initial - can_volume) < .08: can_volume = random.randint(1, 50)/100

            error_pressure_initial = error_pressure_final/can_volume
            volumes.append(can_volume)
            pressures.append(error_pressure_initial)
        
        correct = random.randint(0,3)
        correct_num = correct + 1
        volumes.insert(correct, vol_initial)
        pressures.insert(correct, p_initial)

        out_string += f"Problem:\nTank Final Volume: {(200)} milliliters\nTank Final Pressure: {1}atm\n\nOxygen Tanks to Choose From:\n"
        for j in range(4):
            temp_pressure = random.choice(pressure_list)
            temp_volume = random.choice(volume_list)

            out_string += f"{j+1}: {round(volumes[j] * volume_dict[temp_volume], 6)} {temp_volume} at {round((pressures[j] * pressure_dict[temp_pressure]), 3)}{temp_pressure}\n"
        out_string += f"Answer Code: {round(math.cos((math.pi/correct_num)), 3)}\n"
elif type_generated == 3:
    for i in range(number):
        out_string += "In order to successfully finish the race you must bring a refreshing drink to T. Rose who is waiting at the finish line. You must choose from a selection of sodas to take with you along the rest of the journey. Based on knowing the volume of each drink at the finish line and the initial volume and pressure of each drink, choose the soda that will have the smallest chance of erupting when T. Rose opens it at the finish line.\n\n"
        vol_initial = random.randint(40, 500)/1000
        vol_final = 0.355
        p_final = 0.4
        p_initial = (p_final*vol_final)/vol_initial
        volumes = []
        pressures = []
        for j in range(3):
            error_pressure_final = random.randint(5,50)/10
            can_volume = random.randint(40, 500)/1000
            while abs(vol_initial - can_volume) < .05: can_volume = random.randint(40, 500)/1000

            error_pressure_initial = error_pressure_final/can_volume
            volumes.append(can_volume)
            pressures.append(error_pressure_initial)
        
        correct = random.randint(0,3)
        correct_num = correct + 1
        volumes.insert(correct, vol_initial)
        pressures.insert(correct, p_initial)

        out_string += f"Problem:\nSoda Final Volume: 355ml\n\nSodas to Choose From:\n"
        sodasList = random.sample(sodas, 4)
        for j in range(4):
            temp_pressure = random.choice(pressure_list)
            temp_volume = random.choice(volume_list)

            
            
            
            out_string += f"{sodasList[j]}: {round(volumes[j] * volume_dict[temp_volume], 6)} {temp_volume} at {round((pressures[j] * pressure_dict[temp_pressure]), 3)}{temp_pressure}\n"
        out_string += f"Answer Code: {round(math.sin((math.pi/correct_num)), 3)}\n"



open(f"output{type_generated}.txt", mode='w').write(out_string)

