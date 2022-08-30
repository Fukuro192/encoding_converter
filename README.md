# encoding_converter

A python script for converting strings from encoding to another the fastest way possible.

## usage

let's say you have a garbled string, you know the encoding, you need to run this command

```bash
python3 encoding_converter.py <my_garbled_string> --from <source-encoding> --to <destination-encoding>
```

## example

```
$ python3 encoding_converter.py У·Ц{МъЙ╣Р║СfН▐ПW --from IBM866 --to Shift_JIS
日本語音声素材集
```

## help message

```
usage: encoding_converter.py [-h] -s SOURCE [-d DESTINATION] string

positional arguments:
  string                the value to be converted, for example:
                        У·Ц{МъЙ╣Р║СfН▐ПW

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE, --from SOURCE
                        the source encoding of the wanted string, for example:
                        IBM866
  -d DESTINATION, --destination DESTINATION, --to DESTINATION
                        the destination encoding of the wanted string, for
                        example: Shift_JIS
```