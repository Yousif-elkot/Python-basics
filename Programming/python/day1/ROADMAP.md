# Project Roadmap

A living plan to evolve the Day 1 projects (Unit Converter + Phone Book) into more robust, testable, and extensible tools while practicing professional Python habits.

---
## Vision
Build small CLI utilities that progressively adopt real software engineering practices: modular design, testing, data modeling, packaging, and maintainability.

## Guiding Principles
- Start simple → refactor toward purity + testability.
- Prefer pure functions that return data over printing.
- Add structure only when justified by complexity.
- Small, frequent, documented commits.
- Tests first for pure logic; wrap I/O separately.

---
## Milestone 1: Testable Core (Foundations)
**Goal:** Make logic functions independent from user input/output.
- [ ] Refactor `add_contact`, `delete_contact`, `search_contact` into core logic functions (e.g., `add_contact(name, phone, contacts)` → `(ok, message)`).
- [ ] Add interactive wrappers that call pure functions.
- [ ] Alphabetically list contacts in `show_all_contacts`.
- [ ] Normalize names to lowercase internally; preserve original casing for display.
- [ ] Add `requirements.txt` (even if empty placeholder for now).
- [ ] Create `tests/` folder.
- [ ] Add tests for unit converter functions (`km_to_miles`, etc.).
- [ ] Add tests for phone book core logic (adding empty name/phone, duplicate name handling decision).

## Milestone 2: Data Model Upgrade (Phone Book)
**Goal:** Support richer contact info + future growth.
- [ ] Change JSON structure to:
	```json
	{"version": 1, "contacts": {"john doe": {"name": "John Doe", "phone": "123", "email": null}}}
	```
- [ ] Migration logic: if old flat dict detected → transform + save.
- [ ] Introduce optional fields: email, notes (nullable).
- [ ] Add `edit_contact` (update phone/email/notes).
- [ ] Validate phone (digits + optional leading '+').

## Milestone 3: CLI Enhancements
**Goal:** Improve usability + flexibility.
- [ ] Case-insensitive & partial search (substring match).
- [ ] Add export (`contacts.csv`) + import (CSV → JSON merge).
- [ ] `--non-interactive` / argparse mode for scripted use (e.g., add/search/delete).
- [ ] Introduce colored output (optional later via `rich`).

## Milestone 4: Reliability & Tooling
**Goal:** Harden workflows and structure.
- [ ] Atomic save (write temp file then rename).
- [ ] Logging (use `logging` module at INFO/WARNING instead of some prints).
- [ ] Add `.editorconfig` + choose a linter (`ruff` or `flake8`).
- [ ] Add GitHub-friendly badges / doc links (future).
- [ ] Basic coverage check (e.g., `pytest --maxfail=1 -q`).

## Milestone 5: Packaging & Distribution
**Goal:** Prepare for reuse and sharing.
- [ ] Move code into `src/` layout.
- [ ] Add `pyproject.toml` (set project metadata, dependencies, scripts).
- [ ] Create console entry points: `phonebook`, `unit-convert`.
- [ ] Publish (optional) to TestPyPI.

---
## Cross-Cutting Improvements
| Area | Action | Benefit |
|------|--------|---------|
| Input Handling | Wrap `input()` calls in thin functions | Mocking in tests |
| Pure Logic | Return `(ok, message, data?)` tuples | Deterministic behavior |
| Data Validation | Centralize validators (phone, email) | Consistency |
| Error Handling | Guard JSON parsing & schema | Prevent silent corrupt data |
| Naming | Consistent snake_case + descriptive verbs | Readability |

---
## Stretch Goals (Later)
- Fuzzy search (`difflib`).
- SQLite backend instead of JSON.
- Contact categories & tagging.
- Time-based backups / restore points.
- Combined "toolbox" CLI with both apps under one command group.

---
## Suggested Commit Sequence (Example)
1. refactor(phone): add pure add_contact logic + wrapper
2. test(converter): add tests for conversion functions
3. chore: add requirements.txt + tests folder
4. feat(phone): alphabetical listing + normalized names
5. refactor(phone): add atomic save logic
6. feat(converter): generic conversion mapping

---
## Open Questions (Decide Early)
- Overwrite existing contact silently or require confirm? (Choose policy.)
- Enforce unique phone numbers? (Optional.)
- Email validation strict or basic? (Start basic.)

---
## Immediate Next Actions (You Can Do Now)
- [ ] Refactor one phone book function to core + wrapper.
- [ ] Add `tests/test_conversions.py` with 4 basic asserts.
- [ ] Create `requirements.txt`.
- [ ] Add alphabetical display + lowercase key normalization.

> Keep revisiting this roadmap after each milestone; trim or reorder as you learn.

