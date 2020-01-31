import pandas as pd
import csv
from numpy import nan as Nan
import requests
from bs4 import BeautifulSoup
from threading import Thread
from queue import Queue
import os
import time

file_path ='/home/ananta/Documents/Feeds/Breadcrumb/NSCD/2019-07-09/'
old_file = os.path.join(file_path,'old.csv')
new_file = os.path.join(file_path,'input.csv')

queue = Queue(10)
consumer = 8

global data_list
data_list = []
exception_data_list = []
def scrape_breadcrumb(each_store, each_sku, each_url):
    global data_list
    global exception_data_list

    each_store = each_store.strip()
    each_sku = each_sku.strip()
    each_url = each_url.strip()
    headers={'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}
    try:
        source_code = requests.get(each_url, headers=headers)
        soup = BeautifulSoup(source_code.content.decode('utf-8', 'ignore'), "lxml")
        print(each_url)

    
        breadcrumb_set = soup.find_all('div', {'class': 'breadcrumbs'})
        breadcrumb_set = breadcrumb_set[0].text
        each_breadcrumb_string = breadcrumb_set.strip()
        print(each_breadcrumb_string)
    
        data_list.append((each_store, each_sku, each_url, each_breadcrumb_string))

    except:
        print('Exception')
        print('#############################################################################################################')
        each_breadcrumb_string = ''
        exception_data_list.append((each_store, each_sku, each_url, each_breadcrumb_string))

class ProducerThread(Thread):
    def run(self):
        global combolist
        global queue
        while combolist:
            each_row = combolist.pop()
            queue.put(each_row)
            print("Produced")


class ConsumerThread(Thread):
    def run(self):
        global queue
        global result
        while not queue.empty():
            each_row = queue.get()
            each_element = each_row.split(' , ')
            each_store = each_element[0]
            each_sku = each_element[1]
            each_url = each_element[2]
            print("Inside Consumer")
            scrape_breadcrumb(each_store, each_sku, each_url)
            queue.task_done()


def comparision_between_old_and_new(file_path, old_file, new_file):
    global combolist
    new_df = pd.read_csv(new_file).fillna('')
    old_df = pd.read_csv(old_file).fillna('')
    list_of_all_old_sku = list(set(old_df['ProductSKU'].tolist()))
    old_empty_bc_df = old_df[(old_df['BreadCrumb'] == '')]
    old_not_empty_df = old_df[(old_df['BreadCrumb'] != '')]
    all_new_sku_df = new_df[~new_df['ProductSKU'].isin(list_of_all_old_sku)]
    all_new_sku_df = pd.concat([old_empty_bc_df, all_new_sku_df, ], ignore_index=True)
    combolist = all_new_sku_df[['StoreId', 'ProductSKU', 'ProductURL']].apply(lambda x: ' , '.join(x), axis=1).tolist()

    return old_not_empty_df, combolist

def thread_process(consumer):
    producer_thread_list = []
    p1 = ProducerThread()
    producer_thread_list.append(p1)
    consumer_thread_list = [ConsumerThread() for x in range(consumer)]
    for each_producer in producer_thread_list:
        each_producer.start()
    for each_consumer in consumer_thread_list:
        each_consumer.start()
    for each_producer in producer_thread_list:
        each_producer.join()
    for each_consumer in consumer_thread_list:
        each_consumer.join()

    return None

def post_process(file_path,old_not_empty_df):
    columns = ['StoreId', 'ProductSKU', 'ProductURL', 'BreadCrumb']
    output_scraped_df = pd.DataFrame(data_list, columns=columns)
    exception_df = pd.DataFrame(exception_data_list, columns=columns)
    exception_df.to_csv(file_path + '/Exception_df.csv', index=False, encoding='utf-8', quoting=csv.QUOTE_ALL)
    output_scraped_df['BreadCrumb'] = output_scraped_df['BreadCrumb'].apply(lambda x: str(x).replace('BackHome >', '').replace('BackHome > ', '').replace('Home > ', '').replace('Home >', '').replace('HOME > ', '').replace('HOME >', ''))
    empty_df = pd.DataFrame([[Nan, Nan, Nan, Nan]], columns=columns)
    final_df = pd.concat([old_not_empty_df, empty_df, output_scraped_df], ignore_index=True)
    final_df.drop_duplicates(subset=['ProductSKU','ProductURL'], keep='first', inplace=True)
    final_df.to_csv(file_path + '/final_ready_to_deliver_with_QA.csv', index=False, encoding='utf-8',quoting=csv.QUOTE_ALL)

if __name__ == '__main__':
    start_time = time.time()
    old_not_empty_df, combolist = comparision_between_old_and_new(file_path,old_file, new_file)
    thread_process(consumer)
    post_process(file_path,old_not_empty_df)
    print("--- %s seconds ---" % (time.time() - start_time))

