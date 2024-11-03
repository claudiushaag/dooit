from typing import TYPE_CHECKING, Optional

from dooit.api import Workspace
from ._base import ApiComponent


if TYPE_CHECKING: # pragma: no cover
    from dooit.ui.tui import Dooit


class VarManager(ApiComponent):
    def __init__(self, app: "Dooit") -> None:
        super().__init__()
        self.app = app

    @property
    def theme(self):
        return self.app.current_theme

    @property
    def current_workspace(self) -> Optional[Workspace]:
        tree = self.app.workspace_tree
        if tree.highlighted is None:
            return None

        return tree.current_model
