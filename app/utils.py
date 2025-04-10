import logging


# 設定日誌紀錄
def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


# 示範使用
if __name__ == '__main__':
    logger = setup_logger('main_logger', 'app.log')
    logger.info("這是一則資訊日誌")
