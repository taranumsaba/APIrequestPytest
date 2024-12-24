import logging
import os

class LogGen:

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        p = os.getcwd().replace("\\Pages", "")
        s = p.replace("\\Testcases", "")
        path = s.__add__("\\Logs\\logfile.log")
        handler_info = logging.FileHandler(path)
        handler_info.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%y %I:%M:%S %p")
        handler_info.setFormatter(formatter)
        logger.addHandler(handler_info)
        logger.info("Information")
        return logger


