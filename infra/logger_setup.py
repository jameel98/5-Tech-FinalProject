import logging


class LogSetup:
    def __init__(self):
        self.logger = self.setup_logger()

    def setup_logger(self):
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,  # Set the logging level to INFO
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler("../test_log.log"),  # Log to a file
                logging.StreamHandler()  # Log to console
            ]
        )
        return logging.getLogger(self.__class__.__name__)
