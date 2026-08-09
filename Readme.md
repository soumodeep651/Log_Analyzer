# Production Log Analyzer

A Python-based log analysis tool built as part of my Python for DevOps practice.

## What it does

The program:

- Reads a production-style log file line by line
- Counts total log lines
- Counts ERROR entries
- Extracts error messages
- Groups errors with dynamic values into common error categories
- Produces an error summary

## Example

```text
Total lines: 1500
Errors: ...

Error summary:
  Database connection failed: ...
  Failed to process job: ...
  Timeout connecting to Redis: ...