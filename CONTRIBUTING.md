# Contributing to models_lang

Contributions improve local-model qualification, fine-tuning, and optimization experiments while preserving explicit distinctions between candidate discovery, pipeline tests, and benchmark qualification.

## Before you start

Read the [README](README.md) and the [qualification track](conductor/tracks/local-model-qualification_20261108/index.md). Respect the versioned qualification result contract and the existing separation between Intel/OpenVINO training, retrieval sidecars, and other runtime environments.

Search existing issues and pull requests to avoid duplicating work. Describe substantial proposals before implementation, and use repository issue or pull request templates when available. Small corrections can go directly into a focused pull request.

For bug reports, include the affected version or commit, environment, minimal reproduction, expected and actual behavior, and sanitized diagnostics. For feature requests, explain the use case and intended outcome.

## Development and validation

The README lists focused verification commands. For example, the Intel configuration test is:

```powershell
python -m pytest training\tests\test_intel_lora_config.py
```

Use the documented environment for the affected lane and run the corresponding tests, recording exact versions and results. Keep synthetic smoke-training evidence separate from held-out performance measurements and live runtime acceptance.

A catalogue entry is discovery metadata, not certification. Record model and dataset revisions, licenses, hardware, resource limits, evaluation conditions, and known dependency conflicts. Preserve isolated environments where the README describes incompatible stacks. Do not change model defaults or claim qualification based on an unrelated model's result. Keep weights and caches outside ordinary source changes.

Update affected documentation and examples alongside behavior changes. Add a focused regression case for a bug fix where executable tests are appropriate. Record checks that were not run and the reason.

## Submitting a pull request

Create a focused branch from the current `main` branch and open a pull request back to it. Keep unrelated formatting, refactoring, and dependency changes separate.

Include:

- The problem, proposed change, and resulting behavior.
- Related issues or existing track references.
- Exact validation commands or inspection steps, results, and limitations.
- Compatibility implications and any data or dependency provenance.

Inspect the complete diff before submission. Required automated checks must pass before merge. Follow the existing repository and account policies; this guide does not introduce a second-person approval requirement or relax existing checks.

## Security and sensitive information

Follow the [account security policy](https://github.com/edithatogo/.github/blob/main/SECURITY.md). Report vulnerabilities privately through GitHub's **Report a vulnerability** option if available. Otherwise request a private reporting contact without disclosing the vulnerability publicly. Keep credentials, personal data, and unredacted logs out of commits, issues, and examples.

## Licensing and conduct

Preserve existing attribution and applicable source or package terms. This guide does not grant a new license. Submit only material you are entitled to contribute, and document unclear permissions before adding third-party content. Follow the [account code of conduct](https://github.com/edithatogo/.github/blob/main/CODE_OF_CONDUCT.md). This guide adds no CLA, mandatory sign-off, or relicensing condition.

## Reference guidance

- [GitHub contributor guidelines](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
- [OpenSSF Best Practices criteria](https://www.bestpractices.dev/en/criteria)
