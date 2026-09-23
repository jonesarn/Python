# AGENTS

## Project context

This workspace is a small Python scratch project. There is no formal app structure, package metadata, or README to infer project conventions from, so keep changes minimal and direct.

- The active script is `new.py`.
- The project interpreter lives in `python.py/.venv`.
- `main.py` appears to be an empty placeholder.

## Working conventions

- Prefer small, self-contained edits over introducing new architecture or tooling.
- Keep scripts runnable from the workspace root without adding project-wide setup unless it is clearly required.
- Preserve the existing Python environment and avoid creating extra virtual environments when the repo already has one.
- Use explicit imports and keep dependency assumptions visible in the file being edited.

## Validation

Run scripts through the existing venv instead of a system Python:

```powershell
c:\Users\armojon\Desktop\Python\python.py\.venv\Scripts\python.exe c:/Users/armojon/Desktop/Python/new.py
```

## Notes for AI agents

- Do not assume a package build step exists.
- Do not add README-heavy documentation unless the project grows beyond a scratch script.
- When editing `new.py`, keep the existing `boto3` and `bracket` usage in mind and avoid broad refactors.
- If a requested change requires new dependencies, verify they can be installed into the existing venv before restructuring the code.
