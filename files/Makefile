.PHONY: test
all: extract transform load

extract:
	echo "Extracting catalogs...."
	python3 ./extract_catalogs.py -o ./tmp/

transform:
	echo "Transforming catalogs...."
	python3 ./transform_uris.py -o ./tmp/
	python3 ./transform_catalogs.py -o ./tmp/

load:
	echo "Loading catalogs...."
	python3 ./load_catalogs.py -o ./tmp/

clean:
	rm ./tmp/*.json
