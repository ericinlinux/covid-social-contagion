# Opinion Contagion Model


##### Disconnecting for the good: A network-oriented model for social contagion of opinions and social network interventions to increase adherence to social distancing


###### Eric Araujo (eric at ufla dot br)

---

This repository contains the codes and results obtained for the paper "Disconnecting for the good: A network-oriented model for social contagion of opinions and social network interventions to increase adherence to social distancing". 

## Jupyter Notebook

To run the python notebook provided inside the code folder, go to the folder and install the requirements by typing 

```
pip install -r requirements.txt
```

To start the Jupyter Notebook interface on your browser, give the command:

```
jupyter notebook
```


## Running Netlogo script

To run the simulations use the following command lines. These commands were tested on a Mac OSx 10.15.4

```
./netlogo-headless.sh \
  --model Simulation.nlogo \
  --experiment Basic_100_people \
  --table ../results/basic_100_people_table.csv \
  --spreadsheet ../results/basic_100_people_spreadsheet.csv
```

```
./netlogo-headless.sh \
  --model Simulation.nlogo \
  --experiment Basic_100_people_End \
  --table ../results/basic_100_people_end_table.csv \
  --spreadsheet ../results/basic_100_people_end_spreadsheet.csv
```

```
./netlogo-headless.sh \
  --model Simulation.nlogo \
  --experiment Interventions_100_people_End \
  --table ../results/interv_100_people_end_table.csv \
  --spreadsheet ../results/interv_100_people_end_spreadsheet.csv
```

## Results Notebook

To visualize the notebook with the graphics and results obtained in our study, [click here](./code/Data_Analysis.ipynb).

## Netlogo code

The simulation code is available in the [folder for Netlogo](./code/Netlogo).