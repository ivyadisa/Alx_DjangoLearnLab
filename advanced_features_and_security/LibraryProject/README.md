# Permissions and Groups Setup

## Custom Permissions
Defined in `relationship_app/models.py` → Book model:
- can_view
- can_create
- can_edit
- can_delete

## Groups
Configured via Django Admin:
- Viewers → can_view
- Editors → can_view, can_create, can_edit
- Admins → all permissions

## Views
Permission checks applied using `@permission_required` in `relationship_app/views.py`.

## Testing
- Assign users to groups via Admin.
- Test by logging in as each role and verifying access restrictions.
