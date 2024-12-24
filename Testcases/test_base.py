import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:

    def assert_link(self, actual_link, Expected):
        if actual_link != [Expected]:
            self.logger.error("*********************** Assersion Failed *******************")
        assert actual_link == [Expected], "Assert not equal for " + Expected + " Link ""."
        self.logger.info("************** Assertion for " + Expected + " Passed *************************")

