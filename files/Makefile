.PHONY: test
all: extract transform load

extract_dataservices:
	echo "Extracting...."
	python3 ./extract_dataservices.py -o ./tmp/

extract_datasets:
	echo "Extracting...."
	python3 ./extract_datasets.py -o ./tmp/

transform_dataservices:
	echo "Transforming...."
	python3 -u ./transform_dataservices.py -o ./tmp/

transform_datasets:
	echo "Transforming...."
	python3 -u ./transform_datasets.py -o ./tmp/

load_datasets:
	echo "Loading...."
	python3 ./load_datasets.py -o ./tmp/

load_dataservices:
	echo "Loading...."
	python3 ./load_dataservices.py -o ./tmp/

clean:
	rm ./tmp/*.json
