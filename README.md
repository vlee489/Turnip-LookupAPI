# Turnip-LookupAPI
The lookup package that powers Turnip Bot

This library is used by Turnip Bot for acquiring lookup data.

# NookipediaAPI
This class is responsible for acquiring data from Nookipedia Private API, and
has parts derived from [async-nookipedia](https://github.com/makupi/async-nookipedia)
by [makupi](https://github.com/makupi). Hence `nookipediaAPI.py` is licenced
under **GNU General Public License v3.0**. Changes made are stated in the
`CHANGES` file at the root of the repo.

# turnipLookup
This class is responsible for looking up and caching items via Turnip Bot's own
database located in an AWS DynamoDB instance. 
