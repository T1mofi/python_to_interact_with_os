import os
import datetime

filename = 'paul_hudsons_swift_ui_lesson.txt'

file_size = os.path.getsize(filename)
edit_timestamp = os.path.getmtime(filename)
edit_datetime = datetime.datetime.fromtimestamp(edit_timestamp)
file_path = os.path.abspath(filename)

print(f'File\'s size is = {file_size}\nit was edited last time at {edit_datetime}\nthe path of the file is {file_path}')
