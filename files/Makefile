.PHONY: test
all: extract transform load

extract_catalogs:
	echo "Extracting catalogs...."
	python3 ./extract_catalogs.py -o ./tmp/

extract:
	echo "Extracting datasets...."
	python3 ./extract_datasets.py -o ./tmp/

load_catalogs:
	echo "Loading catalogs...."
	python3 -u ./load_catalogs.py -o ./tmp/

load:
	echo "Loading datasets...."
	python3 ./load_datasets.py -o ./tmp/

clean:
	rm ./tmp/*.json
