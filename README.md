# File_Checker
Simple program to check txt files

in settings.ini
```[FILES]
mainFile1 = 1.txt
archiveFile1 = 2.txt
```

mainFile1
```
16561198155423429|SurvivorM_Oliver|3|0		//27.02.2023
36561198873525958|SurvivorM_Oliver|3|0		//26.01.2022
76561198054981234|SurvivorM_Oliver|2|0		//27.01.2022
56561198832168086|SurvivorM_Oliver|1|0		//27.01.2020

66561198094004288|SurvivorM_Oliver|2|0		//20.01.2022
26561198873525958|SurvivorM_Oliver|3|0		//10.01.2021
56561198832168086|SurvivorM_Oliver|1|0		//27.01.2020
66561198094004288|SurvivorM_Oliver|2|0		//20.01.2022
```

archiveFile1
```
56561198832168086|SurvivorM_Oliver|1|0		//27.01.2020
66561198094004288|SurvivorM_Oliver|2|0		//20.01.2022
26561198873525958|SurvivorM_Oliver|3|0		//10.01.2021
56561198832168086|SurvivorM_Oliver|1|0		//27.01.2020
66561198094004288|SurvivorM_Oliver|2|0		//20.01.2022
```

script check date after '//'. 
if the current date is later than in the file, the line is transferred to the archive file and generally deleted in main file
