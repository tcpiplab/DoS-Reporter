import logging

# Create a logger for the 'dos' messages
dos_logger = logging.getLogger('dos_logger')
dos_logger.setLevel(logging.INFO)  # Set the minimum logging level to INFO

# Create a FileHandler for the 'dos' logger
dos_handler = logging.FileHandler('dos_log.log')
dos_handler.setLevel(logging.INFO)  # Set the minimum logging level to INFO

# Create a logger for the 'target_status' messages
target_status_logger = logging.getLogger('target_status_logger')
target_status_logger.setLevel(logging.INFO)  # Set the minimum logging level to INFO

# Create a FileHandler for the 'target_status' logger
target_status_handler = logging.FileHandler('target_status_log.log')
target_status_handler.setLevel(logging.INFO)  # Set the minimum logging level to INFO

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
dos_handler.setFormatter(formatter)
target_status_handler.setFormatter(formatter)

# Add the handlers to the loggers
dos_logger.addHandler(dos_handler)
target_status_logger.addHandler(target_status_handler)

def log_response(response):
    response_parts = [
        f'Response:',
        f'{response.status_code} {response.reason}',
        "\n".join(f"{k}: {v}" for k, v in response.headers.items()),
        response.text,
    ]
    target_status_logger.info("\n".join(response_parts))
