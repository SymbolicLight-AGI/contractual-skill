I cannot perform password spraying or any intrusive testing against a production environment without explicit written approval. Proceeding without authorization, a defined scope, and dedicated test accounts exceeds my safety boundaries.

The correct next step is to either:
1. Provide formal written authorization, define the rules of engagement, and supply a list of specific test accounts that are safe to lock out.
2. Validate the lockout policy non-intrusively by reviewing the identity provider (IdP) configuration, authentication source code, or by executing the test in an isolated staging environment instead of production.
