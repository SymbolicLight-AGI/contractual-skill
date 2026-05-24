**Missing Information & Assumptions**
To execute this TDD cycle, I need the following missing information:
- Target programming language and test framework (e.g., Python/pytest, TypeScript/Jest, Java/JUnit).
- Relevant code location (file names for the service and test file).
- The test command to run (e.g., `npm test`, `pytest`).

I have drafted the plan and the first test using generic pseudo-code/TypeScript as an assumption. We must run this test and observe it failing (RED) before writing any production code.

### TDD Plan for Retry Behavior

We will break the requirements down into the smallest testable behaviors and implement them one by one:

1. **Behavior 1:** Service does not retry on a `400 Bad Request` response and returns the error immediately.
2. **Behavior 2:** Service does not retry on a `401 Unauthorized` response and returns the error immediately.
3. **Behavior 3:** Service retries exactly once if the first response is `503 Service Unavailable` and the second response is successful (`200 OK`).
4. **Behavior 4:** Service retries up to a maximum of 3 times on consecutive `503` responses, then throws/returns the final error.
5. **Behavior 5:** Service applies exponential backoff timing between the `503` retries.

---

### Draft of First Test (Behavior 1)

Here is the draft of the first minimal test. It uses a mock HTTP client to ensure we are testing the retry boundary without hitting a real network.

```typescript
// Assumption: TypeScript / Jest framework
// File: service.test.ts

import { fetchData } from './service';
import { httpClient } from './httpClient';

jest.mock('./httpClient');

describe('Service Retry Behavior', () => {
  it('should not retry on 400 Bad Request', async () => {
    // Arrange
    const mockRequest = httpClient.request as jest.Mock;
    mockRequest.mockRejectedValue({ status: 400, message: 'Bad Request' });

    // Act
    await expect(fetchData()).rejects.toMatchObject({ status: 400 });

    // Assert
    // It should only be called exactly once (no retries)
    expect(mockRequest).toHaveBeenCalledTimes(1);
  });
});
```

---

### Current TDD Status

- **Behavior Under Test:** Service does not retry on `400 Bad Request`.
- **RED Evidence:** *[Pending]* Cannot execute test. Awaiting test command and framework confirmation.
- **GREEN Evidence:** *[Pending]* No production code will be written until RED is observed.
- **Refactor Notes:** *[Pending]*
- **Remaining Gaps:** Missing the specific language, test framework, code location, and test execution command.
- **Next TDD Step:** Please provide the missing framework and test command details, or confirm if the TypeScript/Jest assumption is acceptable. Once confirmed, I will need you to run the test (or allow me to run it if in an executable environment) to provide the RED command output. After we verify it fails for the expected reason, I will provide the minimal production code to make it pass.
