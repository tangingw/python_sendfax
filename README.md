# Sending Fax with Python Script

## Synopsis

This is a small script that I wrote to send documents to my parents' fax machine using [Phaxio API](https://github.com/phaxio/phaxio-python).

## Installation

Before you use this API, please register yourself at [Phaxio](https://www.phaxio.com) and obtain both API key and API secret.

To install the Phaxio Python SDK

```python
    pip install -r requirements.txt
```

## Usage

```python
    python send_fax.py <PHONE NUMBER E.164 format> <filename>
```