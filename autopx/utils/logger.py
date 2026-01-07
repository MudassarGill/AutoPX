# autopx/utils/logger.py

import logging
import sys

class Logger:
    """
    Simple wrapper around Python's logging module for AutoPX.
    """

    def __init__(self, name="AutoPX", level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Avoid adding multiple handlers if logger is already configured
        if not self.logger.handlers:
            # Console handler
            ch = logging.StreamHandler(sys.stdout)
            ch.setLevel(level)
            
            # Simple format: [LEVEL] message
            formatter = logging.Formatter("[%(levelname)s] %(message)s")
            ch.setFormatter(formatter)
            
            self.logger.addHandler(ch)
    
    def info(self, msg):
        self.logger.info(msg)
    
    def warning(self, msg):
        self.logger.warning(msg)
    
    def error(self, msg):
        self.logger.error(msg)
    
    def debug(self, msg):
        self.logger.debug(msg)
