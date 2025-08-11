# -*- coding: utf-8 -*-

# %% Definition of the inputs
"""
Input data definition
"""


from ramp.core.core import User

User_list = []

"""
This example input file represents an whole village-scale community,
adapted from the data used for the Journal publication. It should provide a
complete guidance to most of the possibilities ensured by RAMP for inputs definition,
including specific modular duty cycles and cooking cycles.
For examples related to "thermal loads", see the "input_file_2".
"""

# Create new user classes
HC = User(user_name="high consumption", num_users=17, user_preference=3)
User_list.append(HC)

ES = User("ES", 34, 3)
User_list.append(ES)

LC = User("low consumption", 119, 3)
User_list.append(LC)

HealthPost = User("health Post", 1)
User_list.append(HealthPost)

School = User("school", 1)
User_list.append(School)

# Create new appliances

# Church
#Ch_indoor_bulb = Church.add_appliance(
#    number=10,
#    power=26,
#    num_windows=1,
#    func_time=210,
#    time_fraction_random_variability=0.2,
#    func_cycle=60,
#    fixed="yes",
#    flat="yes",
#    name="indoor_bulb",
#)
#Ch_indoor_bulb.windows(window_1=[1200, 1440], window_2=[0, 0], random_var_w=0.1)

# High-Consumption
HC_indoor_bulb = HC.add_appliance(5, 7, 2, 300, 0.2, 120, name="indoor_bulb")
HC_indoor_bulb.windows([0, 480], [1080, 1440], 0.35)

HC_outdoor_bulb = HC.add_appliance(3, 14, 2, 180, 0.2, 60, name="outdoor_bulb")
HC_outdoor_bulb.windows([1080, 1440], [0, 60], 0.35)

HC_TV = HC.add_appliance(1, 30, 2, 120, 0.1, 5, name="TV")
HC_TV.windows([1082, 1440], [0, 60], 0.35)

HC_Radio = HC.add_appliance(1, 36, 2, 60, 0.1, 5, name="Radio")
HC_Radio.windows([390, 450], [1082, 1260], 0.35)

HC_Phone_charger = HC.add_appliance(4, 5, 2, 120, 0.2, 10, name="phone_charger")
HC_Phone_charger.windows([1020, 1440], [0, 300], 0.35)

HC_Laptop = HC.add_appliance(1,70,1,90,0.2,30,name="laptop")
HC_Laptop.windows([960,1200],[0,0],0.35)

HC_Blender = HC.add_appliance(1,350,2,20,0.1,5,occasional_use=0.33, name="blender")
HC_Blender.windows([420,480],[720,780],0.35)

HC_Iron = HC.add_appliance(1, 1000, 1, 5, 0.2, 1, occasional_use=0.33, name="iron")
HC_Iron.windows([360, 540], [0, 0], 0.35)

HC_Kettle = HC.add_appliance(1, 800, 2, 6, 0.2, 2, occasional_use=0.33, name="electric kettle")
HC_Kettle.windows([360, 540], [1080, 1200], 0.35)

HC_Freezer = HC.add_appliance(1, 350, 1, 1440, 0, 30, "yes", 3, name="freezer")
HC_Freezer.windows([0, 1440], [0, 0])
HC_Freezer.specific_cycle_1(200, 20, 5, 10)
HC_Freezer.specific_cycle_2(200, 15, 5, 15)
HC_Freezer.specific_cycle_3(200, 10, 5, 20)
HC_Freezer.cycle_behaviour(
    [480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440]
)


# ES
ES_indoor_bulb = ES.add_appliance(3, 7, 2, 300, 0.2, 120, name="indoor_bulb")
ES_indoor_bulb.windows([0, 480], [1080, 1440], 0.35)

ES_outdoor_bulb = ES.add_appliance(1, 14, 2, 180, 0.2, 60, name="outdoor_bulb")
ES_outdoor_bulb.windows([1080, 1440], [0, 60], 0.35)

ES_TV = ES.add_appliance(1, 30, 2, 120, 0.1, 5, name="TV")
ES_TV.windows([1082, 1440], [0, 60], 0.35)

ES_Radio = ES.add_appliance(1, 36, 2, 60, 0.1, 5, name="radio")
ES_Radio.windows([390, 450], [1082, 1260], 0.35)

ES_Laptop = ES.add_appliance(1,70,1,90,0.2,30,name="laptop")
ES_Laptop.windows([960,1200],[0,0],0.35)

ES_Phone_charger = ES.add_appliance(4, 5, 2, 120, 0.2, 10, name="phone_charger")
ES_Phone_charger.windows([1020, 1440], [0, 300], 0.35)

ES_Freezer = ES.add_appliance(1, 350, 1, 1440, 0, 30, "yes", 3, name="freezer")
ES_Freezer.windows([0, 1440], [0, 0])
ES_Freezer.specific_cycle_1(200, 20, 5, 10)
ES_Freezer.specific_cycle_2(200, 15, 5, 15)
ES_Freezer.specific_cycle_3(200, 10, 5, 20)
ES_Freezer.cycle_behaviour(
    [480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440]
)


# Low Consumption
LC_indoor_bulb = LC.add_appliance(3, 7, 2, 300, 0.2, 120, name="indoor_bulb")
LC_indoor_bulb.windows([0, 480], [1080, 1440], 0.35)

LC_outdoor_bulb = LC.add_appliance(1, 14, 2, 180, 0.2, 60, name="outdoor_bulb")
LC_outdoor_bulb.windows([1080, 1440], [0, 60], 0.35)

LC_TV = LC.add_appliance(1, 30, 2, 120, 0.1, 60, name="TV")
LC_TV.windows([360, 720], [1080, 1260], 0.35)

LC_Radio = LC.add_appliance(1, 36, 2, 60, 0.1, 5, name="Radio")
LC_Radio.windows([390, 450], [1082, 1260], 0.35)

LC_Phone_charger = LC.add_appliance(2, 5, 1, 180, 0.2, 60, name="phone_charger")
LC_Phone_charger.windows([720, 1440], [0, 0], 0.35)

# Hospital
HP_indoor_bulb = HealthPost.add_appliance(20, 7, 2, 690, 0.2, 10, name="indoor_bulb")
HP_indoor_bulb.windows([0, 720], [870, 1440], 0.35)

HP_outdoor_bulb = HealthPost.add_appliance(5, 13, 2, 240, 0.2, 10, name="outdoor_bulb")
HP_outdoor_bulb.windows([0, 342], [1037, 1440], 0.35)

HP_Phone_charger = HealthPost.add_appliance(5, 5, 2, 300, 0.2, 10, name="phone_charger")
HP_Phone_charger.windows([480, 720], [900, 1440], 0.35)

HP_TV = HealthPost.add_appliance(2, 60, 2, 360, 0.2, 30, name="TV")
HP_TV.windows([480, 720], [780, 1020], 0.35)

HP_Radio = HealthPost.add_appliance(2, 35, 2, 390, 0.2, 10, occasional_use=0.5,name="Radio")
HP_Radio.windows([480, 720], [780, 1020], 0.35)

HP_Freezer = HealthPost.add_appliance(3, 200, 1, 1440, 0.2, 30, "yes", 3, name="Freezer")
HP_Freezer.windows([0, 1440], [0, 0])
HP_Freezer.specific_cycle_1(150, 20, 5, 10)
HP_Freezer.specific_cycle_2(150, 15, 5, 15)
HP_Freezer.specific_cycle_3(150, 10, 5, 20)
HP_Freezer.cycle_behaviour(
    [580, 1200], [0, 0], [420, 579], [0, 0], [0, 419], [1201, 1440]
)

HP_Micro = HealthPost.add_appliance(1, 3, 2, 120, 0.2, 10, occasional_use=0.3,name="microscope")
HP_Micro.windows([480, 720], [840, 960], 0.35)

HP_serologicar = HealthPost.add_appliance(1, 10, 1, 60, 0.2, 15, occasional_use=0.3,name="serological rotator")
HP_serologicar.windows([480, 720], [0, 0], 0.35)

HP_centrifugue = HealthPost.add_appliance(1, 100, 1, 60, 0.2, 10, occasional_use=0.3,name="centrifugue")
HP_centrifugue.windows([480, 720], [0, 0], 0.35)

HP_dentalC = HealthPost.add_appliance(2, 500, 2, 60, 0.2, 10, occasional_use=0.5,name="dental compresor")
HP_dentalC.windows([480, 720], [840, 1260], 0.35)

HP_PC = HealthPost.add_appliance(2, 150, 2, 300, 0.2, 10, name="PC")
HP_PC.windows([480, 720], [1050, 1440], 0.35)

HP_Printer = HealthPost.add_appliance(1, 100, 1, 60, 0.2, 5, name="Printer")
HP_Printer.windows([540, 1020], [0, 0], 0.35)

HP_fan = HealthPost.add_appliance(5, 30, 1, 250, 0.2, 10, name="fan")
HP_fan.windows([500, 1200], [0, 0], 0.35)

HP_eheater = HealthPost.add_appliance(3, 800, 2, 250, 0.2, 10, name="electric heater")
HP_eheater.windows([480, 660], [1080, 1200], 0.35)

HP_sstove = HealthPost.add_appliance(2, 600, 2, 120, 0.2, 30, occasional_use=0.5,name="sterilizer stove")
HP_sstove.windows([480, 720], [780, 1020], 0.35)

HP_needled = HealthPost.add_appliance(1, 70, 1, 60, 0.2, 10, occasional_use=0.5,name="needle destroyer")
HP_needled.windows([480, 720], [0, 0], 0.35)

HP_pump = HealthPost.add_appliance(1, 400, 1, 45, 0.2, 10, name="water pump")
HP_pump.windows([480, 720], [0, 0], 0.35)

HP_eboiler = HealthPost.add_appliance(2, 600, 1, 15, 0.2, 3, name="electric boiler")
HP_eboiler.windows([420, 480], [660, 750], 0.35)

import pandas as pd
import numpy as np

shower_P = pd.read_csv("shower_P.csv")  # una columna
col = shower_P.columns[0]
shower_Pm = shower_P[col].astype(float).to_numpy()

# RAMP espera num_days=366 por defecto y, para potencias constantes, crea 367.
# Igualamos tamaño: 367
if len(shower_Pm) == 366:
    shower_Pm = np.r_[shower_Pm, shower_Pm[-1]]
elif len(shower_Pm) != 367:
    raise ValueError(f"La serie de potencia para ducha debe tener 366 o 367 valores; tiene {len(shower_Pm)}.")

HP_shower_P = pd.DataFrame({"P_shower": shower_Pm})

#HP_shower_P = pd.read_csv(r"C:\Users\KPEREZ\Downloads\shower_P.csv", header=None)
#HP_shower_power_list = HP_shower_P[0].tolist()
HP_shower = HealthPost.add_appliance(
    number=2,
    power=HP_shower_P,
    num_windows=2,
    func_time=20,
    time_fraction_random_variability=0.2,
    func_cycle=5,
    occasional_use=0.5,
    thermal_p_var=0.2,
    name="shower",
)
HP_shower.windows(window_1=[360, 540], window_2=[1080, 1260], random_var_w=0.35)

# School
S_indoor_bulb = School.add_appliance(27, 7, 1, 300, 0.2, 10, name="indoor_bulb")
S_indoor_bulb.windows([480, 840], [0, 0], 0.35)

S_outdoor_bulb = School.add_appliance(7, 13, 1, 60, 0.2, 10, name="outdoor_bulb")
S_outdoor_bulb.windows([480, 780], [0, 0], 0.35)

S_TV = School.add_appliance(5, 30, 1, 120, 0.2, 10, occasional_use=0.3, name="TV")
S_TV.windows([480, 780], [0, 0], 0.35)

S_fan = School.add_appliance(15, 30, 1, 120, 0.2, 10, occasional_use=0.3, name="fan")
S_fan.windows([480, 780], [0, 0], 0.35)

S_stereo = School.add_appliance(1, 150, 1, 90, 0.2, 5, occasional_use=0.3, name="stereo")
S_stereo.windows([480, 780], [0, 0], 0.35)

S_DVD = School.add_appliance(5, 8, 1, 120, 0.2, 5, occasional_use=0.3, name="stereo")
S_DVD.windows([480, 780], [0, 0], 0.35)

S_Freezer = School.add_appliance(1, 200, 1, 1440, 0.2, 30, "yes", 3, name="freezer")
S_Freezer.windows([0, 1440])
S_Freezer.specific_cycle_1(200, 20, 5, 10)
S_Freezer.specific_cycle_2(200, 15, 5, 15)
S_Freezer.specific_cycle_3(200, 10, 5, 20)
S_Freezer.cycle_behaviour(
    [580, 1200], [0, 0], [510, 579], [0, 0], [0, 509], [1201, 1440]
)

S_PC = School.add_appliance(25, 150, 1, 240, 0.2, 45, name="PC")
S_PC.windows([480, 780], [0, 0], 0.35)

S_Phone_charger = School.add_appliance(5, 5, 1, 180, 0.2, 10, name="phone_charger")
S_Phone_charger.windows([480, 780], [0, 0], 0.35)

S_Printer = School.add_appliance(1, 20, 1, 30, 0.2, 5,  occasional_use=0.5,name="printer")
S_Printer.windows([480, 780], [0, 0], 0.35)

S_DataDisplay = School.add_appliance(3, 420, 1, 60, 0.2, 10,  occasional_use=0.5,name="Data Display")
S_DataDisplay.windows([480, 780], [0, 0], 0.35)

S_Radio = School.add_appliance(5, 35, 1, 120, 0.2, 5,  occasional_use=0.3,name="Radio")
S_Radio.windows([480, 780], [0, 0], 0.35)

if __name__ == "__main__":
    from ramp.core.core import UseCase

    uc = UseCase(
        users=User_list,
        parallel_processing=False,
    )
    uc.initialize(peak_enlarge=0.15)

    Profiles_list = uc.generate_daily_load_profiles(flat=False)

    # post-processing
    from ramp.post_process import post_process as pp

    Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
        Profiles_list
    )
    pp.Profile_series_plot(
        Profiles_series
    )  # by default, profiles are plotted as a series
    if (
        len(Profiles_list) > 1
    ):  # if more than one daily profile is generated, also cloud plots are shown
        pp.Profile_cloud_plot(Profiles_list, Profiles_avg)

    # this would be a new method using work of @mohammadamint
    # results = uc.export_results()
















