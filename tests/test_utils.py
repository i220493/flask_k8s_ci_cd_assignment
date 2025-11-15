from flask_k8s_ci_cd_assignment.utils import add_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5
