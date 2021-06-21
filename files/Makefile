.PHONY: test
all: extract transform load

extract:
	echo "Extracting datasets...."
	python3 ./extract_datasets.py -o ./tmp/
	python3 ./extract_dataservices.py -o ./tmp/

transform:
	echo "Transforming datasets...."
	python3 ./transform_datasets.py -o ./tmp/

load:
	echo "Loading datasets...."
	python3 ./load_datasets.py -o ./tmp/

clean:
	rm ./tmp/*.json
