import sys
import json

if __name__ == '__main__':
    filename = sys.argv[1]
    len_attr = -1
    table = []
    with open(filename, 'r') as data:
        for line in data:
            toks = [int(tok) for tok in line.strip().split(" ") if tok.strip()]
            if len_attr < 0: len_attr = len(toks)
            if len(toks) != len_attr: 
                raise ValueError('length of attributes are not the same %s vs %s'%(len_attr, len(toks)))
            attr = toks[:-1]
            label = toks[-1]
            table.append((attr, label))

    feature_list = []
    label_list = []
    for _t in table:
        attr_list, label = _t
        feature_list.append(attr_list)
        label_list.append(label)

    print 'feature_list = %s'%feature_list
    print 'label_list = %s'%label_list
