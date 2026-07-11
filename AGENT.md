Each sub-directory handles one kind of project as follows:

rust
    Handles projects using Rust programming language

Agents using this repository for validating some other project are hereby called foreign agents.

Agents whose purpose is to update this repository are called native agents.

Instructions for foreign agents
-------------------------------

Determine which sub-directory that matches most closely to the type of project to be validated or setup. Only use one sub-directory.

The information in the directory can be used in either of two ways:

1. For setting up the project, creating the files describing how the development should work
2. Validating an existing project to make sure the process related files still follow the way of working

Instructions for native agents
------------------------------

This repository should contain knowledge found on Internet, and any related best practice that makes sense to use.

For engineering project, a simplified and adapted version of INCOSE should be used as the base foundation.

When creating a new sub-directory, check if there is an existing sub-directory which is similar in nature. For example, if creating a sub-directory for programming in some language, check if there is a directory for programming in some other language. If so, try to make the content of the new directory similar to the existing sub-directory but adapted for the new programming language.

When creating or updating any process documents in this repository, always check if the proposed change would make sense to apply for similar sub-directories as well and if so, implement those changes as well. Also validate that the resulting process still make sense, since this will be a mix of several proposed ways of working from different sources.

All changes to this repository should be done as one or more PR:s, where the last PR must be mergeable to main branch.