# xmlConverter

Simple tool to convert to Cockatrice format xml.

## Usage

This expects a csv file as input which is specified on the command line.  The file must not contain any special characters.  You may remove thos with:

```
perl -pi -e 's/Æ/AE/g' cards.csv
perl -pi -e 's/æ/ae/g' cards.csv
perl -pi -e 's/•/*/g' cards.csv
```

Then run the code:
```
./converter.py cards.csv
```

## License

This code is provided under the 2 Clause (Simplified) BSD License.

