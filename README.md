# MCP Server Backup

This repository contains a backup of an example MCP server with the rope tool implementation that has an issue with the organize_imports operation.

## Current Issue

The organize_imports operation is returning the following error:

```
Error organizing imports: 'ChangeSet' object has no attribute 'splitlines'
```

The error occurs because the code is trying to use the splitlines() method on a ChangeSet object instead of on a string.