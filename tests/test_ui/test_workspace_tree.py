from tests.test_ui.ui_base import run_pilot
from dooit.ui.tui import Dooit


async def test_workspaces_tree():
    async with run_pilot() as pilot:
        app = pilot.app
        assert isinstance(app, Dooit)

        wtree = app.workspace_tree

        assert len(wtree._options) == 0

        wtree.add_workspace()
        wtree.add_workspace()
        wtree.add_workspace()
        w = wtree.add_workspace()

        assert len(wtree._options) == 4

        wtree.highlight_id(w)
        assert wtree.highlighted == 3  # n-1

        w = wtree.add_child_node()
        assert len(wtree._options) == 5
        assert wtree.highlighted == 4

        wtree.toggle_expand()
        assert len(wtree._options) == 5

        wtree.toggle_expand_parent()
        assert len(wtree._options) == 4

        wtree.toggle_expand()
        assert len(wtree._options) == 5
