# coiled-project

This project allows testing all possible interactions between pytask, pytask-parallel
and coiled.

Requires Python 3.11 or newer.

Install dependencies with `just install` and run type checking with `just typing`.
The lockfile records revisions of pytask and pytask-parallel. CI refreshes those two
dependencies from their main branches before checking this project.
