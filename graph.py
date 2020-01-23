def create_function_graph(path="./"):
    g=networkx.DiGraph() # create direct graph 
    files_to_parse=get_python_files(path) #only python files
    allFunctions=[]
    tmpFunctions=[]
    #creating nodes
    for file in files_to_parse:
        allFunctions+=get_functions_names_from_file(path+"/"+file)
        tmpFunctions=get_functions_names_from_file(path+"/"+file)
        for fun in tmpFunctions:
            g.add_node(fun,waga = count_method_size(path+"/"+file,fun))
    #creating edges
    for file in files_to_parse:
        for fun in allFunctions :
            for otherFun in allFunctions:
                methodCount=count_method(path+"/"+file,fun,otherFun)
                if(methodCount>0):
                    g.add_edge(fun,otherFun,weight = methodCount)

    ##  labels copied from other graph
    matplotlib.pyplot.figure()
    pos = networkx.spring_layout(g)
    networkx.draw(g,pos, with_labels=True, font_weight='bold')
    
    pos_attr = {}
    for node, coords in pos.items():
        pos_attr[node] = (coords[0], coords[1] +00.07)
    
    node_attr = networkx.get_node_attributes(g, 'waga')
    custom_node_attrs = {}
    for node, attr in node_attr.items():
        custom_node_attrs[node] = str(attr)

    edge_labels = dict([((u,v),d['weight']) for u,v,d in g.edges(data=True)])
    networkx.draw_networkx_edge_labels(g,pos,edge_labels = edge_labels)

    networkx.draw_networkx_labels(g,pos_attr, labels=custom_node_attrs)
    ##
    matplotlib.pyplot.show()
