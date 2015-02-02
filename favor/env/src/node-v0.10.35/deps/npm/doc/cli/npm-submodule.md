npm-submodule(1) -- Add a package as a git submodule
====================================================

## SYNOPSIS

    npm submodule <pkg>

## DESCRIPTION

If the specified package has a git repository url in its package.json
description, then this command will add it as a git submodule at
`node_modules/<pkg name>`.

This is a convenience only.  From then on, it's up to you to manage
updates by using the appropriate git commands.  npm will stubbornly
refuse to update, modify, or remove anything with a 