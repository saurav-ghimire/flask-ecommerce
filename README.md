# Project Name

## Overview
Provide a brief description of your project, its purpose, and any important features.

## Tests and CI/CD Integration

### Unit Tests

We have implemented the following unit tests to ensure the quality and functionality of the application:

1. **Route Test**:
   - Verifies that invalid HTTP methods (e.g., POST on a GET-only route) return the correct status code (405).

2. **Database Read Operation**:
   - Checks if the MongoDB connection is successful using the ping command.

3. **Database Write Operation**:
   - Tests the insertion and retrieval of a document in the MongoDB database to ensure data can be written and read correctly.

### CI/CD Pipeline

Our CI/CD pipeline is automated using GitHub Actions. Here's how it works:

- The pipeline runs every time there is a **push** or **pull request** to the `main` branch.
- It checks out the code, installs dependencies, and runs all unit tests.
- If any tests fail, the pipeline will notify the team, and the changes will not be merged until the issues are resolved.
- Test results are stored in `test-report.xml` and can be downloaded as artifacts for review.

This ensures that our code remains functional and stable with every change.

