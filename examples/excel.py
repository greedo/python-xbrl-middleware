#! /usr/bin/env python
# encoding: utf-8

from xbrl import XBRLParser
from xbrl_middleware import ExcelDump

xbrl_parser = XBRLParser(precision=0)

# Parse an incoming XBRL file
xbrl = xbrl_parser.parse(file("sam-20130629.xml"))

# Parse just the GAAP data from the xbrl object
gaap_obj = xbrl_parser.parseGAAP(xbrl,
                                 doc_date="20130629",
                                 doc_type="10-Q",
                                 context="current",
                                 ignore_errors=0)

# Dump the GAAP data to XLSX (Excel)
xbrl_dump = ExcelDump(gaap_obj)
xbrl_dump.dump('demo.xlsx')
