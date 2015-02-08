#! /usr/bin/env bash

# je treba mit v ceste programy vlna, vlnaPlav, texPodpis

for i in `ls tex/*.tex`;do
	# spusti klasickou Olsakovu vlnu
    vlna -l $i;
    # spusti alternativni pythovskou vlnu
    vlnaPython -f $i;
    # spusti skrip, ktery vyrobi pekne hlavicky pro vase soubory, nahradte podle potreby
    texPodpis -f $i -a "Tomas Trnka" -e tomas@trnkatomas.eu www.svetovka.cz
done
