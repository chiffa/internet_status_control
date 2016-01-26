"""
Long-term idea: build a progressive map of the network by tracerouting different hosts
and building a tree of how the packets are routed towards that network.
Then render it as a network
"""

import subprocess
import platform
import numpy as np
from matplotlib import pyplot as plt
from textwrap import wrap
from datetime import datetime, timedelta
import click
# import networkx

os_name = platform.system()
print os_name


@click.group()
def main():
    pass


@click.command()
@click.argument('hostname')
def trace(hostname):
    # TODO: perform tracert several times and do stats on the several times run

    if os_name == 'Windows':
        p = subprocess.Popen(['tracert', hostname],
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

    else:
        raise Exception("Don't work on Linux or MacOS for now :S")

    out, err = p.communicate()
    outlist = [line.split('  ') for line in out.split('\r\n') if line]

    parse_= []
    host_names = []

    for line in outlist[2:-1]:
        line = [word.strip() for word in line if word]
        line = line[1:]
        host_names.append(line[-1].split(' ')[0])
        line_parse = []
        for word in line[:-1]:
            if ' ms' in word:
                if '<' in word:
                    word = word[1:]
                line_parse.append(int(word[:-3]))
            elif '*' in word:
                line_parse.append(np.nan)
            else:
                raise Exception('unrecognized character: %s' % word)
        parse_.append(line_parse)

    # host_names = np.array(host_names)[:, np.newaxis]
    # parse_ = np.array(parse_)
    # mean_ping = np.mean(parse_, axis=1)[:, np.newaxis].astype(np.int)
    # var_ping =  np.var(parse_, axis=1)[:, np.newaxis].astype(np.int)
    #
    # results_stack = np.hstack((mean_ping, var_ping, host_names))
    #
    # print results_stack
    #
    # names_ = host_names[:, 0]

    # print parse_
    # TODO: break here: this is where we stop getting raw data and are switching to the analysis

    mean_ping = np.nanmean(parse_, axis=1).astype(np.int)
    std_ping = np.nanstd(parse_, axis=1).astype(np.int)
    lost_ping = np.sum(np.isnan(parse_), axis=1).astype(np.int)

    timed_out = lost_ping > 2
    print timed_out
    mean_ping[timed_out] = -1
    std_ping[timed_out] = -1
    host_names = np.array(host_names)
    host_names[timed_out] = 'Request timed out'
    host_names = host_names.tolist()

    mean_ping = mean_ping.tolist()
    std_ping = std_ping.tolist()
    lost_ping = lost_ping.tolist()

    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            step = int(rect.get_x())
            plt.text(rect.get_x() + rect.get_width()/2., 1.05*rect.get_height(),
                    '%s +/- %s ms %s' % (rect.get_height(), std_ping[step], '*'*lost_ping[step]),
                    ha='center', va='bottom')

    N = len(host_names)
    ind = np.arange(N)
    width=0.35

    means_ = plt.bar(ind, mean_ping, width, color='r')
    vars_ = plt.bar(ind + width, std_ping, width, color='y')

    host_names = ['\n'.join(wrap(name)) for name in host_names]

    plt.ylabel('ms')
    plt.xticks(ind+width, host_names, rotation='vertical')
    plt.legend((means_[0], vars_[0]), ('Mean', 'Std'))

    autolabel(means_)

    plt.title("Tracing '%s' %s" % (hostname , datetime.now().strftime(" on %Y-%m-%d at %H:%M")))
    plt.gcf().set_size_inches(8, 9)
    plt.tight_layout(pad=1.4)
    plt.gcf().set_size_inches(8, 9)
    plt.show()


main.add_command(trace)


if __name__ == "__main__":
    # TODO: embed in a 15 minute loop
    # TODO: make it log the results and then compute the long - term statistics.
    main()
    # trace(hostname='facebook.com')
    # ping_round('youtube.com')
    # ping_round('client4.google.com')
