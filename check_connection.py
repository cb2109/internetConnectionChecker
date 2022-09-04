import socket
import time
import datetime
import os
import logging


def check_connection():
    log_file_name = "network.log"
    log_file = os.path.join(os.getcwd(), log_file_name)
    configure_logging(log_file)
    mon_net_connection()


def configure_logging(log_file):
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())


def mon_net_connection(ping_freq=2):
    monitor_start_time = datetime.datetime.now()
    motd = "Network connection monitoring started at: " + format_date(monitor_start_time) \
           + " Sending ping request in " + str(ping_freq) + " seconds"
    logging.info(motd)
    total_time_down = datetime.timedelta(seconds=0)
    while True:
        if send_ping_request():
            logging.debug("Pinging at " + format_date(datetime.datetime.now()))
            time.sleep(ping_freq)
        else:
            total_time_down = total_time_down + monitor_outage()
            logging.error("Total Time since start " + format_duration(total_time_down))


def monitor_outage():
    down_time = datetime.datetime.now()
    fail_msg = "Network Connection Unavailable at: " + format_date(down_time)
    logging.error(fail_msg)
    i = 0
    while not send_ping_request():
        time.sleep(1)
        i += 1
        if i >= 3600:
            i = 0
            now = datetime.datetime.now()
            continuous_message = "Network Unavailable Persistent at: " + format_date(now)
            logging.warning(continuous_message)

    up_time = datetime.datetime.now()
    uptime_message = "Network Connectivity Restored at: " + format_date(up_time)
    logging.info(uptime_message)
    down_time_duration = calculate_time(down_time, up_time)
    down_time_message = "Network Connection was Unavailable for " + format_duration(down_time_duration)
    logging.error(down_time_message)
    return down_time_duration


def send_ping_request(host='8.8.8.8', port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket()
        s.connect((host, port))
    except OSError:
        return False
    else:
        s.close()
        return True


def calculate_time(start, stop):
    time_difference = stop - start
    seconds = float(str(time_difference.total_seconds()))
    return datetime.timedelta(seconds=seconds)


def format_date(date):
    return str(date).split(".")[0]


def format_duration(duration):
    return str(duration)
