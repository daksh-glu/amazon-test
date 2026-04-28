# Amazon Automation Test

Automated test cases for Amazon using Playwright + Python, 
running in parallel.

## Test Cases
- Test Case 1: Search iPhone, add to cart, print price
- Test Case 2: Search Samsung Galaxy, add to cart, print price
- Both tests run in parallel simultaneously

## Setup Instructions

1. Install Python from python.org
2. Open terminal and run:
   pip install playwright
   playwright install
3. Run the test:
   python test_amazon.py

## Output
[iPhone] Price: INR 76,242.48
[Samsung Galaxy] Price: INR 81,893.10
Both tasks completed in parallel!

## Note
Amazon may block cart addition for automated scripts 
without a logged-in session. Price extraction works 
successfully in parallel.

## Tech Stack
- Python
- Playwright (async)
- asyncio (for parallel execution)
