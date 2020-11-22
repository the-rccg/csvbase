# The CSV "(data)base"

Turn any directory with CSVs into a SQL query-able data-base-thingy.
All the benefits of human readable, portable, interoperable data.
None of the commitment of a database.

## Benefits

* Human readable data storage (duh it's CSVs)
* Trivial interoperability (it's CSVs)
* No technical knowledge required
* Allows querying with SQL!

## Drawbacks

* None of the performance gains of databases

## Mitigation

* Asynchronous parallel querying of CSVs?

## Installation and usage

Install via `pip install .` in the directory.

Run simply as e.g. `csvbase --port=5000 --debug` in the repository you like.

### Flags

* port (int): port to run the flask server on
* directory (string): directory path to map if not the current work directory
* debug (boolean): run flask server in debug mode or not
