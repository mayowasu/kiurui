.. SPDX-FileCopyrightText: 2026 Julian Malinowski
.. SPDX-License-Identifier: CC0-1.0

############
Contributing
############

Before you begin
================

Make sure you have a **supported version of Python installed (>3.11)**, and that you're working in the directory where kiurui is located.

Create a virtual environment
============================

Create a new virtual environment (replace `/path/to/new/virtual/environment` with your preferred location):

.. code-block:: bash

   python3 -m venv /path/to/new/virtual/environment

For example:

.. code-block:: bash

   python3 -m venv .kiurui

Activate the virtual environment
================================

Activation steps `depend on your operating system <https://docs.python.org/3/library/venv.html>`_.

Install dependencies
====================

Make sure you use latest `pip <https://pip.pypa.io/en/stable/>`_:

.. code-block:: bash

   pip install --upgrade pip

Install `uv <https://docs.astral.sh/uv/>`_:

.. code-block:: bash

   pip install uv

Install the development dependencies:

.. code-block:: bash

   uv sync --extra dev --active

Set up pre-commit hooks
=======================

.. code-block:: bash

   pre-commit install

Build the project
=================

.. code-block:: bash

   uv build

Before you commit
=================

Useful tools that this project uses.

Lint and format with Ruff
-------------------------

`Ruff <https://docs.astral.sh/ruff/>`_ is a fast Python linter and formatter written in Rust:

.. code-block:: bash

   ruff check
   ruff format

Check licensing with Reuse
--------------------------

`Reuse <https://reuse.software/>`_ ensures licensing your project is easy, comprehensive, unambiguous, and machine-readable:

.. code-block:: bash

   reuse lint
