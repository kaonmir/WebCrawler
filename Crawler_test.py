def print_value_list(values):
    for val in values:
        if val == 'web':
            print('THIS IS, ')
        elif val == 'crawler':
            print('Web Crawler!')

if __name__=='__main__':
    value_list = ['how', 'to', 'make', 'web', 'crawler']
    print_value_list(value_list)
