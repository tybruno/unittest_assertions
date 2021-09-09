import pytest
from tests.base import BasicAsssertionTester
from unittest_assertions.control import AssertRaises, AssertWarns, AssertLogs


def _raise(e):
    raise e


class TestAssertRaises(BasicAsssertionTester):
    _assertion = AssertRaises

    @pytest.mark.parametrize(
        "testing_data",
        (
            (KeyError, _raise, KeyError),
            (KeyError, _raise, KeyError("key")),
        ),
    )
    def test_assertion_passes(self, testing_data: tuple):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (
                KeyError,
                lambda: None,
            ),
        ),
    )
    def test_assertion_raises(self, testing_data: tuple):
        super().test_assertion_raises(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        ((KeyError, _raise, ValueError),),
    )
    def test_assertion_error(self, testing_data: tuple):
        assert_raises = self._assertion()
        with pytest.raises(testing_data[2]):
            assert_raises(*testing_data)


class TestAssertWarns(BasicAsssertionTester):
    _assertion = AssertWarns

    @pytest.mark.parametrize(
        "testing_data",
        (
            (Warning, _raise, Warning),
            (Warning, _raise, Warning("Warning")),
        ),
    )
    def test_assertion_passes(self, testing_data: tuple):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (
                KeyError,
                lambda: None,
            ),
        ),
    )
    def test_assertion_raises(self, testing_data: tuple):
        super().test_assertion_raises(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        ((KeyError, _raise, ValueError),),
    )
    def test_assertion_error(self, testing_data: tuple):
        assert_raises = self._assertion()
        with pytest.raises(testing_data[2]):
            assert_raises(*testing_data)