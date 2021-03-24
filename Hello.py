#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask import request, jsonify, send_from_directory, abort
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
import xlrd

app = Flask(__name__)

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    global pd_frame
    if request.method == 'POST':
        file = request.files['file']
        f = file.read()  # 文件内容
        data = xlrd.open_workbook(file_contents=f)

        # f.save(secure_filename(f.filename))
        # data_and_names = []

        # table = data.sheets()[0]
        # names = data.sheet_names()  # 返回book中所有工作表的名字
        # # N张表
        # for i, name in enumerate(names):
        #     i_name = data.sheet_by_name(name)
        #     temp_j = list()
        #     for j in range(i_name.nrows):
        #         if j == 0:
        #             temp_columns = i_name.row_values(j)
        #         else:
        #             temp_j.append(i_name.row_values(j))
        #     data_and_names[i] = pd.DataFrame.from_dict(temp_j)
        #     data_and_names[i].columns = temp_columns

        return jsonify({'data': 'ok'})

@app.route("/download/<path:filename>")
def download(filename):
    if request.method=="GET":
        if os.path.isfile(os.path.join('upload', filename)):
            return send_from_directory('upload', filename, as_attachment=True)
        abort(404)

if __name__ == '__main__':
   app.run(host = '127.0.0.1', debug = True)
