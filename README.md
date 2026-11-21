# Automation Progression Week1

# Week 1: Python Fundamentals

**Dates:** 16–22 November 2026
**Focus:** Variables, functions, loops, lists, dictionaries, exception handling and Git basics
**Main resource:** Harvard CS50P, lectures 0–3

## What I built this week

| Topic | File |
| --- | --- |
| Functions and variables | `hello.py` |
| Lists and dictionaries | `food.py` |
| Loops and exception handling | `numbers.py` |
| Git basics: first commits and push to GitHub (Friday) | — |
| Mini project: Lead Sorter CLI (Saturday) | `lead_sorter.py` |

## Mini project: Lead Sorter CLI

A command-line program that asks for leads one at a time, grades each one as **hot**, **warm** or **cold**, and prints a summary at the end. It brings together everything from this week: functions, conditionals, loops, dictionaries and exception handling.

### How it grades a lead

- **Hot:** [e.g. budget of $5,000 or more and ready to start within 30 days]
- **Warm:** [e.g. a good budget or a short timeline, but not both]
- **Cold:** everything else

### How to run it

```bash
python lead_sorter.py
```

Type each lead's name, budget and timeline when prompted. Type `done` to finish and see the summary.

### Example

```text
Lead name: Maria
Budget: 6000
Days until start: 14
Lead name: done

Summary
Hot:  1 (Maria)
Warm: 0
Cold: 0
```

## What I learned

- [One thing that clicked]
- [One thing that was hard]
- [One Git thing, e.g. the difference between commit and push]

## What I'd improve next

- [e.g. save the leads to a file so they aren't lost when the program closes; this is week 2's topic]

