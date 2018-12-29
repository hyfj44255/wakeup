from flask import Flask
from subprocess32 import PIPE, Popen, check_call

app = Flask(__name__)


@app.route('/z2')
def hello_world2():
    return 'Hello, World2!'


@app.route('/kill')
def hello_killer():
    return process_killer('z1') + " " + process_killer('z2'), 200


def process_killer(name):
    p1 = Popen(["ps -ef"], stdout=PIPE, shell=True)
    output = p1.communicate()[0]
    processes = str(output, 'utf-8')
    processes_list = processes.split('\n')
    processes_list.pop(0)
    pids = []
    for process in processes_list:
        if process.find(name) != -1:
            elements = process.strip().split(' ')
            formal = [ele for ele in elements if ele]
            pids.append(formal[1])

    killer = 'kill -9'
    for pid in pids:
        if pid:
            killer = killer + ' ' + pid
    res = check_call(killer, shell=True)
    return str(killer)


# def process_killer(process):
#     p1 = Popen(["ps -ef"], stdout=PIPE, shell=True)
#     p2 = Popen(["grep", process], stdin=p1.stdout, stdout=PIPE, shell=True)
#     p1.stdout.close()
#     output = p2.communicate()[0]
#     processes = str(output, 'utf-8')
#     processes_list = processes.split('\n')
#     pids = []
#     for process in processes_list:
#         pids.append(process.strip().split(' ')[0])
#
#     killer = 'kill -9'
#     for pid in pids:
#         if pid:
#             killer = killer + ' ' + pid
#     res = check_call(killer, shell=True)
#     return str(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=52, debug=True)

