# xmlConverter

Simple tool to convert to Cockatrice format xml.

## Usage

This expects a 2 csv files as input which is specified on the command line.  The file must not contain any special characters.  You may remove those with:

```
perl -pi -e 's/Æ/AE/g' Cards\ CSV.csv
perl -pi -e 's/æ/ae/g' Cards\ CSV.csv
perl -pi -e 's/•/*/g' Cards\ CSV.csv
perl -pi -e 's/Æ/AE/g' Skills_CSV.csv
perl -pi -e 's/æ/ae/g' Skills_CSV.csv
```

Then run the code:
```
./converter.py Cards\ CSV.csv Skills_CSV.csv
```

## License

This code is provided under the 2 Clause (Simplified) BSD License.

