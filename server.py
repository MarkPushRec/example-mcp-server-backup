# Partial contents of /Users/mark/Documents/MCP_Servers/example-mcp-server/mcp_simple_tool/server.py

# This file contains the organize_imports method that needs fixing

def organize_imports(resource):
    # Problem: The code tries to handle ChangeSet object incorrectly
    # The error occurs in the method below:
    # 'ChangeSet' object has no attribute 'splitlines'
    try:
        # Use the proper ImportOrganizer API
        # Create ImportOrganizer instance
        import_organizer = ImportOrganizer(project)
        
        # Use the organize_imports method directly
        # This method returns a ChangeSet object or None
        changes = import_organizer.organize_imports(resource)
        
        result += "Organizing imports:\n\n"
        
        # Apply changes if requested (default is preview mode)
        apply = should_apply_changes(params)
        
        if changes is not None:
            # Format the changes
            result += f"Changes to organize imports in {resource.path}:\n\n"
            
            # Get the modified source code
            # The ChangeSet contains a ChangeContents object with the new source
            for change_item in changes.changes:
                if hasattr(change_item, 'resource') and hasattr(change_item, 'new_contents'):
                    # Show the diff
                    diff = difflib.unified_diff(
                        code.splitlines(True),
                        change_item.new_contents.splitlines(True),
                        fromfile=f"Original: {resource.path}",
                        tofile=f"Modified: {resource.path}"
                    )
                    result += ''.join(diff) + "\n"
            
            # Apply if requested
            if apply:
                project.do(changes)
                result += "Changes have been applied.\n"
            else:
                result += "\nRun with 'apply: true' to apply these changes.\n"
        else:
            result += "No changes needed.\n"
    except exceptions.RefactoringError as e:
        result += f"Refactoring error: {str(e)}\n"
    except Exception as e:
        result += f"Error organizing imports: {str(e)}\n"