#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: myloging.py
# author:gaobo
# time:2019/03/08
import logging
from logging.handlers import RotatingFileHandler # 按文件大小滚动备份
from Common.path import log_dir
import colorlog  # 控制台日志输入颜色
import time
import datetime
import os



if not os.path.exists(log_dir): os.mkdir(log_dir)  # 如果不存在这个log文件夹，就自动创建一个
logName = os.path.join(log_dir, '%s.log' % time.strftime('%Y-%m-%d'))  # 文件的命名

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}


class Logging:
    def __init__(self, logName=logName):
        self.logName = logName
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.formatter = colorlog.ColoredFormatter('%(log_color)s[%(asctime)s] [%(filename)s:%(lineno)d] [%(levelname)s]- %(message)s',log_colors=log_colors_config)  # 日志输出格式
        self.handle_logs()

    def get_file_sorted(self, file_path):
        """最后修改时间顺序升序排列 os.path.getmtime()->获取文件最后修改时间"""
        dir_list = os.listdir(file_path)
        if not dir_list:
            return
        else:
            dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
            return dir_list

    def TimeStampToTime(self, timestamp):
        """格式化时间"""
        timeStruct = time.localtime(timestamp)
        return str(time.strftime('%Y-%m-%d', timeStruct))

    def handle_logs(self):
        """处理日志过期天数和文件数量"""
        file_list = self.get_file_sorted(log_dir)  # 返回按修改时间排序的文件list
        if file_list:  # 目录下有日志文件
            for i in file_list:
                file_path = os.path.join(log_dir, i)  # 拼接文件的完整路径
                t_list = self.TimeStampToTime(os.path.getctime(file_path)).split('-')
                now_list = self.TimeStampToTime(time.time()).split('-')
                t = datetime.datetime(int(t_list[0]), int(t_list[1]),
                                      int(t_list[2]))  # 将时间转换成datetime.datetime 类型
                now = datetime.datetime(int(now_list[0]), int(now_list[1]), int(now_list[2]))
                if (now - t).days > 5:  # 创建时间大于2天的文件删除
                    self.delete_logs(file_path)
            if len(file_list) > 10:  # 限制目录下记录文件数量
                file_list = file_list[0:-4]
                for i in file_list:
                    file_path = os.path.join(log_dir, i)
                    self.delete_logs(file_path)

    def delete_logs(self,file_path):
        try:
            os.remove(file_path)
        except PermissionError as e:
            self.warning('删除日志文件失败：{}'.format(e))

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = RotatingFileHandler(filename=self.logName, mode='a', maxBytes=1024*1024*5, backupCount=5,
                                 encoding='utf-8')  # 使用RotatingFileHandler类，滚动备份日志
        fh.setLevel(logging.INFO)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = colorlog.StreamHandler()
        ch.setLevel(logging.ERROR)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level =='exception':
            self.logger.exception(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()  # 关闭打开的文件

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)
    def exception(self,message):
        self.__console('exception', message)


if __name__ == '__main__':
    log =  Logging()
    for i in range(1000):
        log.info('123132')
