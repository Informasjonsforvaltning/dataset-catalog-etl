.PHONY: test
all: extract transform load

catalogs:
	echo "Extracting catalogs...."
	python3 ./extract_catalogs.py -o ./tmp/

extract:
	echo "Extracting datasets...."
	python3 ./extract_datasets.py -o ./tmp/

transform:
	echo "Transforming datasets...."
	python3 -u ./transform_datasets.py -o ./tmp/

load:
	echo "Loading datasets...."
	python3 ./load_datasets.py -o ./tmp/

clean:
	rm ./tmp/*.json
