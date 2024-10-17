from __future__ import annotations

import pytest

from pre_commit_hooks.erase_data_loader_keys import main
from testing.util import get_resource_path


@pytest.mark.parametrize(
    ('filename', 'expected_retval'), (
        ('envelope_project_bad.prjx', 1),
        ('envelope_project_ok.prjx', 0),
    ),
)
def test_main(filename, expected_retval):
    ret = main([get_resource_path(filename)])
    assert ret == expected_retval
