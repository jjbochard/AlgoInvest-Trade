
bruteforce:
	python bruteforce.py 20 500 actions.csv

optimized:
	python optimized.py 500 actions.csv

sienna1:
	python sienna_optimized.py 50000 dataset1.csv

sienna2:
	python sienna_optimized.py 50000 dataset2.csv

all_sienna:
	python sienna_optimized.py 50000 dataset1.csv
	python sienna_optimized.py 50000 dataset2.csv
