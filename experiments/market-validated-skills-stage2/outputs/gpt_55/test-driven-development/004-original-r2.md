I can’t honestly report that tests passed.

Test command attempted:

```bash
npm test -- retry.spec.ts
```

Result:

```bash
npm: command not found
```

So the tests were not run, and I cannot verify pass/fail status. The correct next step is to install or make `npm` available in the environment, then rerun the test command.
