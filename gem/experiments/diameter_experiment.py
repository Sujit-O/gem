import os
def plot_hist(title,data):
    import matplotlib.pyplot as plt
    plt.figure()
    plt.hist(x=data)
    plt.savefig(title+'.png')


def get_diams(graph_nme, hyps, num_iters):


    diam_list = []
    avg_deg_list = []
    if graph_nme == 'barabasi_albert_graph':
        print '=========================== ' + graph_nme + '============================'
        n = hyps['n']
        m = hyps['m']
        for i in range(num_iters):
            if i % 10 == 0:
                print graph_nme, '______________ ', i
            G = nx.barabasi_albert_graph(n=n, m=m)
            diam_list.append(nx.algorithms.diameter(G))
            avg_deg_list.append(np.mean(nx.degree(G).values()))

        plot_hist(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/plots/' + graph_nme + '_AvgDeg' + '_iter_' + str(
                num_iters), avg_deg_list)
        plot_hist(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/plots/' + graph_nme + '_Diam' + '_iter_' + str(
                num_iters), diam_list)

        print avg_deg_list

    if graph_nme == 'watts_strogatz_graph':
        n = hyps['n']
        k = hyps['k']
        p = hyps['p']
        print '=========================== ' + graph_nme + '============================'
        for i in range(num_iters):
            if i % 10 == 0:
                print graph_nme, '______________ ', i
            G = nx.watts_strogatz_graph(n=n, k=k,p=p)
            diam_list.append(nx.algorithms.diameter(G))
            avg_deg_list.append(np.mean(nx.degree(G).values()))

        plot_hist(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/plots/' + graph_nme + '_AvgDeg' + '_iter_' + str(
                num_iters), avg_deg_list)
        plot_hist(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/plots/' + graph_nme + '_Diam' + '_iter_' + str(
                num_iters), diam_list)

        print avg_deg_list

    if graph_nme == 'random_geometric_graph':
        print '=========================== ' + graph_nme + '============================'
        n = hyps['n']
        radius = hyps['radius']
        for i in range(num_iters):
            if i % 10 == 0:
                print graph_nme, '______________ ', i
            G = nx.random_geometric_graph(n=n, radius=radius)
            diam_list.append(nx.algorithms.diameter(G))
            avg_deg_list.append(np.mean(nx.degree(G).values()))

        plot_hist(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/plots/' + graph_nme + '_AvgDeg' + '_iter_' + str(
                num_iters), avg_deg_list)
        plot_hist(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/plots/' + graph_nme + '_Diam' + '_iter_' + str(
                num_iters), diam_list)

        print avg_deg_list

    if graph_nme == 'powerlaw_cluster_graph':
        print '=========================== ' + graph_nme + '============================'
        n = hyps['n']
        m = hyps['m']
        p = hyps['p']

        for i in range(num_iters):
            if i%10 == 0:
                print graph_nme, '______________ ',i
            G = nx.powerlaw_cluster_graph(n=n, m=m, p=p)
            diam_list.append(nx.algorithms.diameter(G))
            avg_deg_list.append(np.mean(nx.degree(G).values()))

        plot_hist(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/plots/' + graph_nme + '_AvgDeg' + '_iter_' + str(
                num_iters), avg_deg_list)
        plot_hist(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/plots/' + graph_nme + '_Diam' + '_iter_' + str(
                num_iters), diam_list)
        print avg_deg_list

    if graph_nme == 'duplication_divergence_graph':
        print '=========================== '+graph_nme+'============================'
        n = hyps['n']
        p = hyps['p']

        for i in range(num_iters):
            if i%10 == 0:
                print graph_nme, '______________ ',i
            G = nx.duplication_divergence_graph(n=n, p=p)
            diam_list.append(nx.algorithms.diameter(G))
            avg_deg_list.append(np.mean(nx.degree(G).values()))

        plot_hist(os.path.abspath(os.path.join(os.getcwd(), os.pardir))+'/plots/'+graph_nme + '_AvgDeg' + '_iter_' + str(num_iters), avg_deg_list)
        plot_hist(os.path.abspath(os.path.join(os.getcwd(), os.pardir))+'/plots/'+graph_nme + '_Diam' + '_iter_' + str(num_iters), diam_list)

        print avg_deg_list

    if graph_nme == 'dorogovtsev_goltsev_mendes_graph':
        print '=========================== ' + graph_nme + '============================'
        n = hyps['n']
        create_using = hyps['create_using']

        for i in range(num_iters):
            if i%10 == 0:
                print graph_nme, '______________ ',i
            G = nx.dorogovtsev_goltsev_mendes_graph(n=n)

            diam_list.append(nx.algorithms.diameter(G))
            avg_deg_list.append(np.mean(nx.degree(G).values()))

        plot_hist(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/plots/' + graph_nme + '_AvgDeg' + '_iter_' + str(
                num_iters), avg_deg_list)
        plot_hist(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/plots/' + graph_nme + '_Diam' + '_iter_' + str(
                num_iters), diam_list)

        print avg_deg_list

    if graph_nme == 'waxman_graph':
        print '=========================== ' + graph_nme + '============================'
        n = hyps['n']
        alpha = hyps['alpha']
        beta = hyps['beta']

        for i in range(num_iters):
            if i%10 == 0:
                print graph_nme, '______________ ',i
            G = nx.waxman_graph(n=n, alpha=alpha, beta=beta)
            if nx.is_connected(G) == False:
                # print nx.connected_components(G)


                for item in nx.connected_components(G):
                    print '_______', nx.info(item)
            exit()
            diam_list.append(nx.algorithms.diameter(G))
            avg_deg_list.append(np.mean(nx.degree(G).values()))

        plot_hist(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/plots/' + graph_nme + '_AvgDeg' + '_iter_' + str(
                num_iters), avg_deg_list)
        plot_hist(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/plots/' + graph_nme + '_Diam' + '_iter_' + str(
                num_iters), diam_list)

        print avg_deg_list


if __name__=='__main__':
    import networkx as nx
    import numpy as np
    import json

    with open('diam_syn_hyps.conf','r') as fp:
        syn_hyps = json.load(fp)

    num_iters = 10
    graph_names = syn_hyps.keys()
    for i in range(num_iters):
        G = nx.waxman_graph(n=1024, alpha=0.099, beta=0.1)
        for j in nx.connected_components(G):

            print '+_+_+_+_+_+_+_+_ ____ ',j
    exit()
    for graph_nme in graph_names:

        hyps = syn_hyps[graph_nme]

        get_diams(graph_nme,hyps, num_iters)
