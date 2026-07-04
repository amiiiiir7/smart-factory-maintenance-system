# 🏭 Smart Factory Maintenance System

A Python Object-Oriented Programming (OOP) project that evaluates the maintenance condition of industrial machines based on their operating hours and maintenance interval.

## Features

* Calculate machine usage ratio
* Evaluate machine health
* Determine machine maintenance status
* Generate a formatted maintenance report

## Project Structure

```text
smart-factory-maintenance-system/
│
├── machine.py
├── maintenance_evaluator.py
├── main.py
└── README.md
```

## Business Logic

The machine usage ratio is calculated as:

```text
Usage Ratio = Operating Hours / Maintenance Interval
```

The machine is then classified into one of the following categories:

| Usage Ratio | Health Score | Status                 |
| ----------- | ------------ | ---------------------- |
| 0.00 – 0.25 | Excellent    | Healthy                |
| 0.25 – 0.50 | Good         | Healthy                |
| 0.50 – 0.75 | Fair         | Monitor                |
| 0.75 – 1.00 | Poor         | Preventive Maintenance |
| > 1.00      | Critical     | Stop Machine           |

## Example Output

```text
=============================================
         MACHINE MAINTENANCE REPORT
=============================================
Machine ID           : M-1007
Operating Hours      : 1850 hours
Maintenance Interval : 2400 hours
---------------------------------------------
Usage Ratio          : 0.77
Health Score         : Poor
Machine Status       : Preventive Maintenance
=============================================
```

## Technologies

* Python 3
* Object-Oriented Programming (OOP)

## Roadmap

* [ ] Manage multiple machines using a `Factory` class
* [ ] Read and save machine data using CSV files
* [ ] Analyze maintenance data with NumPy
* [ ] Perform factory-wide analysis using Pandas
* [ ] Build a predictive maintenance model with Machine Learning

---

**Author:** Amir Shabani

*This project was developed as part of my journey toward Data Science and Artificial Intelligence by strengthening my Python and software engineering skills.*

