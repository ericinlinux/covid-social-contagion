# Disconnecting for good: understanding how interventionsbased on social network analysis could reduce the spread ofthe COVID-19 and increase self-isolation adherence


### Running Netlogo script


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


./netlogo-headless.sh \
  --model Simulation.nlogo \
  --experiment Interventions_100_people_End \
  --table ../results/interv_100_people_end_table.csv \
  --spreadsheet ../results/interv_100_people_end_spreadsheet.csv
