.. SPDX-FileCopyrightText: 2026 Julian Malinowski
.. SPDX-License-Identifier: CC0-1.0

######
kiurui
######

***************************************
A Python program to generate passwords.
***************************************

|reuse| |ruff| |uv|

.. |reuse| image:: https://api.reuse.software/badge/codeberg.org/kiichigo/kiurui
   :target: https://api.reuse.software/info/codeberg.org/kiichigo/kiurui
   :alt: REUSE status

.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
   :target: https://github.com/astral-sh/ruff
   :alt: Ruff

.. |uv| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json
   :target: https://github.com/astral-sh/uv
   :alt: uv

What does kiurui do?
====================

It has two options to generate a password:

* Alphanumeric - by default 16 characters (min. 3), 1 uppercase letter, 1 lowercase letter and at least 1 digit.
* Passphrase - by default it takes EFF's Long Wordlist and creates a 6-word password. You can specify another file if you wish. More information is available at https://www.eff.org/dice.

How to use?
===========

See `SETUP <https://kiichigo.codeberg.page/kiurui/SETUP.html>`_

Contributing
============

See `CONTRIBUTING <https://kiichigo.codeberg.page/kiurui/CONTRIBUTING.html>`_

License
=======

`Apache-2.0 <https://spdx.org/licenses/Apache-2.0.html>`_
