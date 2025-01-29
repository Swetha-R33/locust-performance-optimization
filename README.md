# Locust Performance Optimization

This repository contains performance tests for the `/cart` and `/browse` routes optimized using Locust.

## Optimizations Made
- **Token Caching:** The authentication token is now cached after the first login and reused for all requests.
- **Task Weighting:** The `/browse` route is more likely to be hit than the `/cart` route, simulating real-world usage patterns.
- **Wait Time:** Realistic wait times are added between requests to simulate human-like behavior.
- **Header Management:** Headers are efficiently managed, and unnecessary headers are eliminated.

## Requirements
- Python 3.9+
- Locust

## How to Run Tests

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
 
